import os, sys, time, webbrowser, re, subprocess
import urllib.request
from playsound import playsound
import pathlib
from pathlib import Path
from os import environ, getcwd
import pyautogui
import colorama

from colorama import Back, Style, Fore
from gtts import gTTS 
colorama.init()


def да():
    playsound('C:/Users/'+user+'/Jarvis/da.wav')
    
def загружаю():
    playsound('C:/Users/'+user+'/Jarvis/Загружаю сэр.wav')
    
def есть():
    playsound('C:/Users/'+user+'/Jarvis/Есть.wav')

def чего():
    playsound('C:/Users/'+user+'/Jarvis/Чего вы пытаетесь добиться сэр.wav')

def мы():
    playsound('C:/Users/'+user+'/Jarvis/Мы подключены и готовы.wav')

def как_пож():
    playsound('C:/Users/'+user+'/Jarvis/Как пожелаете.wav')


getUser = lambda: environ['USERNAME']
user = getUser()


colorama.init()

def res():
    print(Style.RESET_ALL)



print(colorama.Fore.GREEN+'   ╔═══════════════════════════════════════════════╗')
print(colorama.Fore.GREEN+'   ║ '+Fore.WHITE+'Как назвать папку, куда можно скачать музыку?'+Fore.GREEN+' ║')
print(colorama.Fore.GREEN+'   ╚═══════════════════════════════════════════════╝')
time.sleep(0.5)
res()
print('         Она будет создана в C:/Users/user/'+'\n')
print(colorama.Fore.GREEN+   '   ╔═════════════════════════╗'+Style.RESET_ALL)
k = input(                       '     Название папки --> ')

