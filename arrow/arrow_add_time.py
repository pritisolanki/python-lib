import arrow

#exploring humanizing feature of arrow
print(f'Today is {arrow.now().format("dddd DD,MMM")} and time is {arrow.now().format("HH:mm")}')
event_date = arrow.now().shift(hours=2)
attend_date=event_date.shift(minutes=60)
print(f'Event will start in {event_date.humanize(arrow.now(), only_distance=True)}, Please reach venue in {event_date.humanize(attend_date, granularity=["hour"])}')

#arrow convert current time in different timezone
flight_schedule_date = arrow.now("America/New_York")
flight_landing_date = flight_schedule_date.shift(hours=28).to('+05:30')

print(f'flight scheduled departure is {flight_schedule_date.format("DD,MMM HH:mm A ZZZ")} and expected arrival at destination is {flight_landing_date.format("DD,MMM HH:mm A ZZZ")}')
