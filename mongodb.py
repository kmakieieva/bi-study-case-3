from pymongo import MongoClient
from pymongo.server_api import ServerApi


def get_database(connection_string):
    CONNECTION_STRING = connection_string
    client = MongoClient(CONNECTION_STRING, server_api=ServerApi('1'))
    return client["canadiantire_reviews"]
