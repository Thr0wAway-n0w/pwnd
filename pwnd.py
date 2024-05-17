import os
import time
import requests
from colorama import Fore
from colorama import Back
from colorama import Style
from PIL import ImageEnhance
from termcolor import colored
from ascii_magic import AsciiArt
import hashlib
import subprocess

try:
    my_art = AsciiArt.from_url('https://i.postimg.cc/Jhbhr2hT/Screenshot-2024-04-21-at-05-13-59-e21459f8019688f030e3fd2ddf70830b-jpg-JPEG-Image-338-600-pixels.png')
except OSError as e:
    
    print(f'Could not load the image, server said: {e.code} {e.msg}')
my_art.to_terminal()

def ascii_banner():
    try:
        my_art = AsciiArt.from_url('https://i.postimg.cc/Jhbhr2hT/Screenshot-2024-04-21-at-05-13-59-e21459f8019688f030e3fd2ddf70830b-jpg-JPEG-Image-338-600-pixels.png')
    except OSError as e:
    
        print(f'Could not load the image, server said: {e.code} {e.msg}')
    my_art.to_terminal()

def what_now():
    print(colored("Where To?", 'red', attrs=['reverse', 'blink', 'bold']))
    time.sleep(.01)     
    print
    print(" ")
    print("\033[91m1)\033[0m Search Again\033[0m")
    print("\033[91m2) \033[31mGo To Hell\033[0m")
    choice = input("YOU CHOOSE: ")
    
    if choice == "1":
        clear_screen()
        ascii_banner()
        pwnd()
    if choice == "2":
        exit

def clear_screen():
    subprocess.run('clear' if os.name == 'posix' else 'cls')

def check_password(password):
    hashed_password = hashlib.sha1(password.encode()).hexdigest().upper()
    first_five_chars, tail = hashed_password[:5], hashed_password[5:]
    
    response = requests.get(f"https://api.pwnedpasswords.com/range/{first_five_chars}")
    hashes = (line.split(':') for line in response.text.splitlines())
    
    for h, count in hashes:
        if h == tail:
            return f"{password}: {Fore.GREEN}Oh no — pwned!{Style.RESET_ALL}"
    
    return f"{password}: Good news — no pwnage found!"
    
def remove_duplicates(results):
    unique_results = []
    seen = set()
    for result in results:
        if result not in seen:
            unique_results.append(result)
            seen.add(result)
    return unique_results    
    
def pwnd():
    print(colored("Pwned Password Checker", 'red', attrs=['reverse', 'blink', 'bold']))
    print("1) Check Single - Multiple Passwords")
    print("2) Check List of Passwords")    
    print("\033[91m3\033[0m) Run")
    choice = input("Select an option: ")
    
    if choice == '1':
        password = input("Enter password(s) to check (separate each one with a comma and a space): ")
        passwords = [pw.strip() for pw in password.split(',')]
        results = []
        for password in passwords:
            result = check_password(password)
            results.append(result)
            print(result)
        
        if "Oh no — pwned!" in results[0]:
            print("\nOptions:")
            print("1) Only view positive matches")
            print("2) Remove Duplicates")
            print("3) Go back")
            sub_choice = input("Select an option: ")
            if sub_choice == '1':
                clear_screen()
                for result in [r for r in results if "Oh no — pwned!" in r]:
                    print(result)
                    what_now()
            elif sub_choice == '2':
                clear_screen()
                unique_results = remove_duplicates([result for result in results if "Oh no — pwned!" in result])
                for result in unique_results:
                    print(result)
                    what_now()
            elif sub_choice == '3':
                clear_screen()
                ascii_banner()
                pwnd()
        else:
            print("\nAdditional Options:")
            print("1) Remove Duplicates")
            print("2) Go back")
            sub_choice = input("Select an option: ")
            if sub_choice == '1':
                clear_screen()
                unique_results = remove_duplicates(results)
                for result in unique_results:
                    print(result)
            elif sub_choice == '2':
                clear_screen()
                ascii_banner()
                pwnd()
            
    elif choice == '2':
        file_name = input("Enter file name: ")
        try:
            with open(file_name, "r") as file:
                passwords = file.read().splitlines()
        except FileNotFoundError:
            print("File not found.")
            pwnd()
        
        results = []
        for password in passwords:
            result = check_password(password)
            results.append(result)
            print(result)
        
        if "Oh no — pwned!" in results[0]:
            print("\nOptions:")
            print("1) Only view positive matches")
            print("2) Remove Duplicates")
            print("3) Go back")
            sub_choice = input("Select an option: ")
            if sub_choice == '1':
                clear_screen()
                for result in [r for r in results if "Oh no — pwned!" in r]:
                    print(result)
                while True:
                    confirm = input("Do you want to continue? (y/n): ")
                    if confirm.lower() == 'y':
                        clear_screen()
                        ascii_banner()
                        pwnd()
                    elif confirm.lower() == 'n':
                        exit
                    else:
                        print("\033[91m INVALID SELECTION.\033[0m")
                        clear_screen()
                        ascii_banner()
                        pwnd()
            elif sub_choice == '2':
                clear_screen()
                positive_results = [result for result in results if "Oh no — pwned!" in result]
                for result in positive_results:
                    print("\033[92m" + result + "\033[0m")
                while True:
                    confirm = input("Do you want to continue? (y/n): ")
                    if confirm.lower() == 'y':
                        clear_screen()
                        ascii_banner()
                        pwnd()
                    elif confirm.lower() == 'n':
                        exit
                    else:
                        print("Invalid input. Please enter y or n.")
            elif sub_choice == '3':
                clear_screen()
                ascii_banner()
                pwnd()
        else:
            print("\nOptions:")
            print("1) Only view positive matches")
            print("2) Remove Duplicates")
            print("3) Go back")
            sub_choice = input("Select an option: ")
            if sub_choice == '1':
                clear_screen()
                for result in [r for r in results if "Oh no — pwned!" in r]:
                    print(result)
                while True:
                    confirm = input("Do you want to continue? (y/n): ")
                    if confirm.lower() == 'y':
                        clear_screen()
                        ascii_banner()
                        pwnd()
                    elif confirm.lower() == 'n':
                        exit
                    else:
                        print("\033[91m INVALID SELECTION.\033[0m")
                        clear_screen()
                        ascii_banner()
                        pwnd()
            elif sub_choice == '2':
                clear_screen()
                positive_results = [result for result in results if "Oh no — pwned!" in result]
                for result in positive_results:
                    print("\033[92m" + result + "\033[0m")
                while True:
                    confirm = input("Do you want to continue? (y/n): ")
                    if confirm.lower() == 'y':
                        break
                    elif confirm.lower() == 'n':
                        exit
                    else:
                        print("Invalid input. Please enter y or n.")
            elif sub_choice == '3':
                clear_screen()
                ascii_banner()
                pwnd()
    elif choice == '3':
        print("Exiting...")
        clear_screen()
        ascii_banner()
        what_now()
    else:
        print("\033[91m INVALID SELECTION\033[0m")
        time.sleep(1)
        clear_screen()
        ascii_banner()
        pwnd()   
        
if __name__ == "__main__":
    pwnd()
