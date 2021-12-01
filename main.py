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
        self.database.add_client("Sam", "Indy", "Software", "Film", 152.50, 27)

        # Returns a list of all pdf files in current directory
        pdf_files = glob("pdf/*.pdf")
        print(pdf_files)

        # Pass the path to the pdf scraper
        # Assuming we want the first pdf file in the directory
        self.scraper = pdf_scraper(pdf_files[0], print=False)
        #data = self.scraper.extract_all_tables()
        



if __name__ == '__main__':
    app = main()