#creating to-do list application 
'''
features
-add a task 
-view tasks
-mark task as done
-delete a task
-exit program 
'''
#nitialise an empty list to store tasks
tasks = []

#function to display menu options
def show_menu():
    print("\n--To Do list--")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
  
#function to view current tasks  
def view_tasks():
    if not tasks:
        print("No tasks yet")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✔️" if task["done"] else "✖️" #show checkmark if done
            print(f"{i}.[{status}]{task['task']}")
         
#function to add new task
def add_task():
    task_name = input("Enter Task: ")
    tasks.append({"task": task_name, "done": False}) #add task as not done
    print("Task Added")
    
#function to mark a task as done
def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        tasks[index]["done"] = True
        print("Marked as Done")
    except:
        print("Invalid input") #incase of invalid number or empty list
        
#function to delete a list        
def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to be deleted: ")) -1
        removed = tasks.pop(index) #remove task from list
        print(f"Deleted: {removed['task']}")
    except:
        print("invalid input")     
        
#main loop to run the app
while True:
    show_menu() #display menu options
    choice = input("Choose an option (1-5)")
    
    #perform an action based on user's choice 
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye") #exit the program 
        break
    else:
        print("invalid choice") #handle the wrong input
        
        
     