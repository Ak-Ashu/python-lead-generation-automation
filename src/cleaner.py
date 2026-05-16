import pandas as pd
import re

def clean_data(data):

    if not data:
        print("No data scraped.")
        return pd.DataFrame()

    df = pd.DataFrame(data)

    if "Name" not in df.columns:
        print("Name column missing.")
        return df

    df.drop_duplicates(inplace=True)

    df.fillna("Not Available", inplace=True)

    def generate_email(name):

        clean_name = re.sub(r'[^a-zA-Z ]', '', str(name))

        clean_name = clean_name.lower().replace(" ", "")

        return f"contact@{clean_name}.org"

    df["Generated_Email"] = df["Name"].apply(generate_email)

    return df