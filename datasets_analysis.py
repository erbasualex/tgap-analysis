from constants import  generateSelectAllFunction, datasetsFace, LimburgOrig, LimburgTest, connDetailsWin
from psycopg2 import connect, ProgrammingError
from pandas import DataFrame, array
from geopandas import GeoSeries
#import numpy as np
from numpy import array, column_stack, ndarray, nditer
from data_structures import Edge
from shapely import wkb, wkt
from typing import Tuple
import matplotlib.pyplot as plt

def connectAndRetrieveFromDB(connDetails: dict, sqlCommand: str) -> Tuple[ndarray, list]:  # For python 3.10 better way to return multiple values: returnType1 | returnType2
    """Function used for estabulish a connection to a Postgres Server, run a certain command,
    then return the result of the of the query.

    NOTE: Only DQL operations allowed. The function will check if the SQL starts with the SELECT clause,
    and will otherwise return None without performing the query
    More info on DQL: https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/"""

    # First establish the connection to the DB
    # TODO: add try/catch clause connection + type declaration!
    conn = connect(database=connDetails['db'], user=connDetails['usr'], password=connDetails['psw'],
                   host=connDetails['host'], port=connDetails['port'])

    # Make sure the SQL command is in the right format
    sqlSplit: list = sqlCommand.split(" ")
    if sqlSplit[0] == 'SELECT':
        print("The SQL query is in the right format")
    else:
        print("Please run the script again with a correct sql sequence")
        return None

    # Run the SQL DQL command
    try:
        curs = conn.cursor()
        curs.execute(sqlCommand)
        results: list = curs.fetchall()
        colNames: list = [desc[0] for desc in curs.description]
        # print(results)
    except ProgrammingError:
        print("A connection error has occured")
    finally:
        # Initially this was a Pandas DataFrame, but it's a bad practice to iterate over it
        # https://stackoverflow.com/a/55557758
        npResult: ndarray = array(results)
        return colNames, npResult

def countTotalFacesAndBuildingFaces(faces: ndarray, columns: list):
    print("Total_number= ", faces.shape)

    buildings_no = 0
    for face in faces:
        face_class = int(face[5])
        if(int(face_class/1000) == 13):
            #print(f"Found a building for face with id {face[4]}")
            buildings_no += 1

    print(f"Buildings= {buildings_no}")


def main():
    # Get total number of faces + num of buildings
    for dataset in datasetsFace:
        print(f"Dataset: {dataset.value}")
        sqlCommand: str = generateSelectAllFunction(dataset.value)
        cols, res = connectAndRetrieveFromDB(connDetailsWin, sqlCommand)

        countTotalFacesAndBuildingFaces(res, cols)
        print("\n")

if __name__ == "__main__":
    main()