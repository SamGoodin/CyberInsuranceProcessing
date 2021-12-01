from pdf_scraper import pdf_scraper
from db import database
from glob import glob

# Using Python 3.10, pdfplumber 0.5.28, SQLite3

class main:

    def __init__(self):
        #------------------Initialize the database----------------------------------
        self.database = database()

        #self.database.add_client(2, "Sam", "Indy", "Software", "Music", 1000.00, 27, 1)
        #self.database.get_all_clients()

        #self.database.add_sublimit(2, "Name", 12345.1, 12)
        #self.database.get_all_sublimits()

        #self.database.add_policy(2, 50, 100, 50, 25, 1000, 50, 2)
        #self.database.get_all_policies()

        #self.database.add_endorsement(50, 20000, '1-1-2021', '12-31-2022', 12)
        #self.database.get_all_endorsements()

        #----------------------------------------------------------------------------

        # Returns a list of all pdf files in current directory
        pdf_files = glob("pdf/*.pdf")

        # Pass the path to the pdf scraper
        # Assuming we want the first pdf file in the directory
        self.scraper = pdf_scraper(pdf_files[0], print=False)
        #data = self.scraper.extract_all_tables()
        



if __name__ == '__main__':
    app = main()