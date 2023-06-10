pal = str(input('Digite a palavra (sem a acentuação): ')).lower()
sil = int(input('\nDigite quantas sílabas a palavra tem: '))

acent = False
sila = ''
pq = ''

if sil == 1:
    if pal[-1] in ['a', 'e', 'o']:
        acent = True
        sa = (pal[-1]).upper()
        pq = f'monosílaba tônica terminada em {sa}'
    if pal[-2::] in ['as', 'es', 'os']:
        acent = True
        sa = (pal[-2::]).upper()
        pq = f'monosílaba tônica terminada em {sa}'

else:
    print('''
1 - última
2 - penúltima
3 - antepenúltima''')
    ton = int(input('Digite a posição da sílava tônica (1, 2 ou 3): '))
    
    if ton == 1:
        if pal[-1] in ['a', 'e', 'o']:
            acent = True
            sa = (pal[-1]).upper()
            pq = f'oxítona terminada em {sa}'
        if pal[-2::] in ['as', 'es', 'os', 'em']:
            acent = True
            sa = (pal[-2::]).upper()
            pq = f'oxitona terminada em {sa}'
        if pal[-3::] == 'ens':
            acent = True
            pq = 'oxítona terminada em ENS'
        sila = 'última'

    if ton == 2:
        if pal[-1] in ['l', 'x']:
            sila = 'penúltima'
            pq = f'paroxítona terminada em {pal[-1].upper()}'
        acent = True
    
    if ton == 3:
        acent = True
        pq = 'toda proparoxítona é acentuada'
        sila = 'antepenúltima'
    
if acent and sil != 1:
   print(f'\nA palavra é acentuada na {sila} sílaba, pois é uma {pq}.')
elif acent and sil == 1:
    print(f'\nA palavra é acentuada, pois é uma {pq}.')
else:
   print('\nA palavra não é acentuada.')
   