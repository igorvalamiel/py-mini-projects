from time import sleep

def amp():
    v = ' '*10 + '#'*40
    
    l = list(range(1, 19))
    
    for i in l:
        sleep(0.01)
        print(v)
        v = ' '*(10+i) + '#'*(40-(2*i))
    for i in l[::-1]:
        sleep(0.01)
        print(v)
        v = ' '*(10+i) + '#'*(40-(2*i))

for i in range(0, 30):
    amp()