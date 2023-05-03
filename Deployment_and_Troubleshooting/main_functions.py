import subprocess
import os
import keyboard
import nmap
import time
import sys

"""This script is where all the main functions for the deployment_and_troubleshooting_tool are stored. Any changes that need to be made to imported in DATT should be made here.
Be sure and read the ream_me for this tool, as all the features and syntax for using each are explained in great detail. It can be found on GitHub, or if you naviate to the resources
directory, there is a copy there."""

#############################################################################################################################################################################################################################################################################################################################################################################################
"""Functions that will used through out the program, but are not part of the menu options. These are hidden to the end user."""

# Main functions used in DATT.
def clean():
    os.system('cls' if os.name=='nt' else 'clear')

def did_a_thing():
    print("Tots did the stuff and things...\U0001F600\U0001F600")
    time_for_a_break()
    clean()

#def user_ping(ping):  #Testing if I need this function on the script. Will remove in later version if it is not used.
#    command = subprocess.run(["ping", "-n", "2", ip] if os.name=='nt' else ["ping", "-t", "2", ip])

def time_for_a_break():
    time.sleep(5)

def welcome_message():
    print("##############################################################################################################################################")
    print("Welcome to DAT_Tool! Good luck, and don't break anything :D (or if you do, fix before anyone notices...\U0001F600)")
    print("Pressing 0 at any menu will return you to the last menu. Pressing 00 at any menu will you quit the program.")
    print("##############################################################################################################################################")

def file_directory():
    global ping_folder
    main_folder = "/home/linux-user/gitmaster/DAT_Tool/Resources"
    os.makedirs(main_folder, exist_ok=True)

    ip_list_folder = os.path.join(main_folder, "dat_tool_resources")
    os.makedirs(ip_list_folder, exist_ok=True)

    ping_folder = os.path.join(main_folder, "ping")
    os.makedirs(ping_folder, exist_ok=True) 

    nmap_folder = os.path.join(main_folder, "nmap_scan") 
    os.makedirs(nmap_folder, exist_ok=True)

    traceroute_folder = os.path.join(main_folder, "traceroute")
    os.makedirs(traceroute_folder, exist_ok=True)

    did_a_thing()

def exit_program():
    print("Quitting the program!")
    sys.exit()

def feature_not_added():
    print("feature coming soon....... \U0001f600")
    print("Check back soon, or make sure that a fresh Git Pull has been done, as this may have been added recently.")
    time_for_a_break()
    clean()

def update_script(): #Not needed any longer, now that start_DAT_tool.py has been created, tested and pushed out to the deployment_and_troubleshooting_tool.py Git repo.
    subprocess.run(["git", "pull"])
    time.sleep(2)
    clean()
#############################################################################################################################################################################################################################################################################################################################################################################################
"""Start of the (main and sub) menu functions"""

# deployment_and_troubleshooting_tool set-up menu function (option 1 from main menu in DATT).
def set_up_menu():
    file_directory()

# deployment_and_troubleshooting_tool.py ping menu function (option 2 from main menu in DATT).
def ping_menu():
    clean()
    while True:
        ping_menu_selection = input("Do you wish to enter IP(s):\n1.Manually\n2.Select from txt file\n3.Clear screen\n4.Back to main menu\n5.Exit\nEnter Selection:")
        if ping_menu_selection.strip() == "1" or ping_menu_selection.lower() == "manually":
            ping_menu_manual()
        elif ping_menu_selection.strip() == "2" or ping_menu_selection.lower() == "select from txt file":
            ping_menu_from_txt()
        elif ping_menu_selection.strip() == "3" or ping_menu_selection.lower() == "clear screen" or ping_menu_selection == "clear":
            clean()
        elif ping_menu_selection.strip() == "4" or ping_menu_selection.lower() == "back to main menu" or ping_menu_selection == "back":
            break
        elif ping_menu_selection.strip() == "5" or ping_menu_selection.lower() == "quit":
            exit_program()
        else:
            print("Not a valid selction, plesae try again!")

# Sub-menu of ping_menu in deployment_and_troubleshooting_tool.py
def ping_menu_manual():
    while True:
        print("\n*****Seperate IP(s) addresses by commas.*****")
        user_ip = input("Enter IP(s) to be scanned:")
        user_ip_list = [ip.strip() for ip in user_ip.split(',')]
        if user_ip.strip() == "0":
            break
        elif user_ip.strip() == "00":
            exit_program()
        elif len(user_ip_list) == 1:
            ping = subprocess.run(["ping", "-c", "2", user_ip_list[0]], capture_output=True, text=True)
            if "Request timeout for icmp_seq 0" in ping.stdout or "100% packet loss" in ping.stdout:
                print(f"{user_ip_list[0]} is down")
            elif "2 packets transmitted, 2 received, 0% packet loss" in ping.stdout:
                print(f"{user_ip_list[0]} is up")
            else:
               print(f"{user_ip_list[0]} is up")
        elif len(user_ip_list) > 1:
                    for ip in user_ip_list:
                        ping = subprocess.run(["ping", "-c", "2", ip], capture_output=True, text=True)
                        if "Request timeout for icmp_seq 0" or "Request timed out" in ping.stdout:
                            print(f"{ip} is down")
                        else:
                            print(f"{ip} is up")

# Sub-menu of ping_menu in deployment_and_troubleshooting_tool.py
def ping_menu_from_txt():
    file_directory()
    while True:
        # Makes sure the actions in the list section are ran against the right directory
        os.chdir(ping_folder)
        # Set the directory path to scan for files
        directory = "/home/linux-user/gitmaster/DAT_Tool/Resources/ping"
        # Lists the files in the directory that will import for the ping test
        files = os.listdir(directory)
        print("\nSelect a file:") #May not be needed, seems to be a duplicate of the next print statement. Needs testing.
        for i, file in enumerate(directory):
            print(f"{i+1}: {file}")
        # Prompts the user to select a file
        selection = input("Select a file to open (press 0 to go back)\nSelection:")
        if selection.strip() == "0":
            break
        elif selection.strip() == "00":
            exit_program()
        # Gets the selected file path
        file_path = os.path.join(directory, files[int(selection)-1])
        # Opens the file and reads the contents
        with open(file_path, "r") as file:
            contents = [line.strip() for line in file]
            if contents == " ":
                print("File is empty, please select a valid file")
                break
            else:
                for ip in contents:
                    ping = subprocess.run(["ping", "-c", "2", ip], capture_output=True, text=True)
                    if "100% packet loss" in ping.stdout:
                        print(f"{ip} is down")
                    elif "2 packets transmitted, 2 receieved, 0% packet loss" in ping.stdout:
                        print(f"{ip} is up")

