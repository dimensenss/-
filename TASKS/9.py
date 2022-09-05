win1251 = 'йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
koi8_r =  'ИЖСЙЕМЦЬЫГУЗТШБЮОПНКДФЩЪВЯЛХРЭАЧёижсйемцьыгузтшбюопнкдфщъвялхрэачЁ'
dos =     '©жгЄҐ­Јий§екдлў Їа®«¤¦нпзб¬ЁвмЎос‰–“Љ…Ќѓ™‡•љ”›‚ЂЏђЋ‹„†ќџ—‘Њ€’њЃћр'

win1251_to_koi8_r = dict(zip(win1251,koi8_r))
win1251_to_dos = dict(zip(win1251,dos))
koi8_r_to_dos = dict(zip(koi8_r,dos))
koi8_r_to_win1251 = dict(zip(koi8_r,win1251))
dos_to_win1251 = dict(zip(dos,win1251))
dos_to_koi8_r = dict(zip(dos,koi8_r))
print(win1251_to_koi8_r)
text = 'Привет'
print(len(text))
for i in len(text):
    print(i)
print(win1251_to_koi8_r[text[0]])