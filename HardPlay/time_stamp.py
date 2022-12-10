def time_stamp():
    from datetime import datetime, timezone, timedelta

    offset = timedelta(hours=3)
    tz = timezone(offset, name='МСК')
    time_request = datetime.now(tz).isoformat()

    return time_request
