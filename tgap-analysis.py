#from tkinter.tix import Tree
from unittest import result
from psycopg2 import connect, ProgrammingError
from constants import connDetailsUbu, connDetailsWin, generateSelectAllFunction, resultingDatasetsEdge
from pandas import DataFrame, array
from geopandas import GeoSeries
from numpy import array, column_stack, ndarray, nditer
from data_structures import Edge
from shapely import wkb, wkt
from typing import Tuple
import matplotlib.pyplot as plt

"""Main Script, used for analysing the result of the tgap generation library (https://github.com/bmmeijers/tgap-ng)"""

def connectAndRetrieveFromDB(connDetails: dict, sqlCommand: str) -> Tuple[ndarray, list]: #For python 3.10 better way to return multiple values: returnType1 | returnType2
    """Function used for estabulish a connection to a Postgres Server, run a certain command,
    then return the result of the of the query. 
    
    NOTE: Only DQL operations allowed. The function will check if the SQL starts with the SELECT clause,
    and will otherwise return None without performing the query
    More info on DQL: https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/"""

    #First establish the connection to the DB
    #TODO: add try/catch clause connection + type declaration!
    conn = connect(database=connDetails['db'], user=connDetails['usr'], password=connDetails['psw'], host=connDetails['host'], port=connDetails['port'])

    #Make sure the SQL command is in the right format
    sqlSplit: list = sqlCommand.split(" ")
    if sqlSplit[0] == 'SELECT':
        print("The SQL query is in the right format")
    else:
        print("Please run the script again with a correct sql sequence")
        return None
    
    #Run the SQL DQL command
    try:
        curs = conn.cursor()
        curs.execute(sqlCommand)
        results: list = curs.fetchall()  
        colNames: list = [desc[0] for desc in curs.description]
        #print(results)
    except ProgrammingError:
        print("A connection error has occured")
    finally:
        #Initially this was a Pandas DataFrame, but it's a bad practice to iterate over it 
        #https://stackoverflow.com/a/55557758
        npResult: ndarray = array(results)
        return colNames, npResult

def numberOfPointsPerStep(edgesNP: ndarray, columns: list) -> None:
    """Method used for counting the number of points at each step of the tgap generation
    Goes through each line, counting the number of points and tallying up the counter for that step
    
    Note: End points should be considered once for all edges, so these are added to a special counter
    and added at the end.
    
    TODO: !!!IMPORTANT!!! This implementation is relatively cumbersome, since this is the only way to get 
    nodes from the current result of the tgap generation. This could be perhaps implemented in the genration?
    But for the time being, this should be enough."""

    #Dict for saving the no of points per each step
    #Structure of dict - step (int) : no of points in that step (int)
    noPtsStep: dict = {}

    #Dict for saving the ids of endpoins per step
    #Structure: step (int) : list of endpoint ids
    endpointIdsStep: dict = {}

    #Check if the dataset has geometry as a column
    if "geometry" not in columns:
        #TODO: maybe this condition should change to conditioning the table to be only EDGES?
        print("Please add only tables which contain a geometry column")
        return None

    #transform the geometry column to shapely LineString 
    #And Transform the numpy array into an Edge object
    edgeList = []

    for edgeNP in edgesNP:
        edgeGeomStr = wkb.loads(edgeNP[-1], hex=True)
        edgeNP[-1] = edgeGeomStr #TODO: This only works with geometry in the last place. Change this!
        edgeObj = Edge(edgeNP[0], edgeNP[1],edgeNP[2], edgeNP[3], edgeNP[4], edgeNP[-1])
        edgeList.append(edgeObj)
        #print(edge)
    
    #separate this part in another funtion, too much functionality in this method
    for edge in edgeList:
        #print(f'count Nodes for edge {edge.id}: {len(edge.geom.coords[:])}')
        numNodesInEdge = len(edge.geom.coords[:])
        
        #go through each scale that this edge is 
        #TODO: does not account for end-points! Change to accept that
        for step in range(edge.stepLow, edge.stepHigh):
            #check if this step already exists in our dictionary. if yes add #pts, if no create key
            if step not in noPtsStep:
                #print("This step does not yet exist in our dictionary, it is being created now")
                noPtsStep[step] = numNodesInEdge
            else:
                #print(f'Current points at step {step}: {noPtsStep[step]}')
                noPtsStep[step] += numNodesInEdge
                #print(f'New no of pts at step {step}: {noPtsStep[step]}')

    #OLD VERSION FOR ORDERING
    #noPtsStepOrdered: dict = {}
    #order the dictionary based on the key (so that it can be displayed in a graph)
    #for key, value in noPtsStep.items():
        #print(f'Step: {key}, No Pts: {value}')
        #noPtsStepOrdered[key] = value
    noPtsStepOrdered = dict(sorted(noPtsStep.items()))

    #plot
    fig, ax = plt.subplots()

    ax.plot(list(noPtsStepOrdered.keys()), list(noPtsStepOrdered.values()), linewidth=2.0)

    plt.show()

def main():
    #parameters to be extracted
    #params: list[str] = [""]
    sqlCommand: str = generateSelectAllFunction(resultingDatasetsEdge.LimburgSubset2.value)
    cols, res = connectAndRetrieveFromDB(connDetailsWin, sqlCommand)
    #print(cols, res)
    
    numberOfPointsPerStep(res, cols)

if __name__ == "__main__":
    main()