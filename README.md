# HubSpot → Google Sheets

Syncs contacts from a CSV into HubSpot, then exports all HubSpot contacts to a Google Sheet.

## Setup

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Fill in `.env`:

- `HUBSPOT_TOKEN`: HubSpot private app token
- `GOOGLE_CREDENTIALS`: path to the service account JSON (e.g. `credentials/service-account.json`)
- `SPREADSHEET_ID`: target Google Sheet ID (share the sheet with the service account email)
- `WORKSHEET_NAME`: worksheet tab name

## Run

```bash
python pipeline.py --csv ./data/contacts_data.csv
```
