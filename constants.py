connDetailsWin: dict = {
    'db': 'tgap-ng',
    'usr': 'postgres',
    'psw': 'montero', #TODO: remove this detail before publishing any code, VERY UNSAFE!
    'host': '127.0.0.1',
    'port': '5432'
}

connDetailsUbu: dict = {
    'db': 'tgap-ng',
    'usr': 'postgres',
    'psw': 'brio', #TODO: remove this detail before publishing any code, VERY UNSAFE!
    'host': '127.0.0.1',
    'port': '5432'
}

LimburgTinyTgapEdgeOriginal: str = 'public.top10nl_limburg_tiny_tgap_edge'

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
