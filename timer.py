sec = 0
minute = 58
hour = 9

time = ""

def update_time():
    global sec, minute, hour
    sec += 1
    if sec == 60:
        sec = 0
        minute += 1
    if minute == 60:
        minute = 0
        hour += 1
    
    tsec = f'{sec}' if sec >= 10 else f'{sec:02}'
    tmin = f'{minute}' if minute >= 10 else f'{minute:02}'
    thour = f'{hour}' if hour >= 10 else f'{hour:02}'

    print(f'{thour}:{tmin}:{tsec}')

while True:
    input()
    update_time()