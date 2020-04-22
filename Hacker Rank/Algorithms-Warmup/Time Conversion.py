def timeConversion(s):
    """Given a time in 12-hour AM/PM format, convert it to military (24-hour) time."""
    time = s.split(':')  # split the time by the :
    if s[-2:] == 'PM':  # check last two items (AM/PM) in array
        if time[0] != '12':  # if the hour is not equal to 12
            # the hour is equal the hour plus 12 (string inside of integer)
            time[0] = str(int(time[0])+12)
    else:
        if time[0] == '12':  # if the hour is equal to 12
            time[0] = '00'  # the hour is equal to 00
    ntime = ':'.join(time)  # join the split array into orginal form
    return str(ntime[:-2])  # return the string minus the AM/PM


print(timeConversion('07:05:45PM'))

# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array
