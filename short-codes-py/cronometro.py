from time import sleep

s = m = h = 0

while True: 
    sleep(1)
    s += 1
    if s == 59:
        s = 0
        m += 1
        if m == 59:
            m = 0
            h += 1
    hour = str(h)
    minute = str(m)
    second = str(s)
    print(f'{hour}:{minute}:{second}')