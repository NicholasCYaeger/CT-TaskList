task_list = []

def add_task():
    new_task = str(input("Please type the new task, or input no characters to skip: "))
    new_task = new_task.strip()
    if new_task != "":
        task_list.append(new_task)
        print(f"Task added: {new_task}")

def view_tasks():
    if len(task_list) < 1:
        print("There are no current tasks.")
        return
    current_task_string = "Current tasks"
    print("/" + "-"*(len(current_task_string)+2) + "\\")
    print("| " + current_task_string + " |")
    print("\\" + "-"*(len(current_task_string)+2) + "/")
    for i in range(len(task_list)):
        print("{0}: {1}".format(i+1, task_list[i]))

def delete_task():
    if len(task_list) < 1:
        print("There are no current tasks.")
        return
    delete_method = -1
    while delete_method < 0 or delete_method > 2:
        try:
            delete_task_string = "0: Cancel deletion, 1: Delete by number, 2: Delete by text"
            print("/" + "-"*(len(delete_task_string)+2) + "\\")
            print("| " + delete_task_string + " |")
            print("\\" + "-"*(len(delete_task_string)+2) + "/")
            delete_method = int(input("Choose deletion method: "))
            if delete_method < 1 or delete_method > 4:
                print("Please choose an available option.")
        except ValueError:
            print("Please choose the number by an available option.")
        if delete_method == 0:
            return
        elif delete_method == 1:
            delete_task_by_place()
        elif delete_method == 2:
            delete_task_by_text()


def delete_task_by_place():
    view_tasks()
    index = -1
    while index < 0 or index > len(task_list):
        try:
            index = int(input("Choose task to delete by number, or input \'0\' to skip: "))
            if index < 1 or index > 4:
                print("Please choose an available option.")
        except ValueError:
            print("Please choose the number by an available option.")
        except:
            print("_ERROR")
    if index == 0:
        return
    elif index > 0 and index < len(task_list):
        del task_list[index - 1]

def delete_task_by_text():
    view_tasks()
    task_to_remove = ""
    while not (task_to_remove in task_list or task_to_remove == ""):
        task_to_remove = str(input("Type task to remove, or leave blank to cancel: "))
        task_to_remove = task_to_remove.strip()
        if task_to_remove == "":
            return
        elif task_to_remove in task_list:
            task_list.remove(task_to_remove)
        else:
            print("There is no task by that name.")

def quit_application():
    continue_application = False
    print("Ending application. Goodbye")

def run_application():
    task_list = []
    print("Welcome to the To-Do list")
    while(display_options()):
        pass

def display_options():
    option_choice = -1
    while option_choice < 1 or option_choice > 4:
        option_string = "1: Add Task, 2: View Tasks, 3: Delete Task, 4: Quit Application"
        print("/" + "-"*(len(option_string)+2) + "\\")
        print("| " + option_string + " |")
        print("\\" + "-"*(len(option_string)+2) + "/")
        try:
            option_choice = int(input("Your choice?: "))
            if option_choice < 1 or option_choice > 4:
                print("Please choose an available option.")
        except ValueError:
            print("Please choose the number by an available option.")
        except:
            print("_ERROR")
    return execute_option(option_choice)

def execute_option(option_choice):
    if option_choice == 1:
        add_task()
        return True
    elif option_choice == 2:
        view_tasks()
        return True
    elif option_choice == 3:
        delete_task()
        return True
    elif option_choice == 4:
        quit_application()
        return False

if __name__ == "__main__":
    run_application()
