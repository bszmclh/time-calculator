import re
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def add_time(start, duration, day = None):
    [startTime, ampm] = start.split()
    [startH, startM] = startTime.split(":")
    [durationH, durationM] = duration.split(":")

    ampmCount = 0
    dayPassed = 0
    hourUp = False
    
    endM = int(startM) + int(durationM)
    if endM >= 60:
        hourUp = True
        endM -= 60
    
    if endM < 10:
        endM = "0" + str(endM)
    else:
        endM = str(endM)

    endH = int(startH) + int(durationH)
    if hourUp: endH +=1

    ampmCount = int(endH/12)
    endH = str(endH%12)
    if endH =="0": endH = "12"

    if ampmCount %2 ==1:
        if ampm == 'AM': 
            ampm = 'PM'
        else: 
            ampm = 'AM'
            dayPassed +=1
    
    dayPassed += int(ampmCount /2)
    
    result = []
    result.append(endH + ":" + endM +" "+ampm)

    if dayPassed > 0:
        if dayPassed == 1: 
            result.append(' (next day)')
        else: 
            result.append(" (" + str(dayPassed) + " days later)")
    
    if day:
        for weekday in weekdays:
            if re.search(day, weekday, re.IGNORECASE):
                nextDayIndex = (weekdays.index(weekday) + dayPassed) % 7
                result.insert(1, ", " +weekdays[nextDayIndex])
                break

    return "".join(result)


print(add_time("11:55 AM", "3:12"))