from __future__ import annotations

import requests

class HubSpot:
    def __init__(
            self,
            *,
            fiels: list[str],
            api_key: str,
            endpoint: str = 'https://api.hubapi.com/crm/v3/objects/contacts',
        ):
        assert fiels, "Fields list cannot be empty"
        assert api_key, "API key cannot be empty"
        assert endpoint, "Endpoint cannot be empty"

        self.fields = fiels
        self.api_key = api_key
        self.endpoint = endpoint

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def get_contacts(self, limit: int = 100) -> list[dict]:
        params = {
            "limit": limit,
            "properties": [
                *self.fields
            ],
        }

        response = requests.get(
            self.endpoint,
            headers=self.headers,
            params=params,
            timeout=300
        )
        response.raise_for_status()
        results = response.json()['results']
        contacts = [
            {
                'id': r['id'],
                **{field: r['properties'].get(field) for field in self.fields}
            }
            for r in results
        ]
        return contacts

    def create_contact(self, contact_data: list[dict]) -> dict:
        payload = {
            "properties": {
                **contact_data
            }
        }
        response = requests.post(
            self.endpoint,
            headers=self.headers,
            json=payload,
            timeout=300
        )
        if not response.ok and response.status_code != 409:
            print(f"HubSpot error {response.status_code}: {response.text}")
        response.raise_for_status()
        return response.json()