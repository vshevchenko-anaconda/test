import os
from pymongo import MongoClient

MONGO_URL = os.getenv('ANACONDA_MONGO_URL_TESTING', 'localhost')


def main():
    client = MongoClient(MONGO_URL)
    raise Exception(list(client.test_database.users.find()))


if __name__ == '__main__':
    main()
