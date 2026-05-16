import os

def export_to_excel(df):

    os.makedirs("data", exist_ok=True)

    file_path = "data/leads.xlsx"

    df.to_excel(file_path, index=False)

    print(f"Excel file saved successfully at {file_path}")