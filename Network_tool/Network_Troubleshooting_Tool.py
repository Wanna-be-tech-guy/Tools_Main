import subprocess
import os
import keyboard
import nmap

#############################################################################################################################################################################################################################################################################################################################################################################################
# Make sure you have read and understand the Read_Me. All of the aspects of the program have been explained in great detail there.
# Leave feedback on my GitHub :-)
#############################################################################################################################################################################################################################################################################################################################################################################################
""" Section 1. """
# Function built to clear the terminal or cmd, since it gets pretty filled up, quickly. (Not used, I repalced this with clean function, but this can be implemented easily is the user so chooses it.)
def clean_input(prompt):
    os.system('cls' if os.name=='nt' else 'clear')
    user_input = input(prompt)
    return user_input

# Function added for the user to manually clear the screen with a hotkey (Not used as of v1..0)
def clear_screen(prompt):
    os.system('cls' if os.name=='nt' else 'clear')
    keyboard.add_hotkey = ('shift+1', clear_screen)
    keyboard.wait()

# Added this function to give the user the option of clearing the CMD or Terminal within in each menu. 
def clean():
    os.system('cls' if os.name=='nt' else 'clear')

# Function to run the basic ping command across Unix or Windows operating systems. (Not ussed as of v1.0)
def user_ping(ping):
    command = subprocess.run(["ping" , "-n" , "2", ip] if os.name=='nt' else ["ping", "-t", "2", ip])

# Clears the screen at the start of the program.
clean()

#############################################################################################################################################################################################################################################################################################################################################################################################
"""Section 2."""
# Create the main folder and subfolders in a specific directory
main_folder = "/home/linux-user/gitmaster/Network_Troubleshooting_Tool"
os.makedirs(main_folder, exist_ok=True)

ip_list_folder = os.path.join(main_folder, "resources")
os.makedirs(ip_list_folder, exist_ok=True)

ping_folder = os.path.join(main_folder, "Ping")
os.makedirs(ping_folder, exist_ok=True) 

nmap_folder = os.path.join(main_folder, "NMAP") 
os.makedirs(nmap_folder, exist_ok=True)

traceroute_folder = os.path.join(main_folder, "Traceroute")
os.makedirs(traceroute_folder, exist_ok=True)

#############################################################################################################################################################################################################################################################################################################################################################################################

# Welcome message to user(s).
print("##############################################################################################################################################")
print("Welcome to the  Network Troubleshooting tool! Good luck, and don't break anything :D (or if you do, fix before anyone notices...\U0001F600")
print("Press shift+F1 to clear screen. Pressing 00 at any menu will exit the program. Pressing 0 at any menu will you return you to the main menu.\n")

#############################################################################################################################################################################################################################################################################################################################################################################################
"""Section 3."""
# Start of the main while loop.
while True:
    menu_selection = input("Menu options\n1.Ping\n2.NMAP scan.\n3.Traceroute.\n4.Manage Resources\n5.Clear terminal\n0.Exit\nEnter selection:")    
#############################################################################################################################################################################################################################################################################################################################################################################################
    if menu_selection.strip() == "1" or menu_selection.lower() == "ping":
        clean()
        while True:
            ping_menu_selection = input("Do you wish to enter addresses to ping:\n1.Manually\n2.Select from txt file\n3.Clear screen\n0.Back to main menu\nEnter Selection: ")
