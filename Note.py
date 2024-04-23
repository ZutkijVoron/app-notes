import datetime


class Note:

    def __init__(self, title, message, date=None):
        self.title = title
        self.message = message
        self.date = date if date is not None else datetime.datetime.now()

    def __str__(self):
        return f"{self.title}\t\t{self.message}\t\t{self.date}"

    def __getattribute__(self, name):
        return super().__getattribute__(name)

    def __lt__(self, other):
        return self.date < other.date
