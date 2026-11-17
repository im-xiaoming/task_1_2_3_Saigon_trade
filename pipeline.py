from __future__ import annotations

import os
import requests
from dotenv import load_dotenv

from hubspot import HubSpot
from sheets import Sheet

load_dotenv()


def load_data(path: str):
    import pandas as pd

    df = pd.read_csv(path)

    data = []
    for _, row in df.iterrows():
        data.append(row.to_dict())

    return data

if __name__ == '__main__':
    path = './data/contacts_data.csv'
    data = load_data(path)

    fields = list(data[0].keys())
    hubspot = HubSpot(
        fiels=fields,
        api_key=os.getenv("HUBSPOT_TOKEN")
    )
    sheet = Sheet(sheet_tag='Contacts')

    # uncomment the following lines to create contacts in HubSpot from the CSV data
    # for contact in data:
    #     hubspot.create_contact(contact)
    #     print(f"Created {contact['email']}")


    # uncomment the following lines to fetch contacts from HubSpot and print them
    # contacts = hubspot.get_contacts(limit=100)
    # for contact in contacts:
    #     print(contact)

    # uncomment the following lines to fetch contacts from HubSpot and append them to a Google Sheet
    # sheet.append_rows([list(contact.values()) for contact in contacts])

    # uncomment the following lines to fetch all records from the Google Sheet and print them
    # sheet_data = sheet.get_all_records()
    # for row in sheet_data:
    #     print(row)