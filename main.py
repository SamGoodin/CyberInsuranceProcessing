from pdf_scraper import pdf_scraper
from db import database
from glob import glob

# Using Python 3.10, pdfplumber 0.5.28, SQLite3

class main:

    def __init__(self):
        #------------------Initialize the database----------------------------------
        self.database = database()


        self.database.add_client(2, "Sam", "Indy", "Software", "Music", 1000.00, 27, 1)
        #self.database.get_all_clients()

        self.database.add_sublimit(2, "Name", 12)
        #self.database.get_all_sublimits()

        self.database.add_policy(2, 'Example', 50, 100, 50, 25, 1000, 50, 2)
        #self.database.get_all_policies()

        self.database.add_endorsement(50, 20000, '1-1-2021', '12-31-2022', 12)
        #self.database.get_all_endorsements()

        #----------------------------------------------------------------------------

        # Returns a list of all pdf files in current directory
        pdf_files = glob("pdf/*.pdf")

        # Pass the path to the pdf scraper
        # Assuming we want the first pdf file in the directory
        self.scraper = pdf_scraper(pdf_files[0], print=False)
        data = self.scraper.extract_all_tables()

        # Output key value pair
        for k,v in data.items():
            print(k, v)

        # Get all the pieces of data we need from data and format accordingly
        clientname = data['Company Name'].split("company")[0].replace("  ", "") + "company"
        clientloc = data['Company Name'].split("company")[1].replace(" ", "", 1)
        policy_id = 100
        policynumber = data['Policy Number'].replace(" ", "")
        agglimit = data['Policy Aggregate Limit of Insurance'].replace("  $", "")
        if "," in agglimit:
            agglimit = agglimit.replace(",", "")
        premium = data['Annual Premium'].replace("  $", "")
        if "," in premium:
            premium = premium.replace(",", "")
        fees = data['Fees/Assessment'].replace(" $", "")
        deductible = data['Policy Deductible Amount'].replace("  $", "")
        if "," in deductible:
            deductible = deductible.replace(",", "")
        selimit = data['Social Engineering Coverage Limit'].replace("  $", "")
        if "," in selimit:
            selimit = selimit.replace(",", "")
        sedeductible = data['Social Engineering Deductible'].replace("  $", "")
        if "," in sedeductible:
            sedeductible = sedeductible.replace(",", "")
        endorsementid = 100
        sublimitname = data['CoverageAggregate Sublimit(s) of Insurance']
        sublimitname = sublimitname.replace(" Percentage LimitDollarsInsuring Agreement ", "")

        # Add scraped PDF data to database
        self.database.add_client(10, clientname, clientloc, "", "", -1, -1, policy_id)
        self.database.add_policy(policy_id, policynumber, agglimit, premium, fees, deductible, selimit, sedeductible, endorsementid)
        self.database.add_sublimit(10, sublimitname, policy_id)
        
        """
        Client:
            Client_Name=Company_Name
            Client_Location=Company_Name after 'company'
            Client_Type_of_Business=?
            Client_Industry=?
            Client_Annual_Revenue=?
            Client_Num_of_Employees=?
            Policy_ID=Get from policy table based on Policy_Number

        Policy:
            Policy_Number=Policy Number
            Policy_Agg_Limit=Policy Aggregate Limit of Insurance
            Policy_Annual_Premium=Annual Premium
            Policy_Fees=Fees/Assessment
            Policy_Deductible=Policy Deductible Amount
            Policy_SE_Limit=Social Engineering Coverage Limit
            Polocy_SE_Deductible=Social Engineering Deductible
            Endorsement_ID=Get from endorsement table based on ?
        
        Sublimit:
            Sublimit_Name=String of CoverageAggregate Sublimit(s) of Insurance
            Policy_ID=Get from policy

        Endorsement:
        Faulty pdf so can't extract endorsements
            Endorsement_Premium=?
            Endorsement_Effective_Start_Date=?
            Endorsement_Effective_End_Date=?
            Policy_ID=Get from policy
        """
        



if __name__ == '__main__':
    app = main()