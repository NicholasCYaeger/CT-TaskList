option_letters = ["A", "V", "D", "C", "Q"]
list_filename = "to_do_list.dat"
main_task_list = []

def add_task():
    """Add a task to the task list."""
    new_task = str(input("Please type the new task, or input no characters to skip: "))
    new_task = new_task.strip()
    if new_task != "":
        main_task_list.append(new_task)
        write_list_to_file()
        print(f"Task added: {new_task}")

def view_tasks():
    '''View a list of all tasks, or inform user that the task list is empty.'''
    if len(main_task_list) < 1:
        print("There are no tasks on the list.")
        return
    current_task_string = "Current tasks"
    print("\n/" + "-"*(len(current_task_string)+2) + "\\")
    print("| " + current_task_string + " |")
    print("\\" + "-"*(len(current_task_string)+2) + "/")
    for i in range(len(main_task_list)):
        print("{0}: {1}".format(i+1, main_task_list[i]))

def delete_task():
    '''Decide whether to delete a task by list position or by the text'''
    if len(main_task_list) < 1:
        print("There are no tasks on the list.")
        return
    delete_method = -1
    while delete_method < 0 or delete_method > 2:
        try:
            delete_task_string = "0: Cancel deletion, 1: Delete by number, 2: Delete by text"
            print("\n/" + "-" * (len(delete_task_string) + 2) + "\\")
            print("| " + delete_task_string + " |")
            print("\\" + "-"*(len(delete_task_string)+2) + "/")
            delete_method = int(input("Choose deletion method: "))
            if delete_method < 0 or delete_method > 2:
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
    '''Delete a task by place on the list'''
    view_tasks()
    index = -1
    while index < 0 or index > len(main_task_list):
        try:
            index = int(input("Choose task to delete by number, or input \'0\' to skip: "))
            if index < 0 or index > len(main_task_list):
                print("Please choose an available option.")
        except ValueError:
            print("Please choose the number by an available option.")
        except:
            print("_ERROR")
    if index == 0:
        print("No task deleted")
        return
    elif index > 0 and index <= len(main_task_list):
        deleted_task = main_task_list[index - 1]
        del main_task_list[index - 1]
        write_list_to_file()
        print(f"Deleted task #{index}: {deleted_task}")

def delete_task_by_text():
    '''Delete task by task name'''
    view_tasks()
    task_to_remove = ""
    while True:         #leave task by return
        task_to_remove = str(input("Type task to remove, or leave blank to cancel: "))
        task_to_remove = task_to_remove.strip()
        if task_to_remove == "":
            print("No task deleted")
            return
        elif task_to_remove in main_task_list:
            main_task_list.remove(task_to_remove)
            print(f"Deleted task: {task_to_remove}")
            write_list_to_file()
            return
        else:
            print("There is no task by that name.")
            
def clear_list():
    '''Ask to delete the entire list'''
    print("WARNING: This deletes the entire list.")
    delete_agree = str(input("Do you want to delete all entries in the list (if you do, type ""Yes""): "))
    if delete_agree.upper() == "YES":
        print("Deleting task list.")
        main_task_list.clear()
        write_list_to_file()
    else:
        print("Deleting task list cancelled.")
        
def write_list_to_file():
    '''Write the task list to a file'''
    write_file = open(list_filename, "w")
    text_to_write = ""
    for task in main_task_list:
        if text_to_write == "":
            text_to_write = task
        else:
            text_to_write += "\n{}".format(task)
    write_file.write(text_to_write)
    write_file.close()

def read_list_from_file():
    '''Read the task list from a file, if it can.'''
    try:
        read_file = open(list_filename, "r")
        read_file_content = read_file.read()
        print("Read task list from file.")
        return read_file_content.split("\n")
    except:
        print("No task list: Starting new list")
        return []
    pass

def quit_application():
    '''Quit the application.'''
    print("Ending application. Goodbye")

def run_application():
    '''Run the application.'''
    print("Welcome to the To-Do list")
    main_task_list.clear()
    main_task_list.extend(read_list_from_file())
    while(display_options()):
        pass

def display_options():
    '''Display all options, and let the user select an option. Return true if continuing, or false if ending.'''
    option_choice = -1
    option_string = "1: [A]dd Task, 2: [V]iew Tasks, 3: [D]elete Task, 4: [C]lear List, 5: [Q]uit Application"
    print("\n/" + "-" * (len(option_string) + 2) + "\\")
    print("| " + option_string + " |")
    print("\\" + "-"*(len(option_string)+2) + "/")
    try:
        option_choice = str(input("Your choice?: ")).upper()
        if option_choice in option_letters:
            return execute_option(option_choice)
        else:
            option_choice = int(option_choice)
        if option_choice < 1 or option_choice > len(option_letters):
            print("Please choose an available option.")
        else: 
            return execute_option(option_choice)
    except ValueError:
        print("Please choose the number by an available option.")
    except:
        print("_ERROR")


def execute_option(option_choice):
    '''Run the option chosen'''
    print("---Executing Option---")
    if option_choice == "A" or option_choice == 1:
        add_task()
        return True
    elif option_choice == "V" or option_choice == 2:
        view_tasks()
        return True
    elif option_choice == "D" or option_choice == 3:
        delete_task()
        return True
    elif option_choice == "C" or option_choice == 4:
        clear_list()
        return True
    elif option_choice == "Q" or option_choice == 5:
        quit_application()
        return False

if __name__ == "__main__":
    run_application()
