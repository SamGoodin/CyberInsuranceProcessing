import sys
import pdfplumber

class main():
    
    def __init__(self):
        print("Hello world")
        
    def scrape_pdf(self, pdf_link, encoding='utf-8', page_num=None):
        # pdf_link is location of pdf
        # encoding is default utf-8, can be changed but best results with utf-8
        # page_num is if you want a specific page, else the entire pdf is returned
        pdf = pdfplumber.open(pdf_link)
        if page_num:
            try:
                return pdf.pages[page_num].extract_text().encode(encoding)
            except Exception as e:
                print(e)
        else:
            pdf_text = None
            for page in pdf.pages:
                try:
                    pdf_text += page.extract_text().encode(encoding)
                except Exception as e:
                    print(e)
            return pdf_text


if __name__ == '__main__':
    main()