import os
exit_flag = 0
#Getting started


def add_task():
    os.system('clear')
    task = {}
    task["desc"] = input("enter description: ")
    task["due_date"] = input("enter due_date: ")
    task["assignee"] = input("enter assignee: ")
    task["status"] = input("enter status: ")

    task_string = ';'.join(task.values())
    print(task_string)
    f = open("tasks.txt", "a")
    f.write(task_string)
    f.close()
    return

def show_task(task):
    print("description: ", task["desc"])
    print("due date: ", task["due_date"])
    print("assignee: ", task["assignee"])
    print("status: ", task["status"])
    return

def show_tasks_list():
    f = open("tasks.txt", "r")
    for x in f:
      print(x)


while exit_flag == 0:
    print(" operations:\n 1: add task \n 2: show tasks \n 3: assign task to user \n 4: mark as done \n press 5 to exit")
    option = int(input("Enter your operation: "))
    if option == 1:
        add_task()
    elif option == 2:
        show_tasks_list()
        # dict = {"desc": input("enter the desk "), "due_date": input("enter the desk "),
        #         "assignee": input("enter the desk "), "status": input("enter the desk ")}
    elif option == 3:
        dict = {"assignee": input("enter the asignee: ")}
    elif option == 4:
        dict = { "status": input("enter the stutus: ")}
    elif option == 5:
        print("thanks for using our program")
        exit_flag = 1

task1 = {"desc" : "buy_something " , "due date" : "1/7/2020" , "assignee" : "abdalla" , "stutus" : "pending" }
v = task1.values()
s = ';'.join(v)
print(s)
# show_task(task1)