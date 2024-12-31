from os import system
from keyboard import hook,wait
from progressbar import ProgressBar
from time import sleep


def key_event(e):
    if e.event_type == 'down':
        if e.name == '1':
            system("cls")
            print("starting ...\n\n")
            p = ProgressBar()
            for i in p(range(100)):
                sleep(0.1)
            system("cls")
            print("Welcome to the system")
            # 我只要我可以运行！！！！！   你们自己看着办吧（~'')~      --->---\\
            system("python ./V1/V1.2/files/startup.py")#<--------<---------/
        
        elif e.name == '2':
            system("cls")
            print("#            BIOS----------MY-SYSTEM-V1.2            #")
            print('/----------------------------------------------------\\')
            print('| 4.show my GitHub                                   |')
            print('| 5.show my Email                                    |')
            print('\\----------------------------------------------------/')
            a = input("Please enter a number:")
            if a == '4':                                     # Dear!!!          
                print("https://github.com/huluobuo")
            elif a == '5':
                print("HelloHuHi@outlook.com")
            else:
                print("Error ---- Please enter 4 or 5")
            print("Now,you can press 3 to exit")
        
        elif e.name == '3':
            system("cls")
            print("Goodbye\n\n\tPlese press Ctrl+C to exit")
            exit()                 #WHY?????????????????????????????


def main():
    with open("./V1/V1.2/files/text.txt", "r", encoding='utf-8') as f:
        print(f.read())
    print('Bios is loading...')
    sleep(3)
    system("cls")
    print("Welcome to the BIOS")
    print("Press 1 to enter the system")
    print("Press 2 to enter the BIOS")
    print("Press 3 to exit")
    hook(key_event)
    wait()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()