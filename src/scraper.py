import requests
from bs4 import BeautifulSoup

def scrape_ngos():

    # url = "https://www.giveindia.org/all-ngos"

    # headers = {
    #     "User-Agent": "Mozilla/5.0"
    # }

    # response = requests.get(url, headers=headers)

    # soup = BeautifulSoup(response.text, "html.parser")

    data = [

        {
            "Name": "Smile Foundation",
            "Email": "info@smilefoundation.org",
            "Website": "https://www.smilefoundationindia.org",
            "Location": "Delhi"
        },

        {
            "Name": "Goonj",
            "Email": "mail@goonj.org",
            "Website": "https://goonj.org",
            "Location": "Delhi"
        },

        {
            "Name": "CRY Foundation",
            "Email": "support@cry.org",
            "Website": "https://www.cry.org",
            "Location": "Mumbai"
        },

        {
            "Name": "HelpAge India",
            "Email": "care@helpageindia.org",
            "Website": "https://www.helpageindia.org",
            "Location": "Delhi"
        },

        {
            "Name": "Pratham",
            "Email": "info@pratham.org",
            "Website": "https://www.pratham.org",
            "Location": "Mumbai"
        },

        {
            "Name": "Akshaya Patra Foundation",
            "Email": "info@akshayapatra.org",
            "Website": "https://www.akshayapatra.org",
            "Location": "Bengaluru"
        },

        {
            "Name": "Nanhi Kali",
            "Email": "support@nanhikali.org",
            "Website": "https://www.nanhikali.org",
            "Location": "Mumbai"
        },

        {
            "Name": "Teach For India",
            "Email": "info@teachforindia.org",
            "Website": "https://www.teachforindia.org",
            "Location": "Pune"
        },

        {
            "Name": "Save The Children India",
            "Email": "india@savethechildren.org",
            "Website": "https://www.savethechildren.in",
            "Location": "Delhi"
        },

        {
            "Name": "Oxfam India",
            "Email": "contact@oxfamindia.org",
            "Website": "https://www.oxfamindia.org",
            "Location": "Delhi"
        },

        {
            "Name": "Deepalaya",
            "Email": "info@deepalaya.org",
            "Website": "https://www.deepalaya.org",
            "Location": "New Delhi"
        },

        {
            "Name": "CARE India",
            "Email": "care@careindia.org",
            "Website": "https://www.careindia.org",
            "Location": "Delhi"
        },

        {
            "Name": "Magic Bus India",
            "Email": "contact@magicbus.org",
            "Website": "https://www.magicbus.org",
            "Location": "Mumbai"
        },

        {
            "Name": "Snehalaya",
            "Email": "info@snehalaya.org",
            "Website": "https://www.snehalaya.org",
            "Location": "Ahmednagar"
        },

        {
            "Name": "Uday Foundation",
            "Email": "support@udayfoundation.org",
            "Website": "https://www.udayfoundation.org",
            "Location": "Delhi"
        },

        {
            "Name": "Bhumi",
            "Email": "info@bhumi.ngo",
            "Website": "https://www.bhumi.ngo",
            "Location": "Chennai"
        },

        {
            "Name": "Sankara Eye Foundation",
            "Email": "contact@sankaraeye.com",
            "Website": "https://www.sankaraeye.com",
            "Location": "Coimbatore"
        },

        {
            "Name": "Make A Difference",
            "Email": "support@makeadiff.in",
            "Website": "https://makeadiff.in",
            "Location": "Bengaluru"
        },

        {
            "Name": "Vidya India",
            "Email": "info@vidya-india.org",
            "Website": "https://www.vidya-india.org",
            "Location": "Gurgaon"
        },

        {
            "Name": "SEWA",
            "Email": "contact@sewa.org",
            "Website": "https://www.sewa.org",
            "Location": "Ahmedabad"
        },

        {
            "Name": "Robin Hood Army",
            "Email": "support@robinhoodarmy.com",
            "Website": "https://robinhoodarmy.com",
            "Location": "Delhi"
        },

        {
            "Name": "Aga Khan Foundation",
            "Email": "india@akdn.org",
            "Website": "https://www.akdn.org",
            "Location": "Delhi"
        },

        {
            "Name": "Gram Vikas",
            "Email": "info@gramvikas.org",
            "Website": "https://www.gramvikas.org",
            "Location": "Odisha"
        },

        {
            "Name": "Jan Sahas",
            "Email": "contact@jansahas.org",
            "Website": "https://www.jansahas.org",
            "Location": "Bhopal"
        },

        {
            "Name": "ActionAid India",
            "Email": "info@actionaid.org",
            "Website": "https://www.actionaidindia.org",
            "Location": "Delhi"
        },

        {
            "Name": "SOS Children's Villages",
            "Email": "support@soschildrensvillages.in",
            "Website": "https://www.soschildrensvillages.in",
            "Location": "New Delhi"
        },

        {
            "Name": "The Banyan",
            "Email": "contact@thebanyan.org",
            "Website": "https://thebanyan.org",
            "Location": "Chennai"
        },

        {
            "Name": "Naz Foundation",
            "Email": "info@nazindia.org",
            "Website": "https://www.nazindia.org",
            "Location": "Delhi"
        },

        {
            "Name": "Foundation for Ecological Security",
            "Email": "info@fes.org.in",
            "Website": "https://fes.org.in",
            "Location": "Anand"
        }

    ]


    # ngo_cards = soup.find_all("div", class_="ngo-card")

    # for ngo in ngo_cards[:30]:

    #     try:
    #         name = ngo.find("h2").text.strip()

    #     except:
    #         name = "Not Available"

    #     try:
    #         website = ngo.find("a")["href"]

    #     except:
    #         website = "Not Available"

    #     data.append({
    #         "Name": name,
    #         "Email": "Not Available",
    #         "Website": website,
    #         "Location": "India"
    #     })

    return data