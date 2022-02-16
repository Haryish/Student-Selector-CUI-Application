#Document name: StudentSelectorMain.py
#Package name and number of files: Student Selector (3)
#Created by Haryish Elangumaran

i=1
key=True

def takenote():
    global key
    x=[]
    while(key==True):
        try:
            note=int(input())
        except:
            print('The roll number suffix you enter should be an integer')
            continue
        x.append(note)
        if (note==0):
            key=False
            x.remove(note)
    return x

def ptoa(l,int):
    full=list(range(1,int))
    for a in l:
        for b in full:
            if (a == b):
                full.remove(b)
    return full

def withprefix(prefix,a):
    if (prefix=='yes'):
        for x in a:
            if(x<10):
                print(" 18E200"+str(x), end=',')
            else:
                print(" 18E20"+str(x), end=',')
    else:
        for x in a:
            print(str(x), end=',')

def display(strength,p,a):
    print("ATTENDANCE REPORT".center(80))
    print("Number in roll: "+str(strength))
    print("Number of Presentees: "+str(len(p)))
    print("Number of absentees: "+str(len(a)))
    print("***********************************".center(80))
    prefix=input('Can we provide prefix to the roll numbers: ')
    print("ABSENTEES :-")
    withprefix(prefix,a)
    print(("\n"+(("--"*40).ljust(80)))*2+"\n")

def PresenteesToAbsenteesConverter(strength):
    presentees=takenote()
    print("PRESENTEES :-\n",presentees)
    absentees=ptoa(presentees,strength)
    print("***********************************".center(80))
    display(strength,presentees,absentees)

#Unit Test Cases
#PresenteesToAbsenteesConverter(5)

