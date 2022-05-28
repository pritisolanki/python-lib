import arrow

#print arrow installed version - By Priti
print(arrow.__version__ )

#format current date with timezone and AM/PM 
print(f'current time in PST: { arrow.now("US/Pacific").format("MMMM DD, YYYY HH:mm A")}');
print(f'current time in EST: { arrow.now("America/New_York").format("MMMM DD, YYYY HH:mm A")}');

todaydate=arrow.now("America/New_York")
print(f'Today is { todaydate.format("dddd MMMM Do")} and time is {todaydate.format("HH:mm A")}');
print(f'my current timezone is : {arrow.now().format("ZZZ")}')