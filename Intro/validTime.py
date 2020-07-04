def validTime(time):
    time = time.split(':')
    return int(time[0]) < 24 and int(time[1]) < 60