try:
    d = 'c:/Users/'+user+'/'+k
    os.mkdir(d)
    print('\n         Папка '+k+ ' создана в '+ d)
    time.sleep(2)
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Really Slow Motion - Deadwood.mp3')
    if path.exists() == False:                           
        url1 = 'https://ru.hitmotop.com/get/music/20190627/Really_Slow_Motion_-_Deadwood_65256742.mp3'
        urllib.request.urlretrieve(url1, 'c:/Users/'+user+'/'+k+'/Really Slow Motion - Deadwood.mp3')
        print('\n     Файл Really Slow Motion - Deadwood' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Really Slow Motion - Deadwood'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        os.system('cls')
        
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Slipknot - Duality.mp3')
    if path.exists() == False:                           
        url2 = 'https://ru.hitmotop.com/get/music/20170902/Slipknot_-_Duality_47954348.mp3'
        urllib.request.urlretrieve(url2, 'c:/Users/'+user+'/'+k+'/Slipknot - Duality.mp3')
        print('\n     Файл Slipknot - Duality' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Slipknot - Duality'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(2)
        os.system('cls')
        
    
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Король и Шут - Прыгну со скалы.mp3')
    if path.exists() == False:                           
        url3 = 'https://ru.hitmotop.com/get/music/20190305/Korol_i_SHut_-_Prygnu_so_skaly_62570549.mp3'
        urllib.request.urlretrieve(url3, 'c:/Users/'+user+'/'+k+'/Король и Шут - Прыгну со скалы.mp3')
        print('\n     Файл Король и Шут - Прыгну со скалы' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Король и Шут - Прыгну со скалы'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        os.system('cls')
    
    
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Король и Шут - Кукла колдуна.mp3')
    if path.exists() == False:                           
        url4 = 'https://ru.hitmotop.com/get/music/20190305/Korol_i_SHut_-_Kukla_kolduna_62570545.mp3'
        urllib.request.urlretrieve(url4, 'c:/Users/'+user+'/'+k+'/Король и Шут - Кукла колдуна.mp3')
        print('\n     Файл Король и Шут - Кукла колдуна' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Король и Шут - Кукла колдуна'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        os.system('cls')
    
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Король и Шут - Ром.mp3')
    if path.exists() == False:                           
        url5 = 'https://ru.hitmotop.com/get/music/20170918/Korol_i_SHut_-_Rom_48646395.mp3'
        urllib.request.urlretrieve(url5, 'c:/Users/'+user+'/'+k+'/Король и Шут - Ром.mp3')
        print('\n     Файл Король и Шут - Ром' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Король и Шут - Ром'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        os.system('cls')
    
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Король и Шут - Маска.mp3')
    if path.exists() == False:                           
        url6 = 'https://ru.hitmotop.com/get/music/20170918/Korol_i_SHut_-_Maska_48646394.mp3'
        urllib.request.urlretrieve(url6, 'c:/Users/'+user+'/'+k+'/Король и Шут - Маска.mp3')
        print('\n     Файл Король и Шут - Маска' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Король и Шут - Маска'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        os.system('cls')
    
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Slipknot - Before I Forget.mp3')
    if path.exists() == False:                           
        url7 = 'https://ru.hitmotop.com/get/music/20170902/Slipknot_-_Before_I_Forget_47954384.mp3'
        urllib.request.urlretrieve(url7, 'c:/Users/'+user+'/'+k+'/Slipknot - Before I Forget.mp3')
        print('\n     Файл Slipknot - Before I Forget' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Slipknot - Before I Forget'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        os.system('cls')

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Slipknot - Psychosocial.mp3')
    if path.exists() == False:                           
        url8 = 'https://ru.hitmotop.com/get/music/20170902/Slipknot_-_Psychosocial_47954626.mp3'
        urllib.request.urlretrieve(url8, 'c:/Users/'+user+'/'+k+'/Slipknot - Psychosocial.mp3')
        print('\n     Файл Slipknot - Psychosocial' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Slipknot - Psychosocial'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        os.system('cls')

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Slipknot - Unsainted.mp3')
    if path.exists() == False:                           
        url9 = 'https://ru.hitmotop.com/get/music/20190518/Slipknot_-_Unsainted_64305760.mp3'
        urllib.request.urlretrieve(url9, 'c:/Users/'+user+'/'+k+'/Slipknot - Unsainted.mp3')
        print('\n     Файл Slipknot - Unsainted' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Slipknot - Unsainted'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        os.system('cls')
        
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Exile - Lost Control.mp3')
    if path.exists() == False:                           
        url10 = 'https://ru.hitmotop.com/get/music/20201118/Exile_-_Lost_Control_71646673.mp3'
        urllib.request.urlretrieve(url10, 'c:/Users/'+user+'/'+k+'/Exile - Lost Control.mp3')
        print('\n     Файл Exile - Lost Control' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Exile - Lost Control'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        os.system('cls')
    
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Exile - Tututu.mp3')
    if path.exists() == False:                           
        url11 = 'https://ru.hitmotop.com/get/music/20201118/Exile_-_Tututu_71646674.mp3'
        urllib.request.urlretrieve(url11, 'c:/Users/'+user+'/'+k+'/Exile - Tututu.mp3')
        print('\n     Файл Exile - Tututu' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Exile - Tututu'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        os.system('cls')
        
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Exile - Castle.mp3')
    if path.exists() == False:                           
        url12 = 'https://ru.hitmotop.com/get/music/20201118/Exile_-_Castle_71646681.mp3'
        urllib.request.urlretrieve(url12, 'c:/Users/'+user+'/'+k+'/Exile - Castle.mp3')
        print('\n     Файл Exile - Castle' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Exile - Castle'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Ghostemane - Fed Up.mp3')
    if path.exists() == False:                           
        url13 = 'https://ru.hitmotop.com/get/music/20201022/Ghostemane_-_Fed_Up_71339681.mp3'
        urllib.request.urlretrieve(url13, 'c:/Users/'+user+'/'+k+'/Ghostemane - Fed Up.mp3')
        print('\n     Файл Ghostemane - Fed Up' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Ghostemane - Fed Up'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)  
    
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/AC_DC - War Machine.mp3')
    if path.exists() == False:                           
        url14 = 'https://ru.hitmotop.com/get/music/20170830/ACDC_-_War_Machine_47830058.mp3'
        urllib.request.urlretrieve(url14, 'c:/Users/'+user+'/'+k+'/AC_DC - War Machine.mp3')
        print('\n     Файл AC/DC - War Machine' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл AC/DC - War Machine'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/AC_DC - Back In Black.mp3')
    if path.exists() == False:                           
        url15 = 'https://ru.hitmotop.com/get/music/20170830/ACDC_-_Back_In_Black_47830042.mp3'
        urllib.request.urlretrieve(url15, 'c:/Users/'+user+'/'+k+'/AC_DC - Back In Black.mp3')
        print('\n     Файл AC/DC - Back In Black' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл AC/DC - Back In Black'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)


    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Где нас нет.mp3')
    if path.exists() == False:                           
        url16 = 'https://ru.hitmotop.com/get/music/20170830/Oxxxymiron_-_Gde_nas_net_47828363.mp3'
        urllib.request.urlretrieve(url16, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Где нас нет.mp3')
        print('\n     Файл Oxxxymiron - Где нас нет' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron - Где нас нет'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5) 

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Больше Бена.mp3')
    if path.exists() == False:                           
        url17 = 'https://ru.hitmotop.com/get/music/20170830/Oxxxymiron_-_Bolshe_Bena_47829561.mp3'
        urllib.request.urlretrieve(url17, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Больше Бена.mp3')
        print('\n     Файл Oxxxymiron - Больше Бена' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron - Больше Бена'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Кем ты стал.mp3')
    if path.exists() == False:                           
        url18 = 'https://ru.hitmotop.com/get/music/20170830/Oxxxymiron_-_Kem_ty_stal_47828349.mp3'
        urllib.request.urlretrieve(url18, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Кем ты стал.mp3')
        print('\n     Файл Oxxxymiron - Кем ты стал' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron - Кем ты стал'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - В долгий путь (1 раунд 17ib).mp3')
    if path.exists() == False:                           
        url19 = 'https://ru.hitmotop.com/get/music/20190909/Oxxxymiron_-_V_dolgijj_put_1_raund_17ib_66491831.mp3'
        urllib.request.urlretrieve(url19, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - В долгий путь (1 раунд 17ib).mp3')
        print('\n     Файл Oxxxymiron - В долгий путь (1 раунд 17ib)' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron - В долгий путь (1 раунд 17ib)'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib).mp3')
    if path.exists() == False:                           
        url20 = 'https://ru.hitmotop.com/get/music/20191109/Oxxxymiron_Samariddin_Radzhabov_-_Veter_peremen_67218029.mp3'
        urllib.request.urlretrieve(url20, 'c:/Users/'+user+'/'+k+'/Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib).mp3')
        print('\n     Файл Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib)' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib)'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)


    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Дело нескольких минут.mp3')
    if path.exists() == False:                           
        url21 = 'https://ru.hitmotop.com/get/music/20211113/Oxxxymiron_-_Delo_neskolkikh_minut_73314777.mp3'
        urllib.request.urlretrieve(url21, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Дело нескольких минут.mp3')
        print('\n     Файл Oxxxymiron - Дело нескольких минут' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron - Дело нескольких минут'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)


    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib).mp3')
    if path.exists() == False:                           
        url22 = 'https://ru.hitmotop.com/get/music/20200206/Oxxxymiron_-_V_knige_vsjo_bylo_po-drugomu_68273638.mp3'
        urllib.request.urlretrieve(url22, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib).mp3')
        print('\n     Файл Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib)' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib)'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
    
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Переплетено.mp3')
    if path.exists() == False:                           
        url23 = 'https://ru.hitmotop.com/get/music/20170830/Oxxxymiron_-_Perepleteno_47828355.mp3'
        urllib.request.urlretrieve(url23, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Переплетено.mp3')
        print('\n     Файл Oxxxymiron - Переплетено' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron - Переплетено'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Город под подошвой.mp3')
    if path.exists() == False:                           
        url24 = 'https://ru.hitmotop.com/get/music/20170901/Oxxxymiron_-_Gorod_pod_podoshvojj_47921143.mp3'
        urllib.request.urlretrieve(url24, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Город под подошвой.mp3')
        print('\n     Файл Oxxxymiron - Город под подошвой' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron - Город под подошвой'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)


    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/PORCHY, MAY WAVE, JEEMBO, LOQIEMEAN, THOMAS MRAZ, TVETH, SOULOUD, MARKUL, OXYMIRON - KONSTRUKT.mp3')
    if path.exists() == False:                           
        url25 = 'https://ru.hitmotop.com/get/music/20180817/PORCHY_MAY_WAVE_JEEMBO_LOQIEMEAN_THOMAS_MRAZ_TVETH_SOULOUD_MARKUL_OXYMIRON_-_KONSTRUKT_58034566.mp3'
        urllib.request.urlretrieve(url25, 'c:/Users/'+user+'/'+k+'/PORCHY, MAY WAVE, JEEMBO, LOQIEMEAN, THOMAS MRAZ, TVETH, SOULOUD, MARKUL, OXYMIRON - KONSTRUKT.mp3')
        print('\n     Файл PORCHY, MAY WAVE, JEEMBO, LOQIEMEAN, THOMAS MRAZ, TVETH, SOULOUD, MARKUL, OXYMIRON - KONSTRUKT' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл PORCHY, MAY WAVE, JEEMBO, LOQIEMEAN, THOMAS MRAZ, TVETH, SOULOUD, MARKUL, OXYMIRON - KONSTRUKT'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)


    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron, Markul - Fata Morgana.mp3')
    if path.exists() == False:                           
        url26 = 'https://ru.hitmotop.com/get/music/20191117/Oxxxymiron_Markul_-_Fata_Morgana_67311405.mp3'
        urllib.request.urlretrieve(url26, 'c:/Users/'+user+'/'+k+'/Oxxxymiron, Markul - Fata Morgana.mp3')
        print('\n     Файл Oxxxymiron, Markul - Fata Morgana' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron, Markul - Fata Morgana'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - Slowmotion.mp3')
    if path.exists() == False:                           
        url27 = 'https://ru.hitmotop.com/get/music/20190807/JOHAN_x_Goddamn_-_Slowmotion_65947794.mp3'
        urllib.request.urlretrieve(url27, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Slowmotion.mp3')
        print('\n     Файл JOHAN x Goddamn - Slowmotion' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл JOHAN x Goddamn - Slowmotion'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)


    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - Инферно 2.0.mp3')
    if path.exists() == False:                           
        url28 = 'https://ruy.zvukofon.com/dl/1138471416/JOHAN_Goddamn_-_Inferno_20_(musportal.org).mp3'
        urllib.request.urlretrieve(url28, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Инферно 2.0.mp3')
        print('\n     Файл JOHAN x Goddamn - Инферно 2.0' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл JOHAN x Goddamn - Инферно 2.0'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - Инсомния.mp3')
    if path.exists() == False:                           
        url29 = 'https://ru.hitmotop.com/get/music/20190401/JOHAN_x_Goddamn_-_Insomniya_63214349.mp3'
        urllib.request.urlretrieve(url29, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Инсомния.mp3')
        print('\n     Файл JOHAN x Goddamn - Инсомния' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл JOHAN x Goddamn - Инсомния'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - 1100.mp3')
    if path.exists() == False:                           
        url30 = 'https://rum.muzikavsem.org/dl/1135735277/JOHAN_x_Goddamn_-_1100_(rum.muzikavsem.org).mp3'
        urllib.request.urlretrieve(url30, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - 1100.mp3')
        print('\n     Файл JOHAN x Goddamn - 1100' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл JOHAN x Goddamn - 1100'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - Inferno.mp3')
    if path.exists() == False:                           
        url31 = 'https://ru.hitmotop.com/get/music/20190427/JOHAN_x_Goddamn_-_Inferno_63783589.mp3'
        urllib.request.urlretrieve(url31, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Inferno.mp3')
        print('\n     Файл JOHAN x Goddamn - Inferno' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл JOHAN x Goddamn - Inferno'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - Рецидив.mp3')
    if path.exists() == False:                           
        url32 = 'https://ru.hitmotop.com/get/music/20190425/JOHAN_x_Goddamn_-_Recidiv_63734390.mp3'
        urllib.request.urlretrieve(url32, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Рецидив.mp3')
        print('\n     Файл JOHAN x Goddamn - Рецидив' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл JOHAN x Goddamn - Рецидив'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - Марианская впадина.mp3')
    if path.exists() == False:                           
        url33 = 'https://ru.hitmotop.com/get/music/20200109/JOHAN_x_Goddamn_-_Marianskaya_vpadina_67911874.mp3'
        urllib.request.urlretrieve(url33, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Марианская впадина.mp3')
        print('\n     Файл JOHAN x Goddamn - Марианская впадина' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл JOHAN x Goddamn - Марианская впадина'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        
        
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Goddamn - Ногами вверх.mp3')
    if path.exists() == False:                           
        url34 = 'https://ru.hitmotop.com/get/music/20210118/Goddamn_-_Nogami_vverkh_72361848.mp3'
        urllib.request.urlretrieve(url34, 'c:/Users/'+user+'/'+k+'/Goddamn - Ногами вверх.mp3')
        print('\n     Файл Goddamn - Ногами вверх' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Goddamn - Ногами вверх'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
        
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Disturbed - Stricken.mp3')
    if path.exists() == False:                           
        url35 = 'https://ru.hitmotop.com/get/music/20170830/Disturbed_-_Stricken_47829348.mp3'
        urllib.request.urlretrieve(url35, 'c:/Users/'+user+'/'+k+'/Disturbed - Stricken.mp3')
        print('\n     Файл Disturbed - Stricken' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Disturbed - Stricken'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Disturbed - Open Your Eyes.mp3')
    if path.exists() == False:                           
        url36 = 'https://ru.hitmotop.com/get/music/20170908/Disturbed_-_Open_Your_Eyes_48407460.mp3'
        urllib.request.urlretrieve(url36, 'c:/Users/'+user+'/'+k+'/Disturbed - Open Your Eyes.mp3')
        print('\n     Файл Disturbed - Open Your Eyes' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Disturbed - Open Your Eyes'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Агент.mp3')
    if path.exists() == False:                           
        url37 = 'https://ru.hitmotop.com/get/music/20211205/Oxxxymiron_-_Agent_73431910.mp3'
        urllib.request.urlretrieve(url37, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Агент.mp3')
        print('\n     Файл Oxxxymiron - Агент' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron - Агент'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Мы все умрем.mp3')
    if path.exists() == False:                           
        url38 = 'https://ru.hitmotop.com/get/music/20211205/Oxxxymiron_-_My_vse_umrem_73431914.mp3'
        urllib.request.urlretrieve(url38, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Мы все умрем.mp3')
        print('\n     Файл Oxxxymiron - Мы все умрем' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron - Мы все умрем'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - ОРГАНИЗАЦИЯ.mp3')
    if path.exists() == False:                           
        url39 = 'https://ru.hitmotop.com/get/music/20211111/Oxxxymiron_-_ORGANIZACIYA_73302782.mp3'
        urllib.request.urlretrieve(url39, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - ОРГАНИЗАЦИЯ.mp3')
        print('\n     Файл Oxxxymiron - ОРГАНИЗАЦИЯ' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Oxxxymiron - ОРГАНИЗАЦИЯ'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Alan Walker, Jamie Miller - Running Out of Roses.mp3')
    if path.exists() == False:                           
        url40 = 'https://ru.hitmotop.com/get/music/20210910/Alan_Walker_Jamie_Miller_-_Running_Out_of_Roses_73156491.mp3'
        urllib.request.urlretrieve(url40, 'c:/Users/'+user+'/'+k+'/Alan Walker, Jamie Miller - Running Out of Roses.mp3')
        print('\n     Файл Alan Walker, Jamie Miller - Running Out of Roses' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Alan Walker, Jamie Miller - Running Out of Roses'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)
    
    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Alan Walker, Imanbek - Sweet Dreams.mp3')
    if path.exists() == False:                           
        url41 = 'https://ru.hitmotop.com/get/music/20210611/Alan_Walker_Imanbek_-_Sweet_Dreams_72998823.mp3'
        urllib.request.urlretrieve(url41, 'c:/Users/'+user+'/'+k+'/Alan Walker, Imanbek - Sweet Dreams.mp3')
        print('\n     Файл Alan Walker, Imanbek - Sweet Dreams' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Alan Walker, Imanbek - Sweet Dreams'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)

    path = pathlib.Path('C:/Users/'+ user +'/'+k+'/Alan Walker - Legends Never Die.mp3')
    if path.exists() == False:                           
        url42 = 'https://ru.hitmotop.com/get/music/20180303/League_of_Legends_Alan_Walker_League_of_Legends_Alan_Walker_Again_-_Legends_Never_Die_54268252.mp3'
        urllib.request.urlretrieve(url42, 'c:/Users/'+user+'/'+k+'/Alan Walker - Legends Never Die.mp3')
        print('\n     Файл Alan Walker - Legends Never Die' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
        time.sleep(0.5)
    else:
        print('\n     Файл Alan Walker - Legends Never Die'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
        time.sleep(0.5)



except FileExistsError:
    print("\n     Эта папка"+ colorama.Fore.CYAN+ ' уже '+ Style.RESET_ALL +'существует\n')
    time.sleep(3)
    h = input('     Скачать туда да/нет --> ')
    os.system('cls')
    if h == 'да':
        path1 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Really Slow Motion - Deadwood.mp3')
        if path1.exists() == False:       
            url11 = 'https://ru.hitmotop.com/get/music/20190627/Really_Slow_Motion_-_Deadwood_65256742.mp3'
            urllib.request.urlretrieve(url11, 'c:/Users/'+user+'/'+k+'/Really Slow Motion - Deadwood.mp3')
            print('\n     Файл Really Slow Motion - Deadwood' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(2)
        else:       
            print('\n     Файл Really Slow Motion - Deadwood'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            
        
        path2 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Slipknot - Duality.mp3')
        if path2.exists() == False:  
            url22 = 'https://ru.hitmotop.com/get/music/20170902/Slipknot_-_Duality_47954348.mp3'
            urllib.request.urlretrieve(url22, 'c:/Users/'+user+'/'+k+'/Slipknot - Duality.mp3')
            print('\n     Файл Slipknot - Duality' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)  
            time.sleep(0.5) 
        else:
            print('\n     Файл Slipknot - Duality'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5) 
            
        
        path3 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Король и Шут - Прыгну со скалы.mp3')
        if path3.exists() == False:
            url33 = 'https://ru.hitmotop.com/get/music/20190305/Korol_i_SHut_-_Prygnu_so_skaly_62570549.mp3'
            urllib.request.urlretrieve(url33, 'c:/Users/'+user+'/'+k+'/Король и Шут - Прыгну со скалы.mp3')
            print('\n     Файл Король и Шут - Прыгну со скалы' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Король и Шут - Прыгну со скалы'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5) 
            
        
        path4 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Король и Шут - Кукла колдуна.mp3')
        if path4.exists() == False:
            url44 = 'https://ru.hitmotop.com/get/music/20190305/Korol_i_SHut_-_Kukla_kolduna_62570545.mp3'
            urllib.request.urlretrieve(url44, 'c:/Users/'+user+'/'+k+'/Король и Шут - Кукла колдуна.mp3')
            print('\n     Файл Король и Шут - Кукла колдуна' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Король и Шут - Кукла колдуна'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5) 
            
        path5 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Король и Шут - Ром.mp3')
        if path5.exists() == False:
            url55 = 'https://ru.hitmotop.com/get/music/20170918/Korol_i_SHut_-_Rom_48646395.mp3'
            urllib.request.urlretrieve(url55, 'c:/Users/'+user+'/'+k+'/Король и Шут - Ром.mp3')
            print('\n     Файл Король и Шут - Ром' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Король и Шут - Ром'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5) 
        
        path6 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Король и Шут - Маска.mp3')
        if path6.exists() == False:
            url66 = 'https://ru.hitmotop.com/get/music/20170918/Korol_i_SHut_-_Maska_48646394.mp3'
            urllib.request.urlretrieve(url66, 'c:/Users/'+user+'/'+k+'/Король и Шут - Маска.mp3')
            print('\n     Файл Король и Шут - Маска' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Король и Шут - Маска'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5) 
        
        path7 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Slipknot - Before I Forget.mp3')
        if path7.exists() == False:
            url77 = 'https://ru.hitmotop.com/get/music/20170902/Slipknot_-_Before_I_Forget_47954384.mp3'
            urllib.request.urlretrieve(url77, 'c:/Users/'+user+'/'+k+'/Slipknot - Before I Forget.mp3')
            print('\n     Файл Slipknot - Before I Forget' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Slipknot - Before I Forget'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5) 
        
        path8 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Slipknot - Psychosocial.mp3')
        if path8.exists() == False: 
            url88 = 'https://ru.hitmotop.com/get/music/20170902/Slipknot_-_Psychosocial_47954626.mp3'
            urllib.request.urlretrieve(url88, 'c:/Users/'+user+'/'+k+'/Slipknot - Psychosocial.mp3')
            print('\n     Файл Slipknot - Psychosocial' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Slipknot - Psychosocial'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5) 
        
        path9 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Slipknot - Unsainted.mp3')
        if path9.exists() == False:                           
            url99 = 'https://ru.hitmotop.com/get/music/20190518/Slipknot_-_Unsainted_64305760.mp3'
            urllib.request.urlretrieve(url99, 'c:/Users/'+user+'/'+k+'/Slipknot - Unsainted.mp3')
            print('\n     Файл Slipknot - Unsainted' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Slipknot - Unsainted'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5) 
           
        path10 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Exile - Lost Control.mp3')
        if path10.exists() == False:                           
            url10 = 'https://ru.hitmotop.com/get/music/20201118/Exile_-_Lost_Control_71646673.mp3'
            urllib.request.urlretrieve(url10, 'c:/Users/'+user+'/'+k+'/Exile - Lost Control.mp3')
            print('\n     Файл Exile - Lost Control' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Exile - Lost Control'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5) 
        
        path11 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Exile - Tututu.mp3')
        if path11.exists() == False:                           
            url11 = 'https://ru.hitmotop.com/get/music/20201118/Exile_-_Tututu_71646674.mp3'
            urllib.request.urlretrieve(url11, 'c:/Users/'+user+'/'+k+'/Exile - Tututu.mp3')
            print('\n     Файл Exile - Tututu' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Exile - Tututu'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5) 
            
        path12 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Exile - Castle.mp3')
        if path12.exists() == False:                           
            url12 = 'https://ru.hitmotop.com/get/music/20201118/Exile_-_Castle_71646681.mp3'
            urllib.request.urlretrieve(url12, 'c:/Users/'+user+'/'+k+'/Exile - Castle.mp3')
            print('\n     Файл Exile - Castle' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Exile - Castle'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)    
        

        path13 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Ghostemane - Fed Up.mp3')
        if path13.exists() == False:                           
            url13 = 'https://ru.hitmotop.com/get/music/20201022/Ghostemane_-_Fed_Up_71339681.mp3'
            urllib.request.urlretrieve(url13, 'c:/Users/'+user+'/'+k+'/Ghostemane - Fed Up.mp3')
            print('\n     Файл Ghostemane - Fed Up' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Ghostemane - Fed Up'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5) 
        
        path14 = pathlib.Path('C:/Users/'+ user +'/'+k+'/AC_DC - War Machine.mp3')
        if path14.exists() == False:                           
            url14 = 'https://ru.hitmotop.com/get/music/20170830/ACDC_-_War_Machine_47830058.mp3'
            urllib.request.urlretrieve(url14, 'c:/Users/'+user+'/'+k+'/AC_DC - War Machine.mp3')
            print('\n     Файл AC/DC - War Machine' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл AC/DC - War Machine'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)    
          
        path15 = pathlib.Path('C:/Users/'+ user +'/'+k+'/AC_DC - Back In Black.mp3')
        if path15.exists() == False:                           
            url15 = 'https://ru.hitmotop.com/get/music/20170830/ACDC_-_Back_In_Black_47830042.mp3'
            urllib.request.urlretrieve(url15, 'c:/Users/'+user+'/'+k+'/AC_DC - Back In Black.mp3')
            print('\n     Файл AC/DC - Back In Black' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл AC/DC - Back In Black'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)   
       
        path16 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Где нас нет.mp3')
        if path16.exists() == False:                           
            url16 = 'https://ru.hitmotop.com/get/music/20170830/Oxxxymiron_-_Gde_nas_net_47828363.mp3'
            urllib.request.urlretrieve(url16, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Где нас нет.mp3')
            print('\n     Файл Oxxxymiron - Где нас нет' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Oxxxymiron - Где нас нет'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)      
         
        path17 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Больше Бена.mp3')
        if path17.exists() == False:                           
            url17 = 'https://ru.hitmotop.com/get/music/20170830/Oxxxymiron_-_Bolshe_Bena_47829561.mp3'
            urllib.request.urlretrieve(url17, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Больше Бена.mp3')
            print('\n     Файл Oxxxymiron - Больше Бена' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Oxxxymiron - Больше Бена'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5) 
       
        path18 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Кем ты стал.mp3')
        if path18.exists() == False:                           
            url18 = 'https://ru.hitmotop.com/get/music/20170830/Oxxxymiron_-_Kem_ty_stal_47828349.mp3'
            urllib.request.urlretrieve(url18, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Кем ты стал.mp3')
            print('\n     Файл Oxxxymiron - Кем ты стал' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5) 
        else:
            print('\n     Файл Oxxxymiron - Кем ты стал'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)       
        
        path19 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - В долгий путь (1 раунд 17ib).mp3')
        if path19.exists() == False:                           
            url19 = 'https://ru.hitmotop.com/get/music/20190909/Oxxxymiron_-_V_dolgijj_put_1_raund_17ib_66491831.mp3'
            urllib.request.urlretrieve(url19, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - В долгий путь (1 раунд 17ib).mp3')
            print('\n     Файл Oxxxymiron - В долгий путь (1 раунд 17ib)' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Oxxxymiron - В долгий путь (1 раунд 17ib)'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
       
        path20 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib).mp3')
        if path20.exists() == False:                           
            url20 = 'https://ru.hitmotop.com/get/music/20191109/Oxxxymiron_Samariddin_Radzhabov_-_Veter_peremen_67218029.mp3'
            urllib.request.urlretrieve(url20, 'c:/Users/'+user+'/'+k+'/Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib).mp3')
            print('\n     Файл Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib)' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib)'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path21 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Дело нескольких минут.mp3')
        if path21.exists() == False:                           
            url21 = 'https://ru.hitmotop.com/get/music/20211113/Oxxxymiron_-_Delo_neskolkikh_minut_73314777.mp3'
            urllib.request.urlretrieve(url21, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Дело нескольких минут.mp3')
            print('\n     Файл Oxxxymiron - Дело нескольких минут' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Oxxxymiron - Дело нескольких минут'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path22 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib).mp3')
        if path22.exists() == False:                           
            url22 = 'https://ru.hitmotop.com/get/music/20200206/Oxxxymiron_-_V_knige_vsjo_bylo_po-drugomu_68273638.mp3'
            urllib.request.urlretrieve(url22, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib).mp3')
            print('\n     Файл Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib)' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib)'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path23 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Переплетено.mp3')
        if path23.exists() == False:                           
            url23 = 'https://ru.hitmotop.com/get/music/20170830/Oxxxymiron_-_Perepleteno_47828355.mp3'
            urllib.request.urlretrieve(url23, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Переплетено.mp3')
            print('\n     Файл Oxxxymiron - Переплетено' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Oxxxymiron - Переплетено'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path24 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Город под подошвой.mp3')
        if path24.exists() == False:                           
            url24 = 'https://ru.hitmotop.com/get/music/20170901/Oxxxymiron_-_Gorod_pod_podoshvojj_47921143.mp3'
            urllib.request.urlretrieve(url24, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Город под подошвой.mp3')
            print('\n     Файл Oxxxymiron - Город под подошвой' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Oxxxymiron - Город под подошвой'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path25 = pathlib.Path('C:/Users/'+ user +'/'+k+'/PORCHY, MAY WAVE, JEEMBO, LOQIEMEAN, THOMAS MRAZ, TVETH, SOULOUD, MARKUL, OXYMIRON - KONSTRUKT.mp3')
        if path25.exists() == False:                           
            url25 = 'https://ru.hitmotop.com/get/music/20180817/PORCHY_MAY_WAVE_JEEMBO_LOQIEMEAN_THOMAS_MRAZ_TVETH_SOULOUD_MARKUL_OXYMIRON_-_KONSTRUKT_58034566.mp3'
            urllib.request.urlretrieve(url25, 'c:/Users/'+user+'/'+k+'/PORCHY, MAY WAVE, JEEMBO, LOQIEMEAN, THOMAS MRAZ, TVETH, SOULOUD, MARKUL, OXYMIRON - KONSTRUKT.mp3')
            print('\n     Файл PORCHY, MAY WAVE, JEEMBO, LOQIEMEAN, THOMAS MRAZ, TVETH, SOULOUD, MARKUL, OXYMIRON - KONSTRUKT' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл PORCHY, MAY WAVE, JEEMBO, LOQIEMEAN, THOMAS MRAZ, TVETH, SOULOUD, MARKUL, OXYMIRON - KONSTRUKT'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path26 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron, Markul - Fata Morgana.mp3')
        if path26.exists() == False:                           
            url26 = 'https://ru.hitmotop.com/get/music/20191117/Oxxxymiron_Markul_-_Fata_Morgana_67311405.mp3'
            urllib.request.urlretrieve(url26, 'c:/Users/'+user+'/'+k+'/Oxxxymiron, Markul - Fata Morgana.mp3')
            print('\n     Файл Oxxxymiron, Markul - Fata Morgana' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Oxxxymiron, Markul - Fata Morgana'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path27 = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - Slowmotion.mp3')
        if path27.exists() == False:                           
            url27 = 'https://ru.hitmotop.com/get/music/20190807/JOHAN_x_Goddamn_-_Slowmotion_65947794.mp3'
            urllib.request.urlretrieve(url27, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Slowmotion.mp3')
            print('\n     Файл JOHAN x Goddamn - Slowmotion' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл JOHAN x Goddamn - Slowmotion'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path28 = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - Инферно 2.0.mp3')
        if path28.exists() == False:                           
            url28 = 'https://ruy.zvukofon.com/dl/1138471416/JOHAN_Goddamn_-_Inferno_20_(musportal.org).mp3'
            urllib.request.urlretrieve(url28, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Инферно 2.0.mp3')
            print('\n     Файл JOHAN x Goddamn - Инферно 2.0' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл JOHAN x Goddamn - Инферно 2.0'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path29 = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - Инсомния.mp3')
        if path29.exists() == False:                           
            url29 = 'https://ru.hitmotop.com/get/music/20190401/JOHAN_x_Goddamn_-_Insomniya_63214349.mp3'
            urllib.request.urlretrieve(url29, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Инсомния.mp3')
            print('\n     Файл JOHAN x Goddamn - Инсомния' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл JOHAN x Goddamn - Инсомния'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
      
        path30 = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - 1100.mp3')
        if path30.exists() == False:                           
            url30 = 'https://rum.muzikavsem.org/dl/1135735277/JOHAN_x_Goddamn_-_1100_(rum.muzikavsem.org).mp3'
            urllib.request.urlretrieve(url30, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - 1100.mp3')
            print('\n     Файл JOHAN x Goddamn - 1100' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл JOHAN x Goddamn - 1100'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path31 = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - Inferno.mp3')
        if path31.exists() == False:                           
            url31 = 'https://ru.hitmotop.com/get/music/20190427/JOHAN_x_Goddamn_-_Inferno_63783589.mp3'
            urllib.request.urlretrieve(url31, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Inferno.mp3')
            print('\n     Файл JOHAN x Goddamn - Inferno' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл JOHAN x Goddamn - Inferno'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path32 = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - Рецидив.mp3')
        if path32.exists() == False:                           
            url32 = 'https://ru.hitmotop.com/get/music/20190425/JOHAN_x_Goddamn_-_Recidiv_63734390.mp3'
            urllib.request.urlretrieve(url32, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Рецидив.mp3')
            print('\n     Файл JOHAN x Goddamn - Рецидив' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл JOHAN x Goddamn - Рецидив'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
       
        path33 = pathlib.Path('C:/Users/'+ user +'/'+k+'/JOHAN x Goddamn - Марианская впадина.mp3')
        if path33.exists() == False:                           
            url33 = 'https://ru.hitmotop.com/get/music/20200109/JOHAN_x_Goddamn_-_Marianskaya_vpadina_67911874.mp3'
            urllib.request.urlretrieve(url33, 'c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Марианская впадина.mp3')
            print('\n     Файл JOHAN x Goddamn - Марианская впадина' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл JOHAN x Goddamn - Марианская впадина'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path34 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Goddamn - Ногами вверх.mp3')
        if path34.exists() == False:                           
            url34 = 'https://ru.hitmotop.com/get/music/20210118/Goddamn_-_Nogami_vverkh_72361848.mp3'
            urllib.request.urlretrieve(url34, 'c:/Users/'+user+'/'+k+'/Goddamn - Ногами вверх.mp3')
            print('\n     Файл Goddamn - Ногами вверх' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Goddamn - Ногами вверх'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
            
        path35 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Disturbed - Stricken.mp3')
        if path35.exists() == False:                           
            url35 = 'https://ru.hitmotop.com/get/music/20170830/Disturbed_-_Stricken_47829348.mp3'
            urllib.request.urlretrieve(url35, 'c:/Users/'+user+'/'+k+'/Disturbed - Stricken.mp3')
            print('\n     Файл Disturbed - Stricken' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Disturbed - Stricken'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)       
        
        path36 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Disturbed - Open Your Eyes.mp3')
        if path36.exists() == False:                           
            url36 = 'https://ru.hitmotop.com/get/music/20170908/Disturbed_-_Open_Your_Eyes_48407460.mp3'
            urllib.request.urlretrieve(url36, 'c:/Users/'+user+'/'+k+'/Disturbed - Open Your Eyes.mp3')
            print('\n     Файл Disturbed - Open Your Eyes' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Disturbed - Open Your Eyes'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path37 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Агент.mp3')
        if path37.exists() == False:                           
            url37 = 'https://ru.hitmotop.com/get/music/20211205/Oxxxymiron_-_Agent_73431910.mp3'
            urllib.request.urlretrieve(url37, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Агент.mp3')
            print('\n     Файл Oxxxymiron - Агент' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Oxxxymiron - Агент'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path38 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - Мы все умрем.mp3')
        if path38.exists() == False:                           
            url38 = 'https://ru.hitmotop.com/get/music/20211205/Oxxxymiron_-_My_vse_umrem_73431914.mp3'
            urllib.request.urlretrieve(url38, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - Мы все умрем.mp3')
            print('\n     Файл Oxxxymiron - Мы все умрем' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Oxxxymiron - Мы все умрем'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
        
        path39 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Oxxxymiron - ОРГАНИЗАЦИЯ.mp3')
        if path39.exists() == False:                           
            url39 = 'https://ru.hitmotop.com/get/music/20211111/Oxxxymiron_-_ORGANIZACIYA_73302782.mp3'
            urllib.request.urlretrieve(url39, 'c:/Users/'+user+'/'+k+'/Oxxxymiron - ОРГАНИЗАЦИЯ.mp3')
            print('\n     Файл Oxxxymiron - ОРГАНИЗАЦИЯ' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Oxxxymiron - ОРГАНИЗАЦИЯ'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
            
        path40 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Alan Walker, Jamie Miller - Running Out of Roses.mp3')
        if path40.exists() == False:                           
            url40 = 'https://ru.hitmotop.com/get/music/20210910/Alan_Walker_Jamie_Miller_-_Running_Out_of_Roses_73156491.mp3'
            urllib.request.urlretrieve(url40, 'c:/Users/'+user+'/'+k+'/Alan Walker, Jamie Miller - Running Out of Roses.mp3')
            print('\n     Файл Alan Walker, Jamie Miller - Running Out of Roses' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Alan Walker, Jamie Miller - Running Out of Roses'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
            
        path41 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Alan Walker, Imanbek - Sweet Dreams.mp3')
        if path41.exists() == False:                           
            url41 = 'https://ru.hitmotop.com/get/music/20210611/Alan_Walker_Imanbek_-_Sweet_Dreams_72998823.mp3'
            urllib.request.urlretrieve(url41, 'c:/Users/'+user+'/'+k+'/Alan Walker, Imanbek - Sweet Dreams.mp3')
            print('\n     Файл Alan Walker, Imanbek - Sweet Dreams' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Alan Walker, Imanbek - Sweet Dreams'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
            
        path42 = pathlib.Path('C:/Users/'+ user +'/'+k+'/Alan Walker - Legends Never Die.mp3')
        if path42.exists() == False:                           
            url42 = 'https://ru.hitmotop.com/get/music/20180303/League_of_Legends_Alan_Walker_League_of_Legends_Alan_Walker_Again_-_Legends_Never_Die_54268252.mp3'
            urllib.request.urlretrieve(url42, 'c:/Users/'+user+'/'+k+'/Alan Walker - Legends Never Die.mp3')
            print('\n     Файл Alan Walker - Legends Never Die' + colorama.Fore.CYAN +  ' скачан\n'+ Style.RESET_ALL)
            time.sleep(0.5)
        else:
            print('\n     Файл Alan Walker - Legends Never Die'+colorama.Fore.YELLOW +' уже '+ Style.RESET_ALL +'скачан\n')
            time.sleep(0.5)
    elif h == 'нет':
        print('\n     Будет ошибка в открытии музыки (в хорошем случае, добавление музыки)')
        time.sleep(4)
        os.system('cls')
        
    
    else:
        print('     Вы ввели не то')
        time.sleep(3)
        os.system('cls')



while True:
    os.system('cls')
    print('\n\n')
    print(colorama.Fore.GREEN+'     ╔═══════════════════════════════════════════════════════════════════════╗')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   1. Really Slow Motion - Deadwood      0. Выход'+ Fore.GREEN+'                      ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   2. Slipknot - Duality '+Fore.GREEN+'                                              ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   3. Король и Шут - Прыгну со скалы '+Fore.GREEN+'                                  ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   4. Король и Шут - Кукла колдуна '+Fore.GREEN+'                                    ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   5. Король и Шут - Ром'+Fore.GREEN+'                                               ║')   
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   6. Король и Шут - Маска'+Fore.GREEN+'                                             ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   7. Slipknot - Before I Forget'+Fore.GREEN+'                                       ║')   
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   8. Slipknot - Psychosocial'+Fore.GREEN+'                                          ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   9. Slipknot - Unsainted'+Fore.GREEN+'                                             ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   10. Exile - Lost Control'+Fore.GREEN+'                                            ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   11. Exile - Tututu'+Fore.GREEN+'                                                  ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   12. Exile - Castle'+Fore.GREEN+'                                                  ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   13. Ghostemane - Fed Up'+Fore.GREEN+'                                             ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   14. AC_DC - War Machine'+Fore.GREEN+'                                             ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   15. AC_DC - Back In Black'+Fore.GREEN+'                                           ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   16. Oxxxymiron - Где нас нет'+Fore.GREEN+'                                        ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   17. Oxxxymiron - Больше Бена'+Fore.GREEN+'                                        ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   18. Oxxxymiron - Кем ты стал'+Fore.GREEN+'                                        ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   19. Oxxxymiron - В долгий путь (1 раунд 17ib)'+Fore.GREEN+'                       ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   20. Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib)'+Fore.GREEN+'  ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   21. Oxxxymiron - Дело нескольких минут'+Fore.GREEN+'                              ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   22. Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib)'+Fore.GREEN+'        ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   23. Oxxxymiron - Переплетено'+Fore.GREEN+'                                        ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   24. Oxxxymiron - Город под подошвой'+Fore.GREEN+'                                 ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   25. PORCHY, MAY WAVE, JEEMBO, LOQIEMEAN, THOMA OXYMIRON - KONSTRUKT'+Fore.GREEN+' ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   26. Oxxxymiron, Markul - Fata Morgana'+Fore.GREEN+'                               ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   27. JOHAN x Goddamn - Slowmotion'+Fore.GREEN+'                                    ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   28. JOHAN x Goddamn - Инферно 2.0'+Fore.GREEN+'                                   ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   29. JOHAN x Goddamn - Инсомния'+Fore.GREEN+'                                      ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   30. JOHAN x Goddamn - 1100'+Fore.GREEN+'                                          ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   31. JOHAN x Goddamn - Inferno'+Fore.GREEN+'                                       ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   32. JOHAN x Goddamn - Рецидив'+Fore.GREEN+'                                       ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   33. JOHAN x Goddamn - Марианская впадина'+Fore.GREEN+'                            ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   34. Goddamn - Ногами вверх'+Fore.GREEN+'                                          ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   35. Disturbed - Stricken'+Fore.GREEN+'                                            ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   36. Disturbed - Open Your Eyes'+Fore.GREEN+'                                      ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   37. Oxxxymiron - Агент'+Fore.GREEN+'                                              ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   38. Oxxxymiron - Мы все умрем'+Fore.GREEN+'                                       ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   39. Oxxxymiron - ОРГАНИЗАЦИЯ'+Fore.GREEN+'                                        ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   40. Alan Walker, Jamie Miller - Running Out of Roses'+Fore.GREEN+'                ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   41. Alan Walker, Imanbek - Sweet Dreams'+Fore.GREEN+'                             ║')   
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   42. Alan Walker - Legends Never Die'+Fore.GREEN+'                                 ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')   
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   43. '+Fore.GREEN+'                                           ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   44. '+Fore.GREEN+'                                           ║')   
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   45. '+Fore.GREEN+'                                           ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')   
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   46. '+Fore.GREEN+'                                           ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   47. '+Fore.GREEN+'                                           ║')   
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   48. '+Fore.GREEN+'                                           ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')   
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   49. '+Fore.GREEN+'                                           ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   50. '+Fore.GREEN+'                                           ║')   
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   51. '+Fore.GREEN+'                                           ║')
    print(colorama.Fore.GREEN+'     ╠═══════════════════════════════════════════════════════════════════════╣')   
    print(colorama.Fore.GREEN+'     ║'+Fore.WHITE+'   52. '+Fore.GREEN+'                                           ║')
    print(colorama.Fore.GREEN+'     ╚═══════════════════════════════════════════════════════════════════════╝')
    res()
    an = input('    Что открыть --> ')
    if an == '1':
        try:
            да()
            os.startfile('C:/Users/'+ user +'/'+k+'/Really Slow Motion - Deadwood.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)   
    if an == '2':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Slipknot - Duality.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '3':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Король и Шут - Прыгну со скалы.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '4':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Король и Шут - Кукла колдуна.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)      
    if an == '5':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Король и Шут - Ром.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '6':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Король и Шут - Маска.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '7':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Slipknot - Before I Forget.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '8':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Slipknot - Psychosocial.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '9':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Slipknot - Unsainted.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)    
    if an == '10':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Exile - Lost Control.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '11':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Exile - Tututu.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '12':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Exile - Castle.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '13':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Ghostemane - Fed Up.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '14':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/AC_DC - War Machine.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2) 
    if an == '15':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/AC_DC - Back In Black.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '16':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron - Где нас нет.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '17':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron - Больше Бена.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '18':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron - Кем ты стал.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '19':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron - В долгий путь (1 раунд 17ib).mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '20':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron, Самариддин Раджабов - Ветер перемен (2 раунд 17ib).mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '21':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron - Дело нескольких минут.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '22':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron - В книге всё было по-другому (4 раунд, 17ib).mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '23':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron - Переплетено.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '24':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron - Город под подошвой.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '25':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/PORCHY, MAY WAVE, JEEMBO, LOQIEMEAN, THOMAS MRAZ, TVETH, SOULOUD, MARKUL, OXYMIRON - KONSTRUKT.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '26':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron, Markul - Fata Morgana.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '27':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Slowmotion.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '28':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Инферно 2.0.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '29':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Инсомния.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '30':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - 1100.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2) 
    if an == '31':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Inferno.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '32':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Рецидив.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '33':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - Марианская впадина.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '34':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Goddamn - Ногами вверх.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '35':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Disturbed - Stricken.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '36':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Disturbed - Open Your Eyes.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '37':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron - Агент.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)     
    if an == '38':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron - Мы все умрем.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)        
    if an == '39':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Oxxxymiron - ОРГАНИЗАЦИЯ.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)    
    if an == '40':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Alan Walker, Jamie Miller - Running Out of Roses.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)  
    if an == '41':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/Alan Walker, Imanbek - Sweet Dreams.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '42':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/Alan Walker - Legends Never Die.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '43':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - 1100.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '44':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - 1100.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '45':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - 1100.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '46':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - 1100.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '47':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - 1100.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '48':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - 1100.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '49':
        try:
            да()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - 1100.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '50':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - 1100.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
    if an == '51':
        try:
            есть()
            os.startfile('c:/Users/'+user+'/'+k+'/JOHAN x Goddamn - 1100.mp3')
            os.system('cls')
        except FileNotFoundError:
            print('\n     Музыки в этой папки нет')
            time.sleep(2)
       
       
    if an == '0':
        os.system('cls')
        break