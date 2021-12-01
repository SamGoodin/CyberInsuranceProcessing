import pyodbc
import pandas as pd

class database:

    def __init__(self, path):
        self.path = path
        self.__connect()

    def __connect(self):
        conn_string = (
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
            r"Dbq=" + self.path + ";"
        )
        self.conn = pyodbc.connect(conn_string)
        self.cursor = self.conn.cursor()

    def add_client(self, name, location, business_type, industry, revenue, employees):
        sql = "insert into Client (ID,Client_Name,Client_Location,Client_Type_of_Business,Client_Industry,Client_Annual_Revenue,Client_Num_of_Employees,Policy_ID) values (2,Sam,Indy,Software,Film,125.00,27,27)"
        print(sql)
        self.cursor.execute(sql)
        
    def get_all_clients(self):
        sql = "select * from Client"
        self.cursor.execute(sql)

        for row in self.cursor.fetchall():
            print(row)

    def get_all_endorsements(self):
        sql = "select * from Endorsements"
        self.cursor.execute(sql)
        
        for row in self.cursor.fetchall():
            print(row)

    def get_all_policies(self):
        sql = "select * from Policy"
        self.cursor.execute(sql)

        for row in self.cursor.fetchall():
            print(row)

    def get_all_sublimits(self):
        sql = "select * from Sublimits"
        self.cursor.execute(sql)

        for row in self.cursor.fetchall():
            print(row)

    def __run_sql(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()