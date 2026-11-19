from __future__ import annotations

import requests

import logging

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

    def create(self):
        endpoint = 'https://api.hubapi.com/crm/v3/objects/0-3'

if __name__ == '__main__':
    dealer = Deal()

    res = dealer.list_deals()
    print(res.json())


# {'results': [{'id': '372471867097', 'properties': {'amount': '25000', 'closedate': None, 'createdate': '2026-11-19T08:51:58.455Z', 'dealname': 'PC', 'dealstage': 'appointmentscheduled', 'hs_lastmodifieddate': '2026-11-19T08:51:59.068Z', 'hs_object_id': '372471867097', 'pipeline': 'default'}, 'createdAt': '2026-11-19T08:51:58.455Z', 'updatedAt': '2026-11-19T08:51:59.068Z', 'archived': False, 'url': 'https://app-na2.hubspot.com/contacts/248029724/record/0-3/372471867097'}]}