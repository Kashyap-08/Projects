import dotenv
import os
import pymongo

dotenv.load_dotenv('.env')

user_id = os.environ['USERID']
password = os.environ['PASSCODE']

def get_db_conn(db_name):
    '''
    :param db_name: database name to connect
    :return: database object
    '''
    try:
        client = pymongo.MongoClient(f"mongodb+srv://{user_id}:{password}@cluster01.n7r3noi.mongodb.net/?retryWrites=true&w=majority")
        db = client[db_name]
        print("DB connection is successful.")
        return db
    except Exception as e:
        print("Error While connecting to MongoDB database named: ", db_name)
        print(e)

def insert(db, table_name, data):
    '''
    :param db: Get the Database object
    :param table_name: table name available in DB to connect
    :param data: Data to be inserted. Data should contain a list of dictionary i.e. [{},{}]
    :return: None
    '''
    try:
        conn = db[table_name]
        conn.insert_many(data)
        print("Data Insertion Completed")
    except Exception as e:
        print("Error while inserting data into table: ", table_name)
        print(e)


def get_all(db, table_name):
    '''
    :param db: Get the Database object
    :param table_name: table name available in DB to connect
    :return: whole table data
    '''
    try:
        coll = db[table_name]
        records = coll.find({}, {"_id":0})

        return records
    except Exception as e:
        print("Error while fetching records form table: ", table_name)
        print(e)

def delete_table(db, table_name):
    '''
    :param db: Get the Database object
    :param table_name: table name available in DB to delete
    '''
    try:
        coll = db[table_name]
        coll.drop
    except Exception as e:
        print("Error while deleting table: ", table_name)
        print(e)




