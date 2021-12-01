import pdfplumber


class pdf_scraper():

    def __init__(self, pdf_file, print=False):
        self.pdf_path = pdf_file
        self.print = print

    def extract_all_text(self):
        # Returns all text from pdf as a string
        data = None
        with pdfplumber.open(self.pdf_path) as pdf:
            for page_num, page in enumerate(pdf.pages):
                page_data = page.extract_text()
                data += page_data
                if print:
                    print("------- Page {}-----------".format((page_num + 1)))
                    print(page_data)
        pdf.close()
        return data

    def extract_all_tables(self):
        # Returns all data from pdf as a dictionary
        data = {}
        with pdfplumber.open(self.pdf_path) as pdf:
            # Loop through all the pages in the pdf
            for page_num, page in enumerate(pdf.pages):
                print("Scraping tables from page {} of {}".format(page_num + 1, self.pdf_path))
                # Extract all tables from the page
                page_data = page.extract_tables()

                # Data is in format of list, in a list
                # so we must iterate through
                for item in page_data:
                    for subitem in item:
                        # Raw data - formatting to give proper
                        # key value pairs in dictionary
                        formatted = subitem[0].strip()
                        while "\n" in formatted:
                            formatted = formatted.replace("\n", "")
                        split = formatted.split(":", 1)
                        # Ignoring cases we don't need
                        if len(split) == 2:
                            data[split[0]] = split[1]
        print("Finished scraping tables from all pages in {}\n".format(self.pdf_path))
        pdf.close()

        # Output the data if selected
        if self.print:
            for k,v in data.items():
                print(k, v)
        
        return data