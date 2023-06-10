form = input('Digite a fórmula: ')

num = []
let = []
function = ''

for a in form:
    if a.isnumeric():
        num.append(a)
    elif a.isalpha():
        if a.isupper():
            let.append(a)
        if a.islower():
            let[-1] += a
    else:
        pass

#obs: HCOOH -> ácido

if let[-2] == 'O' and let[-1] == 'H':
    function = 'Base'
elif let[0] == 'H':
    function = 'Ácido'
elif let[-1] == 'O' and len(let) == 2:
    function = 'Óxido'
else:
    function = 'Sal'
    
print(function)
