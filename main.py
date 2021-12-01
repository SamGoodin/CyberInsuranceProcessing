from pdf_scraper import pdf_scraper
import glob

# Using Python 3.10, pdfplumber 0.5.28

class main():

    def __init__(self):   
        # Returns a list of all pdf files in current directory
        pdf_files = glob.glob("*.pdf")

        # Pass the path to the pdf scraper
        # Assuming we want the first pdf file in the directory
        scraper = pdf_scraper(pdf_files[0], True)
        scraper.extract_all_tables()
        



if __name__ == '__main__':
    app = main()