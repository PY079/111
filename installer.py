import os, time
os.system('clear')




print ('\n')

while True:
    print('\n\n')
    print(" #                 #          ##    ##              ")
    print ("                   #           #     #              ")
    print ("##   ###    ###   ###    ###   #     #     ##   ### ")
    print (" #   #  #  ##      #    #  #   #     #    # ##  #  #")
    print (" #   #  #    ##    #    # ##   #     #    ##    #   ")
    print ("###  #  #  ###      ##   # #  ###   ###    ##   #   ")
    print ('\n')
    print ("    [by @SYPEXHACK]                            [v1.0]")
    time.sleep(2)
    print ('\n\n')
    print ("    [1] ngrok")
    print ("    [2] фишинг")
    print ("    [3] брутфорс <Instagram>")
    print ("    [4] заблокировать Termux <!!ОПАСНО!!>")
    print ("    [5] просмотр камер <98 стран>")
    print ("\n")
    print ("    [6] обновить")
    print ("    [0] выход")
    print ("\n\n")
    inp = input ('  Выбери пункт>>>  ')
    os.system('clear')
    
    if inp == '1':    
        os.system('cd $HOME')
        os.system('git clone https://github.com/tchelospy/termux-ngrok.git')
        time.sleep(8)
        os.system('cd termux-ngrok')
        os.system('chmod +x termux-ngrok.sh')
        os.system('./termux-ngrok.sh')
        os.system('clear')
    

    if inp == '6':    
        os.system('git clone https://github.com/777-FOXik-777/installer')
        time.sleep(3)
        os.system('cd installer')
        os.system('python3 installer.py')
        os.system('clear')
        
    if inp == '0':
        os.system('clear')
        break
        
    if inp < '0':
        os.system('clear')
        pass
    if inp > '6':
        os.system('clear')
        pass
        
