def add_time(start, duration, start_day = 'monday'):

# Calculate the resulting day of the week (using a fixed list)
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

# Find the index of the starting day (handling case insensitivity)
    start_day_lower = start_day.lower()
    start_day_index = (weekdays.index(start_day_lower) if start_day_lower in weekdays else 0) % 7  

# Split the time for easy calculation
    hours_minutes, am_pm = start.split()
    hours, minutes = map(int, hours_minutes.split(':'))
    hours2, minutes2 = map(int, duration.split(':'))

# Convert start time to minutes (considering PM)
    start_time = (hours * 60) + minutes
    if am_pm.lower() == 'pm':
        start_time += 12 * 60  # Add 12 hours only if it's PM

    total_duration = ((hours2 * 60) + minutes2)
    end_time = start_time + total_duration

#calculate the number of days that have passed
    days_passed = end_time //1440

# Handle cross midnighting
    if end_time >= 1440:
        end_time %= 1440

    total_hours = (end_time // 60)
    final_minutes = (end_time % 60)

# Determine AM or PM for the new time
    period = 'PM' if total_hours >= 12 else 'AM'
    final_hours = (total_hours % 12) or 12  # Use 12 for midnight in AM format

# Format minutes with leading zeros
    formatted_minutes = f'{final_minutes:02}'

    output = f'{final_hours}:{formatted_minutes} {period}'

    #Calculate the resulting day of the week
    start_day_lower = start_day.lower()

    #Find index of starting day
    start_day_index = weekdays.index(start_day_lower)

    #Calculate the index of the resulting day (considering day crossing)
    result_day_index = (start_day_index + days_passed) % 7

    result_day = weekdays[result_day_index]

    #Determine if a starting day argument is provided
    provided_day = start_day != 'monday'

    
#add logic for handling day crossing
    if days_passed > 0:
        if provided_day: 
            if days_passed >1:
                new_time =  f'{output}, {result_day.capitalize()} ({days_passed} days later)'
            else:
                new_time =  f'{output}, {result_day.capitalize()} (next day)'
        else:
            if days_passed >1:
                new_time =  f'{output} ({days_passed} days later)'
            else:
                new_time = f'{output} (next day)'#No day information if default start _day used
    else:
        if provided_day:
            new_time = f'{output}, {result_day.capitalize()}'
        else: 
            new_time = f'{output}'

    return new_time

#Testing values 
print(add_time('3:30 PM', '2:12', 'Monday'))

print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)