#############################################################################################################################################################################################################################################################################################################################################################################################
            if ping_menu_selection.strip() == "1" or ping_menu_selection.lower() == "manually":
                print("\n\n***Seperate IP addresses by commas.***")
                user_ip = input("Enter IP(s) to be scanned: ")
                user_ip_list = [ip.strip() for ip in user_ip.split(',')]
                if len(user_ip_list) == 1:
                        ping = subprocess.run(["ping", "-c", "2", user_ip_list[0]], capture_output=True, text=True)
                        if "Request timeout for icmp_seq 0" or "Request timed out" or "2 packets transmitted, 0 received, 100% packet loss" in ping.stdout:
                            print(f"{user_ip_list[0]} is down")
                        else:
                           print(f"{user_ip_list[0]} is up")
                
                elif len(user_ip_list) > 1:
                    for ip in user_ip_list:
                        ping = subprocess.run(["ping", "-c", "2", ip], capture_output=True, text=True)
                        if "Request timeout for icmp_seq 0" or "Request timed out" in ping.stdout:
                            print(f"{ip} is down")
                        else:
                           print(f"{ip} is up")
                elif user_ip.strip() == "0":
                    break
                elif user_ip_list.strip() == "00":
                    print("Quitting program")
                    quit()
                else:
                    break
#############################################################################################################################################################################################################################################################################################################################################################################################
            elif ping_menu_selection.strip() == "2" or ping_menu_selection.lower() == "Select from txt file":
                while True:
                    #Makes sure that the following actions are ran against the correct directory
                    os.chdir(ping_folder)   
                    # Set the directory path to scan for files
                    directory = "/home/linux-user/gitmaster/Network_Troubleshooting_Tool/Ping"    
                    # Lists the files in the directory that will be imported into the NMAP scan
                    files = os.listdir(directory) 
                    print("\nSelect a file:")
                    for i, file in enumerate(files):
                            print(f"{i+1}: {file}") 
                    # Prompts the user to select a file    
                    selection = input("Select the file to open, press 0 to go back: ")
                    if selection.strip() == "0": # Takes the user back to the main menu
                        break
                    elif selection.strip() == "00":
                        print("Quitting program.")
                        quit()
                    # Get the selected file path
                    file_path = os.path.join(directory, files[int(selection)-1])
                    # Open file and read its content
                    with open(file_path, "r") as file:
                        contents = [line.strip() for line in file]
                        if contents == " ":
                            print("File is enmpty, please select a new file")
                            break
                        else:
                            for ip in contents:
                                ping = subprocess.run(["ping", "-n", "2", ip], capture_output=True, text=True)
                                if "Request timeout for icmp_seq 0" or "Request timed out" in ping.stdout:
                                    print(f"{ip} is down")
                                elif "Sent = 2"in ping.stdout:
                                   print(f"{ip} is up")
#############################################################################################################################################################################################################################################################################################################################################################################################
            elif ping_menu_selection.strip() == "3" or ping_menu_selection.lower() == "clear":
                clean()
#############################################################################################################################################################################################################################################################################################################################################################################################
            elif ping_menu_selection.strip() == "0" or ping_menu_selection.lower() == "exit":
                break
#############################################################################################################################################################################################################################################################################################################################################################################################
            elif ping_menu_selection.strip() == "00":
                print("Quiting program")
                quit()
#############################################################################################################################################################################################################################################################################################################################################################################################
    elif menu_selection.strip() == "2" or menu_selection.lower() == "nmap" or menu_selection.lower == "nmap scan":
        clean()
        while True:
            nmap_menu_selction = input("\n\nSelect from the following:\n1.Manually scan IP range\n2.Scan from txt file\n3.Clear\n0.Return to main menu\nEnter Selection:")
#############################################################################################################################################################################################################################################################################################################################################################################################
            if nmap_menu_selction.strip() == "1" or nmap_menu_selction.lower() == "manual" or nmap_menu_selction.lower() == "manual scan ip range" or nmap_menu_selction == "scan":
                print("Work in progress")
#############################################################################################################################################################################################################################################################################################################################################################################################
            elif nmap_menu_selction == "2" or nmap_menu_selction == "scan from txt file" or nmap_menu_selction == "scan" or nmap_menu_selction == "txt":
                os.chdir(nmap_folder) #Makes sure that the following actions are ran against the correct directory
                directory = r"C:\Users\andy1\Networking_Troubleshooting_Tool\NMAP" # Set the directory path to scan for files

                # Lists the files in the directory that will be imported into the NMAP scan
                files = os.listdir(directory) 
                print("\nSelect a file:")
                for i, file in enumerate(files):
                    print(f"{i+1}: {file}")

                # Prompts the user to select a file    
                selection = input("Enter the number of the file to open, press 0 to go back: ")
                if selection.strip() == "0": # Takes the user back to the main menu
                    break
                # Get the selected file path
                file_path = os.path.join(directory, files[int(selection)-1])

                # Open file and read its content
                with open(file_path, "r") as file:
                    contents = file.read()
                    print("hostname | ", contents)
