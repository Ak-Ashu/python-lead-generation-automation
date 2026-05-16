from scraper import scrape_ngos
from cleaner import clean_data
from exporter import export_to_excel

def main():

    raw_data = scrape_ngos()

    cleaned_data = clean_data(raw_data)

    export_to_excel(cleaned_data)

if __name__ == "__main__":
    main()