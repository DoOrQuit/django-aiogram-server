from google.oauth2 import service_account
from googleapiclient.discovery import build


# Google Calendar
class GoogleCalendar:

    SCOPES = ['https://www.googleapis.com/auth/calendar']
    # Path to service_account.json file
    FILE_PATH = 'core/service_account.json'

    def __init__(self, calendar_id):
        self.credentials = service_account.Credentials.from_service_account_file(
                    filename=self.FILE_PATH,
                    scopes=self.SCOPES
                )
        self.calendar_id = calendar_id
        self.service = build("calendar", "v3", credentials=self.credentials)

    def events_list_simplified(self):
        """ Returns a list of dicts which contains all events in format {date: 2023-06-04, time:[14:00, 17:00]} """

        events = []

        # Retrieves a raw data from API
        raw_events_data = self.service.events().list(calendarId=self.calendar_id).execute()['items']

        for event in raw_events_data:
            events.append(event['start']['dateTime'])

        grouped_events = {}

        for event in events:
            date, time = event.split('T')
            if date not in grouped_events:
                grouped_events[date] = []
            grouped_events[date].append(time[:5])

        for times in grouped_events.values():
            times.sort()

        result = [{"date": date, "time": times} for date, times in grouped_events.items()]

        return result

