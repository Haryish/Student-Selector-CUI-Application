#Document name: StudentSelectorMain.py
#Package name and number of files: Student Selector (1)
#Created by Haryish Elangumaran

import resume
import PresentToAbsent


def Choice(a,b):
    print(("ATTENDANCE SELECTOR\n\nStrength: {}".format(b)).center(80))
    if(a==1):
        print("\nENTER YOUR PRESENTEES")
        PresentToAbsent.PresenteesToAbsenteesConverter(b)
    elif(a==2):
        print("\nENTER YOUR ABSENTEES")
        PresentToAbsent.PresenteesToAbsenteesConverter(b)
    elif(a==3):
        print("\nENTER YOUR ABSENTEES")
        Abs=PresentToAbsent.takenote()
        w=len(Abs)
        PresentToAbsent.display(b,PresentToAbsent.ptoa(Abs,v),Abs)
    else:
        print("Try Again later")
        
def main():        
    menus={
        1:"Presentees to Absentees Conversion",
        2:"Absentees to Presentees Conversion",
        3:"List of Absentees"
    }
    print("STUDENTS SELECTOR\n\n".center(80))
    strength=int(input("Enter the total number of students: "))
    print("\n\nSelect one of the following operations:\n".center(80))
    for x in range(1,4):
        print((str(x)+' '+menus[x]).center(80))
    typemenu=int(input("OPTION: "))
    resume.directclear()
    Choice(typemenu,strength)
        
while(PresentToAbsent.key==True):
        main()
        PresentToAbsent.key=resume.ContinueSystem()    

