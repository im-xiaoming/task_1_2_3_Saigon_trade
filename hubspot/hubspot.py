from __future__ import annotations

import requests
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class HubSpot:
    def __init__(
            self,
            *,
            api_key: str
        ):
        assert api_key, "API key cannot be empty"

        self.api_key = api_key

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def update_contact(self, id: str, contact: dict) -> requests.Response:
        endpoint = f'https://api.hubapi.com/crm/v3/objects/contacts/{id}'
        payload = {
            'properties': {
                **contact
            }
        }
        if payload['properties'].get('id', None):
            del payload['properties']['id']
        response = requests.patch(
            url=endpoint,
            headers=self.headers,
            json=payload
        )
        if not response.ok:
            logger.error(f"HubSpot error {response.status_code}: {response.json()}")

        return response


    def get_contact_by_email(self, email: str) -> requests.Response:
        endpoint = f'https://api.hubapi.com/crm/v3/objects/contacts/{email}'
        response = requests.get(
            url=endpoint,
            headers=self.headers,
            params={'idProperty': 'email'},
            timeout=300
        )
        if not response.ok:
            logger.error(f"Fetch email {email} error {response.status_code}")

        return response


    def create_contact(self, contact: dict) -> requests.Response:
        endpoint = 'https://api.hubapi.com/crm/v3/objects/contacts'

        payload = {
            'id': str(contact['id']),
            "properties": {
                **contact
            }
        }
        if payload['properties'].get('id', None):
            del payload['properties']['id']
        response = requests.post(
            endpoint,
            headers=self.headers,
            json=payload,
            timeout=300
        )
        if not response.ok:
            logger.error(f"HubSpot error {response.status_code}: {response.json()}")

        return response


    def get_all_contacts(self):
        endpoint = 'https://api.hubapi.com/crm/v3/objects/contacts'
        response = requests.get(
            url=endpoint,
            headers=self.headers
        )
        if not response.ok:
            logger.error(f"HubSpot error {response.status_code}: {response.json()}")
            
        return response