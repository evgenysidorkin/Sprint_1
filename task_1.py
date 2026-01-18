total_minutes = 0 
time = '1h 45m,360s,25m,30m 120s,2h 60s'
times = time.replace(',', ' ')
times = times.split(' ')

for tm in times:
    if 'h' in tm: 
        tm = int(tm.replace('h', '')) 
        total_minutes += tm * 60 
    elif 'm' in tm: 
        tm = int(tm.replace('m', '')) 
        total_minutes += tm
    else:
        tm = int(tm.replace('s', ''))
        total_minutes += tm // 60
        

print(total_minutes) 