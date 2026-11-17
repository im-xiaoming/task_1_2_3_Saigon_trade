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
        self.worksheet = self.spreadsheet.worksheet(
            os.getenv("WORKSHEET_NAME", sheet_tag)
        )

    def append_row(self, row: list[str]):
        self.worksheet.append_row(row)

    def append_rows(self, rows: list[list[str]]):
        self.worksheet.append_rows(rows)

    def get_all_records(self):
        return self.worksheet.get_all_records()