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

    def add_client(self, ID, name, location, business_type, industry, revenue, employees, policyID):
        info = "({},{},{},{},{},{},{},{})".format(ID, name, location, business_type, industry, revenue, employees, policyID)
        sql = "insert into Client (ID,Client_Name,Client_Location,Client_Type_of_Business,Client_Industry,Client_Annual_Revenue,Client_Num_of_Employees,Policy_ID) values " + info + ";"
        print(sql)
        self.cursor.execute(sql)

    def add_endorsement(self, ID, endorsement, date, policyid):
        info = "({},{},{},{})".format(ID, endorsement, date, policyid)
        sql = "insert into Endorsements (ID,Endorsement_Premium,Endorsement_Effective_Date,Policy_ID) values " + info + ";"
        self.cursor.execute(sql)
        self.conn.commit()

    def add_policy(self, ID, limit, premium, fees, deductible, se_limit, se_deductible, endorsementsID, sublimitsID, clientID):
        info = "({},{},{},{},{},{},{},{},{},{})".format(ID, limit, premium, fees, deductible, se_limit, se_deductible, endorsementsID, sublimitsID, clientID)
        sql = "insert into Policy (ID,Policy_Agg_Limit,Policy_Annual_Premium,Policy_Fees,Policy_Deductible,Policy_Social_Engineering_Limit,Policy_Social_Engineering_Deductible,Endorsements_ID,Sublimits_ID,Client_ID) values " + info + ";"
        self.cursor.execute(sql)
        self.conn.commit()

    def add_sublimit(self, ID, name, coverage, policyID):
        info = "({},{},{},{})".format(2, 'Name', '20000.00', 2)
        sql = "insert into Sublimits (ID,Sublimit_Name,Sublimit_Coverage,Policy_ID) values " + info + ";"
        self.cursor.execute(sql)
        self.conn.commit()

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