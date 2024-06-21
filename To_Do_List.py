import sys, subprocess

tasks = {}
iterate = 1
while True:
    print("""
Menu:
1. Add new task
2. Mark task as done
3. Remove task
4. Show list of tasks
5. End
    """)
    a = int(input("Enter an option : "))
    if(a == 1):
        b = input("Enter the task to be added : ")
        tasks[str(iterate) + " " + b] = 0
        iterate += 1
    elif(a == 2):
        for i in tasks.items():
            print("☑" if(i[1] == 1) else "☐", i[0])
        comp = input("Enter the task number to mark as done : ")
        j = 1
        try:
            for i in tasks.items():
                if(i[0][0] == comp):
                    tasks[i[0]] = 1
                j += 1

        except:
            pass
        for i in tasks.items():
            print("☑" if (i[1] == 1) else "☐", i[0])
    elif(a == 3):
        tasknum = input("Enter the task number : ")
        j = 1
        try:
            for i in tasks.items():
                if(i[0][0] == tasknum):
                    del tasks[i[0]]
        except:
            pass
    elif(a == 4):
        for i in tasks.items():
            print("☑" if (i[1] == 1) else "☐", i[0])
    elif(a == 5):
        break
    else:
        print("Invalid option")