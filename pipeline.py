from __future__ import annotations

import os
import requests
import logging
from dotenv import load_dotenv

from hubspot import HubSpot
from sheets import Sheet
from helper import load_data, to_dict
import argparse

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="HubSpot Contact Management")
    parser.add_argument('--csv', type=str, default='./data/contacts_data.csv', help='Path to the CSV file containing contact data')

    args = parser.parse_args()

    contacts: list[dict] = load_data(args.csv)
    hubspot = HubSpot(
        api_key=os.getenv('HUBSPOT_TOKEN')
    )

    # =================== create/update/remove duplicate contacts =============================
    # for contact in contacts:
    #     response = hubspot.get_contact_by_email(email=contact['email'])
    #     if response.ok:
    #         hubspot.update_contact(response.json()['id'], contact)
    #     else:
    #         response = hubspot.create_contact(contact)

    # ================ to sheet ===================================
    response = hubspot.get_all_contacts()
    contacts = response.json()['results']


    sheet = Sheet(sheet_tag='Contacts')
    results = []
    for contact in contacts:
        r = {}
        to_dict(contacts[0], r)
        results.append(list(r.values()))
    sheet.append_rows(results)



if __name__ == '__main__':
    main()