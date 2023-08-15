# utils.py

def generate_time_choices():
    times = []
    for hour in range(24):  # 24 hours in a day
        for minute in [0, 30]:  # Only 00 and 30 minutes
            time_string = "{:02d}:{:02d}".format(hour, minute)
            times.append((time_string, time_string))
    return times
