from flask import Flask
from peewee import *


class ConnectDatabase:

    def get_connect_string():
        try:
            with open('connect.txt', "r") as db_name:
                return db_name.readline().strip()
        except:
            print("You need to create a database and store its name in a file named 'connect_str.txt'. \
                  For more info, head over to the README")

    db = PostgresqlDatabase(get_connect_string())
ConnectDatabase.db.connect()
ConnectDatabase.db.create_tables([Test], safe=True)
