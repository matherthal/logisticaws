from LogisticaWS.utils import db_utils

def persistMap(map):
    print("Persisting map....")

    db_utils.insertMap(map)