import json
from datetime import date, datetime, timedelta


def reformat_date(date, format):
    return date.strftime(format)