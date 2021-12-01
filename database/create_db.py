import sqlite3
from os.path import exists

# Run this script to generate the database

# Guard against overwriting db if it exists
if not exists("Trava_DB.db"):
    conn = sqlite3.connect('database/Trava_DB.db')

    c = conn.cursor()

    #Generates Client Table
    c.execute("""CREATE TABLE Client (
                Client_ID INTEGER,
                Client_Name TEXT,
                Client_Location TEXT,
                Client_Type_of_Business TEXT,
                Client_Industry TEXT,
                Client_Annual_Revenue FLOAT,
                Client_Num_of_Employees INTEGER,
                Policy_ID INTEGER
                )""")

    #Generates Policy Table
    c.execute("""CREATE TABLE Policy(
                Policy_ID INTEGER,
                Policy_Number TEXT,
                Policy_Agg_Limit INTEGER,
                Policy_Annual_Premium INTEGER,
                Policy_Fees TEXT,
                Policy_Deductible INTEGER,
                Policy_Social_Engineering_Limit INTEGER,
                Policy_Social_Engineering_Deductible INTEGER,
                Endorsement_ID INTEGER
                )""")

    #Generates Sublimit Table
    c.execute("""CREATE TABLE Sublimit(
                Sublimit_ID INTEGER,
                Sublimit_Name TEXT,
                Policy_ID INTEGER
                )""")

    #Generates Endorsement Table
    c.execute("""CREATE TABLE Endorsement (
                Endorsement_ID INTEGER,
                Endorsement_Premium INTEGER,
                Endorsement_Effective_Start_Date TEXT,
                Endorsement_Effective_End_Date TEXT,
                Policy_ID INTEGER
                )""")
                
    conn.commit()
    conn.close()

else:
    print("The database already exists. I don't think you intended to run this file.")