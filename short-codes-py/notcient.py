opc = str(input('Você deseja fazer ou desfazer uma Notação Científica? [f/d]: ')).lower()

while opc not in ('f', 'd', 'fazer', 'desfazer'):
    print('Valor inserido inválido. Por favor, tente novamente.')
    opc = str(input('Você deseja fazer ou desfazer uma Notação Científica? [f/d]: ')).lower()

#================================

if opc == 'f' or opc == 'fazer':
    num = float(input('Digite o valor que deseja transformar em notação científica: '))
    
    txtnum = str(num)
    qnum = len(txtnum) - 1
    intnum = num // 1
    qintnum = len(str(int(intnum)))
    qdecnum = qnum - qintnum
    decnum = (num - intnum) * (10**(qdecnum + 1))
    
    def fazer(x):
        expo = qintnum - 1
        nc = x / (10 ** expo)
        cd = qnum - 1
        return nc, expo, cd
    
    nc, expo, cd = fazer(num)
    print(f'{num} = {nc:.{cd}f} x 10^{expo}')

#================================

if opc == 'd' or opc == 'desfazer':
    anum = float(input('Digite o número base da notação científica: '))
    aexpo = int(input('Digite o expoente da notação científica: '))
   
    def desfazer(x, y):
        nc = x * (10 ** y)
        return nc
    
    anc = desfazer(anum, aexpo)
    print(f'{anum} x 10^{aexpo} = {anc}')