#############################################################################################################################################################################################################################################################################################################################################################################################
            elif nmap_menu_selction == "3" or nmap_menu_selction == "clear":
                clean()
#############################################################################################################################################################################################################################################################################################################################################################################################
            elif nmap_menu_selction == "0" or nmap_menu_selction == "back":
                break
#############################################################################################################################################################################################################################################################################################################################################################################################
            elif nmap_menu_selction == "00":
                quit()
#############################################################################################################################################################################################################################################################################################################################################################################################
            else:
                print("Not a valid option. Please another selction.")
#############################################################################################################################################################################################################################################################################################################################################################################################
    elif menu_selection.strip() == "3" or menu_selection.lower() == "traceroute":
        clean()
        while True:
            traceroute_menu_selection = input("Select from the following:\n1.Maually Selection\n2.Select from txt file\n3.Clear\n0.Exit\nEnter Selection:")
            if traceroute_menu_selection.strip() == "1" or traceroute_menu_selection.lower() == "manual":
                traceroute_manual_selection = input("Enter IP to ran traceroute against: ")
                print(traceroute_manual_selection)
#############################################################################################################################################################################################################################################################################################################################################################################################
            elif traceroute_menu_selection.strip() == "2" or traceroute_menu_selection.lower() == "select" or traceroute_menu_selection.lower() == "txt" or traceroute_menu_selection.lower() == "select from txt file":
                os.chdir(traceroute_folder) #Makes sure that the following actions are ran against the correct directory
                directory = r"C:\Users\andy1\Networking_Troubleshooting_Tool\Traceroute" # Set the directory path to scan for files

                # Lists the files in the directory that will be imported into the NMAP scan
                files = os.listdir(directory) 
                print("\nSelect a file:")
                for i, file in enumerate(files):
                    print(f"{i+1}: {file}")

                # Prompts the user to select a file    
                selection = input("Enter the number of the file to open, press 0 to go back: ")
                if selection.strip() == "0": # Takes the user back to the main menu
                    break
                # Get the selected file path
                file_path = os.path.join(directory, files[int(selection)-1])

                # Open file and read its content
                with open(file_path, "r") as file:
                    contents = file.read()
                    print(contents)
#############################################################################################################################################################################################################################################################################################################################################################################################
            elif traceroute_menu_selection.strip() == "3" or traceroute_menu_selection.lower() == "clear":
                clean()
#############################################################################################################################################################################################################################################################################################################################################################################################
            elif traceroute_menu_selection.strip() == "0" or traceroute_menu_selection.lower() == "exit":
                break
#############################################################################################################################################################################################################################################################################################################################################################################################
            elif traceroute_menu_selection.strip() == "00" or traceroute_menu_selection.lower() == "quit":
                print("Quitting the program.")
                quit()
#############################################################################################################################################################################################################################################################################################################################################################################################
    elif menu_selection.strip() =="4" or menu_selection.lower() == "manage" or menu_selection.lower() == "manage resources":
        print("Working on it")
#############################################################################################################################################################################################################################################################################################################################################################################################      
    elif menu_selection.strip() =="5" or menu_selection.lower() == "clear":
        clean()
#############################################################################################################################################################################################################################################################################################################################################################################################
    elif menu_selection.strip() == "0" or menu_selection.lower() == "exit":
        print("\nClosing program. Came back soon!")
        quit()
#############################################################################################################################################################################################################################################################################################################################################################################################
    else:
        print("Not a valid selection, please try again.")
#############################################################################################################################################################################################################################################################################################################################################################################################