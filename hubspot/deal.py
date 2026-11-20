from __future__ import annotations

import requests

import logging
from hub_types import DealData

logger = logging.getLogger(__name__)

class Deal:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def list_deals(self) -> requests.Response:
        endpoint = 'https://api.hubapi.com/crm/v3/objects/0-3'
        response = requests.get(
            url=endpoint,
            headers=self.headers
        )
        if not response.ok:
            logger.error("list deal failed.")
        return response

    def get_valid_owner_ids(self) -> requests.Response:
        endpoint = 'https://api.hubapi.com/crm/v3/owners/'
        response = requests.get(
            url=endpoint,
            headers=self.headers
        )
        return response

    def create(self, deal: dict):
        endpoint = 'https://api.hubapi.com/crm/v3/objects/0-3'
        deal = DealData(**deal).model_dump(mode='json')
        if 'id' in deal:
            del deal['id']
        payload = {
            'properties': {
                **deal
            }
        }
        response = requests.post(
            url=endpoint,
            json=payload,
            headers=self.headers
        )

        if not response.ok:
            logger.error("Cannot create deal.")
        return response

    def get_deal_by_id(self, id: str) -> requests.Response:
        endpoint = f'https://api.hubapi.com/crm/v3/objects/0-3/{id}'
        response = requests.get(
            url=endpoint,
            headers=self.headers
        )
        if not response.ok:
            logger.error(f"Cannot fetch deal ID {id} - staus: {response.status_code}")
        return response

    def update(self, id: str, deal: dict) -> requests.Response:
        endpoint = f'https://api.hubapi.com/crm/v3/objects/0-3/{id}'
        if 'hubspot_owner_id' in deal:
            del deal['hubspot_owner_id']
        payload = {
            'properties': {
                **deal
            }
        }
        response = requests.patch(
            url=endpoint,
            headers=self.headers,
            json=payload
        )
        if not response.ok:
            logger.error(f"Cannot create deal ID {id}.")

        return response