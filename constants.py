from enum import Enum

connDetailsWin: dict = {
    'db': 'tgap-ng',
    'usr': 'postgres',
    'psw': 'password',
    'host': '127.0.0.1',
    'port': '5432'
}

connDetailsUbu: dict = {
    'db': 'tgap-ng',
    'usr': 'postgres',
    'psw': 'password', 
    'host': '127.0.0.1',
    'port': '5432'
}

#Initial Datasets
LimburgOrig: str = 'public.top10nl_9x9_face'
LimburgTest: str  = 'public.top10nl_limburg_tiny_face'

class datasetsFace(Enum):
    LimburgSmallTest = 'public.top10nl_limburg_tiny_face'
    LimburgSubset1 = 'public.top10nl_limburg_subset1_face'
    LimburgSubset2 = 'public.top10nl_limburg_subset2_face'
    LimburgSubset3 = 'public.top10nl_limburg_subset3_face'
    LimburgOriginal = 'public.top10nl_9x9_face'

class resultingDatasetsEdge(Enum):
    LimburgSubset1 = 'public.top10nl_limburg_subset1_tgap_edge'
    LimburgSubset2 = 'public.top10nl_limburg_subset2_tgap_edge'

def generateSelectAllFunction(table: str, args: list = None) -> str:
    """Helper function, used for generating an SQL command which retreives all entries and all data from a certain table
    It selects all objects if no args is provided in the call of the function.

    TODO: adapt function to take in more variables, like WHERE, IN, etc."""

    #Ternary operator
    selectors: list[str] = ["*"] if args is None else args
    
    sqlCommand: str = 'SELECT '
    for elem in selectors:
        sqlCommand += elem + " "
    
    sqlCommand += f'from {table}'
    print(sqlCommand)

    return sqlCommand
