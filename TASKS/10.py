win1251 = 'йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
koi8_r =  'ИЖСЙЕМЦЬЫГУЗТШБЮОПНКДФЩЪВЯЛХРЭАЧёижсйемцьыгузтшбюопнкдфщъвялхрэачЁ'
dos =     '©жгЄҐ­Јий§екдлў Їа®«¤¦нпзб¬ЁвмЎос‰–“Љ…Ќѓ™‡•љ”›‚ЂЏђЋ‹„†ќџ—‘Њ€’њЃћр'

win1251_to_koi8_r = dict(zip(win1251,koi8_r))
win1251_to_dos = dict(zip(win1251,dos))
koi8_r_to_dos = dict(zip(koi8_r,dos))
koi8_r_to_win1251 = dict(zip(koi8_r,win1251))
dos_to_win1251 = dict(zip(dos,win1251))
dos_to_koi8_r = dict(zip(dos,koi8_r))
n = int(input('Какую кодировку вы выберете?\n1 - win1251\n2 - koi8-r\n3 - DOS\n\n'))
if n == 1:
    """ text = str(input("Введите текст: ")) """
    text = 'Привет'
    j = int(input('В какую кодировку перевести?\n1 - win1251\n2 - koi8-r\n3 - DOS\n\n'))
    if j == 1:
        text1 =[]
        for i in text:
            if i in win1251:
                text1.append(i)
            else:
                print('Eror')
        text1 = ''.join(text1)        
        print(text1)      
    if j == 2:
        text1 =[]
        for i in text:
            if i in win1251_to_koi8_r.keys():
                text1.append(win1251_to_koi8_r[i])
            else:
                print('Eror')
        text1 = ''.join(text1)        
        print(text1)          
    if j == 3:
        text1 =[]
        for i in text:
            if i in win1251_to_koi8_r.keys():
                text1.append(win1251_to_dos[i])
            else:
                print('Eror')
        text1 = ''.join(text1)        
        print(text1)             
if n == 2:
    """ text = str(input("Введите текст: ")) """
    text = 'Привет'
    j = int(input('В какую кодировку перевести?\n1 - win1251\n2 - koi8-r\n3 - DOS\n\n'))
    if j == 1:
        text1 =[]
        for i in text:
            if i in koi8_r_to_win1251.keys():
                text1.append(koi8_r_to_win1251[i])
            else:
                print('Eror')
        text1 = ''.join(text1)        
        print(text1)      
    if j == 2:
        text1 =[]
        for i in text:
            if i in koi8_r:
                text1.append(i)
            else:
                print('Eror')
        text1 = ''.join(text1)        
        print(text1)            
    if j == 3:
        text1 =[]
        for i in text:
            if i in koi8_r_to_dos.keys():
                text1.append(koi8_r_to_dos[i])
            else:
                print('Eror')
        text1 = ''.join(text1)        
        print(text1)
if n == 3:        
    """ text = str(input("Введите текст: ")) """
    text = 'Привет'
    j = int(input('В какую кодировку перевести?\n1 - win1251\n2 - koi8-r\n3 - DOS\n\n'))
    if j == 1:
        text1 =[]
        for i in text:
            if i in dos_to_win1251.keys():
                text1.append(dos_to_win1251[i])
            else:
                print('Eror')
        text1 = ''.join(text1)        
        print(text1)      
    if j == 2:
        text1 =[]
        for i in text:
            if i in dos_to_koi8_r.keys():
                text1.append(dos_to_koi8_r[i])
            else:
                print('Eror')
        text1 = ''.join(text1)        
        print(text1)          
    if j == 3:
        text1 =[]
        for i in text:
            if i in dos:
                text1.append(i)
            else:
                print('Eror')
        text1 = ''.join(text1)        
        print(text1)           


 