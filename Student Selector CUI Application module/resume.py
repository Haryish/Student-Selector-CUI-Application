#Document name: StudentSelectorMain.py
#Package name and number of files: Student Selector (3)
#Created by Haryish Elangumaran

import os

def ContinueSystem():
    key=input("Do you want to continue? (press any key if no): ")
    choice=["yes","Yes","YES","ok","OK"]
    for i in choice:
        if i==key:
            os.system('cls')
            return True
    else:
        return False

def directclear():
    if (os.name=='posix'):
        os.system('clear')
    else:
        os.system('cls')
    
