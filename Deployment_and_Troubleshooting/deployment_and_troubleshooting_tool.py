from main_functions import *

clean()

welcome_message()

while True:
    menu_selction = input("Menu Options:\n1.Set-up (Should only need ran once, or on a new instance)\n2.Ping\n3.NMAP scan(s)\n4.TraceRoute\n5.Manage Resources\n6.Clear screen\n00.Exit\nEnter selection: ")
    if menu_selction.strip() == "1" or menu_selction.lower() == "set-up" or menu_selction.lower() == "set up":
        set_up_menu()
    elif menu_selction.strip() == "2" or menu_selction.lower() == "ping":
        ping_menu()
    elif menu_selction.strip() == "3" or menu_selction.lower() == "nmap":
        feature_not_added()
    elif menu_selction.strip() == "4" or menu_selction.lower() == "traceroute":
        feature_not_added()
    elif menu_selction.strip() == "5" or menu_selction.lower() == "manage" or menu_selction.lower() == "manage resources":
        feature_not_added()
    elif menu_selction.strip() == "6" or menu_selction.lower() == "clear":
        clean()
    elif menu_selction.strip() == "00" or menu_selction.lower() == "exit":
        exit_program()
    else:
        print("Not a valid selection, please try again.")
        time.sleep(2)
        clean()