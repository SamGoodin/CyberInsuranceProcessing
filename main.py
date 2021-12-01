from pdf_scraper import pdf_scraper
from db import database
from glob import glob

# Using Python 3.10, pdfplumber 0.5.28, pyodbc 4.0.32

class main:

    def __init__(self):
        # Initialize the database
        print(glob("database/*.accdb")[0])
        self.database = database(glob("database/*.accdb")[0])
        self.database.get_all_clients()
        # sublimit does not work
        self.database.add_sublimit(2, "Name", 12345.1, 12)
        # policy does not work
        #self.database.add_policy(2, 50, 100, 50, 25, 1000, 50, 2, 3, 4)
        # endorsement works
        #self.database.add_endorsement(20000, 2)
        # client does not work
        #self.database.add_client(2, "Sam", "Indy", "Software", "Film", 152.50, 27, 89)

        # Returns a list of all pdf files in current directory
        pdf_files = glob("pdf/*.pdf")
        print(pdf_files)

        # Pass the path to the pdf scraper
        # Assuming we want the first pdf file in the directory
        self.scraper = pdf_scraper(pdf_files[0], print=False)
        #data = self.scraper.extract_all_tables()
        



if __name__ == '__main__':
    app = main()