import os
import gspread


class Sheet:
    def __init__(
            self,
            sheet_tag: str = 'Contacts'
        ):
        self.gc = gspread.service_account(
            filename=os.getenv("GOOGLE_CREDENTIALS")
        )
        self.spreadsheet = self.gc.open_by_key(
            os.getenv("SPREADSHEET_ID")
        )
        self.worksheet = self.spreadsheet.worksheet(sheet_tag)

        self.headers = ['id', 'firstname', 'lastname', 'email', 'phone', 'mobilephone',
                        'company', 'jobtitle', 'website', 'country', 'lifecyclestage']
        self.worksheet.update(
            range_name="A1",
            values=[self.headers]
        )

    def append_row(self, row: list[str]):
        self.worksheet.append_row(row)

    def append_rows(self, rows: list[list[str]]):
        self.worksheet.append_rows(rows)

    def get_all_records(self):
        try:
            return self.worksheet.get_all_records()
        except Exception as e:
            print(e)


class DealSheet:
    def __init__(self, sheet_tag: str):
        self.gc = gspread.service_account(
            filename=os.getenv("GOOGLE_CREDENTIALS")
        )
        self.spreadsheet = self.gc.open_by_key(
            os.getenv("SPREADSHEET_ID")
        )
        self.worksheet = self.spreadsheet.worksheet(sheet_tag)
        
        self.headers = ['id', 'amount', 'closedate', 'createdate', 'dealname',
                        'dealstage', 'hs_lastmodifieddate', 'hs_object_id', 'pipeline', 'createdAt', 'updatedAt', 'archived', 'url']
        self.worksheet.update(
            range_name="A1",
            values=[self.headers]
        )

    def append_row(self, row: list[str]):
        self.worksheet.append_row(row)

    def append_rows(self, rows: list[list[str]]):
        self.worksheet.append_rows(rows)

    def get_all_records(self):
        try:
            return self.worksheet.get_all_records()
        except Exception as e:
            print(e)