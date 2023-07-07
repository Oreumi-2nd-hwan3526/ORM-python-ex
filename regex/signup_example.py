import re
import sys
from datetime import date

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def password():
    password=""
    while True:
        print(f"{bcolors.OKBLUE}Please enter the password on following rules:")
        print("1. More than 8 characters")
        print("2. No character repetition")
        print("3. Including upper,lower alphabets, digit, special characters")
        print(f"4. No including space{bcolors.ENDC}")

        password=input()
        if not re.search(r".{8,}",password):
            print(f"{bcolors.WARNING}More than 8 characters{bcolors.ENDC}")
            continue
        if re.search(r"([^.])\1+",password):
            print(f"{bcolors.WARNING}No character repetition{bcolors.ENDC}")
            continue
        if not re.search(r"(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[*.!@$%^&(){}[\]:;<>,.?/~_+-=|\\])",password):
            print(f"{bcolors.WARNING}Including upper,lower alphabets, digit, special characters at least once{bcolors.ENDC}")
            continue
        if re.search(r"\s",password):
            print(f"{bcolors.WARNING}No including space{bcolors.ENDC}")
            continue
        else:
            break

    for i in range(3):
        print(f"{bcolors.OKBLUE}Please enter the password again for confirmation:{bcolors.ENDC}")
        if password==input():
            print(f"{bcolors.OKGREEN}Password confirmation success{bcolors.ENDC}")
            return
        else:
            print(f"{bcolors.WARNING}Password confirmation failed, try again{bcolors.ENDC}")
    
    print(f"{bcolors.FAIL}You failed three times of password confirmation. Process terminated{bcolors.ENDC}")
    sys.exit()

def ssn():
    while True:
        print(f"{bcolors.OKBLUE}Please enter the SSN:{bcolors.ENDC}")
        ssn=input()

        if re.fullmatch(r"\d{6}-\d{7}",ssn)==None:
            print(f"{bcolors.WARNING}Wrong SSN, try again{bcolors.ENDC}")
            continue

        if ssn[7]=="1" or ssn[7]=="3":
            print(f"{bcolors.OKGREEN}You are male member{bcolors.ENDC}")
        elif ssn[7]=="2" or ssn[7]=="4":
            print(f"{bcolors.OKGREEN}You are male member{bcolors.ENDC}")
        else:
            print(f"{bcolors.OKGREEN}You are foreigner member{bcolors.ENDC}")
        break

password()
ssn()
print(f"{bcolors.OKBLUE}Your sign-up date is",date.today(),f"{bcolors.ENDC}")