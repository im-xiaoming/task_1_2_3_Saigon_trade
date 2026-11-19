from __future__ import annotations

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class Contact(BaseModel):
    model_config = ConfigDict(extra='ignore')
    
    id: int
    firstname: str
    lastname: str
    email: str
    phone: str
    mobilephone: str
    company: str
    jobtitle: str
    website: str
    country: str
    lifecyclestage: str


class DealData(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: int
    amount: int
    dealname: str
    pipeline: str
    dealstage: str
    owner: str
    create_date: str
    closedate: datetime
    hs_lastmodifieddate: datetime



# {'results': [{'id': '372471867097', 'properties': {'amount': '25000', 'closedate': None, 'createdate': '2026-11-19T08:51:58.455Z', 'dealname': 'PC', 'dealstage': 'appointmentscheduled', 'hs_lastmodifieddate': '2026-11-19T08:51:59.068Z', 'hs_object_id': '372471867097', 'pipeline': 'default'}, 'createdAt': '2026-11-19T08:51:58.455Z', 'updatedAt': '2026-11-19T08:51:59.068Z', 'archived': False, 'url': 'https://app-na2.hubspot.com/contacts/248029724/record/0-3/372471867097'}]}