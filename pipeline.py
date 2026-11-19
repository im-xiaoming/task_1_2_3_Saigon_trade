from __future__ import annotations

import os
import requests
import logging
from dotenv import load_dotenv

from hubspot import HubSpot
from hub_types import Contact
from sheets import Sheet
from helper import load_data, to_dict
import argparse

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s %(filename)s - %(message)s'
)

logger = logging.getLogger(__name__)


def post_to_hub(contacts: list[dict], hubspot: HubSpot):
    for contact in contacts:
        c = Contact(**contact).model_dump()
        try:
            e_response = hubspot.get_contact_by_email(email=c['email'])
            p_response = hubspot.get_contact_by_phone(phone=c['phone'])

            if e_response.ok:
                response = hubspot.update_contact(e_response.json()['id'], c)
                logger.info(f"Update contact {e_response.json()['id']}")
            elif p_response.ok:
                response = hubspot.update_contact(p_response.json()['id'], c)
                logger.info(f"Update contact {p_response.json()['id']}")
            else:
                response = hubspot.create_contact(c)
                logger.info(f"Create contact {response.json()['id']}")

        except Exception as e:
            logger.exception(str(e))


def post_to_sheet(contacts: list[dict], sheet: Sheet, tag: str):
    results = []
    for contact in contacts:
        r = to_dict(contact)
        c = Contact(**r)
        results.append(list(c.model_dump().values()))
    sheet.append_rows(results)


def main():
    parser = argparse.ArgumentParser(description="HubSpot Contact Management")
    parser.add_argument('--csv', type=str, default='./data/contacts_data.csv', help='Path to the CSV file containing contact data')

    args = parser.parse_args()

    contacts: list[dict] = load_data(args.csv)
    hubspot = HubSpot(
        api_key=os.getenv('HUBSPOT_TOKEN')
    )
    sheet = Sheet(sheet_tag='Contacts')

    ########################################
    post_to_hub(contacts, hubspot)

    # response = hubspot.get_all_contacts()
    # contacts = response.json()['results']
    # post_to_sheet(contacts, sheet, tag='Contact')


    # contacts = sheet.get_all_records()
    # post_to_hub(contacts, hubspot)



if __name__ == '__main__':
    main()