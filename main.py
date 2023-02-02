import os
from pymongo import MongoClient

MONGO_URL = os.getenv('ANACONDA_MONGO_URL_TESTING', 'localhost')


def main():
    client = MongoClient(MONGO_URL)
    return client.test_database.find()


if __name__ == '__main__':
    main()