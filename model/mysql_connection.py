import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Connection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance
    
    def __init__(self):
        self.__host = os.getenv('MYSQL_HOST')
        self.__user = os.getenv('MYSQL_USER')
        self.__passwd = os.getenv('MYSQL_PASSWORD')
        self.__db = os.getenv('MYSQL_DB')


    def conexion_db(self):

        try:
            print("{}".format(self.__host))


            return mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__passwd,
                database=self.__db)
        
        except Exception as e:
            print("Error de conexion")
            print(e)


if __name__ == "__main__":

    db = Connection()
    db.conexion_db()
