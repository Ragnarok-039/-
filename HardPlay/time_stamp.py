# Функция для определения времени в формате ISO8601 в формате: yyyy-MM-dd'T'hh:mm:ss.SSSZ.
# Используется время по часовому поясу GMT+3 (МСК).


def time_stamp():
    from datetime import datetime, timezone, timedelta

    offset = timedelta(hours=3)
    tz = timezone(offset, name='МСК')
    time_request = datetime.now(tz).isoformat()

    return time_request
