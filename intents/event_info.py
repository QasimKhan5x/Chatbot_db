def get_event_datetime(name, organizer):
    if name == 'event':
        return f'SELECT MAX(datetime) FROM event WHERE organizerName = "{organizer}";'
    else:
        return f'SELECT dateTime FROM event WHERE eventName = "{name}" AND organizerName = "{organizer}";'

def get_event_description(name, organizer):
    return f'SELECT description FROM event WHERE eventName = "{name}" AND organizerName = "{organizer}";'

def get_event_organizer(name):
    return f'SELECT organizer FROM event WHERE eventName = "{name}";'