import sqlite3
from os.path import exists

class database:

    def __init__(self):
        # First, check if the db exists. If not, create it.
        self.path = 'database/Trava_DB.db'
        db_exists = exists("database/Trava_DB.db")
        if not db_exists:
            print("Database does not exist. Creating at {}".format(self.path))
            # Importing the script auto runs the code inside it
            from database import create_db
        else:
            print("Database already exists at {}".format(self.path))

        # Connect to the db
        self.__connect()

    def __connect(self):
        conn_string = self.path
        self.conn = sqlite3.connect(conn_string)
        self.cursor = self.conn.cursor()

    def add_client(self, ID, name, location, business_type, industry, revenue, employees, policyID):
        self.cursor.execute("""INSERT INTO Client 
        (Client_ID,Client_Name,Client_Location,Client_Type_of_Business,Client_Industry,Client_Annual_Revenue,Client_Num_of_Employees,Policy_ID) 
        VALUES 
        ({},'{}','{}','{}','{}',{},{},{});

        """.format(ID, name, location, business_type, industry, revenue, employees, policyID))
        self.conn.commit()

    def add_endorsement(self, ID, endorsement, start_date, end_date, policyid):
        self.cursor.execute("""INSERT INTO Endorsement 
        (Endorsement_ID,Endorsement_Premium,Endorsement_Effective_Start_Date,Endorsement_Effective_End_Date,Policy_ID) 
        VALUES 
        ({},{},'{}','{}',{});
        """.format(ID, endorsement, start_date, end_date, policyid))
        self.conn.commit()

    def add_policy(self, ID, policy_number, limit, premium, fees, deductible, se_limit, se_deductible, endorsementsID):
        self.cursor.execute("""INSERT INTO Policy 
        (Policy_ID,Policy_Number,Policy_Agg_Limit,Policy_Annual_Premium,Policy_Fees,Policy_Deductible,Policy_Social_Engineering_Limit,Policy_Social_Engineering_Deductible,Endorsement_ID) 
        VALUES 
        ({},'{}',{},{},{},{},{},{},{});
        """.format(ID, policy_number, limit, premium, fees, deductible, se_limit, se_deductible, endorsementsID))
        self.conn.commit()

    def add_sublimit(self, ID, name, coverage, policyID):
        self.cursor.execute("""INSERT INTO Sublimit 
        (Sublimit_ID,Sublimit_Name,Sublimit_Coverage,Policy_ID) 
        VALUES 
        ({},'{}',{},{});
        """.format(ID, name, coverage, policyID))
        self.conn.commit()

    def get_client(self, ID):
        self.cursor.execute("select * from Client where Client_ID={}".format(ID))
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def get_endorsement(self, ID):
        self.cursor.execute("select * from Endorsement where Endorsement_ID={}".format(ID))
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def get_policy(self, ID):
        self.cursor.execute("select * from Policy where Policy_ID={}".format(ID))
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def get_sublimit(self, ID):
        self.cursor.execute("select * from Sublimit where Sublimit_ID={}".format(ID))
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def get_all_clients(self):
        sql = "select * from Client"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def get_all_endorsements(self):
        sql = "select * from Endorsement"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def get_all_policies(self):
        sql = "select * from Policy"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def get_all_sublimits(self):
        sql = "select * from Sublimit"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        print(rows)
        return rows

    def __run_sql(self, sql):
        # Give the method an sql statement and it will run it
        # Be cautious with this
        self.cursor.execute(sql)
        self.conn.commit()