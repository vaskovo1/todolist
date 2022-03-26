from os import getcwd, path

def menu():
    print('1 - show tasks' + '\t' + '2 - add a task' + '\t' + '3 - del the task' + '\t' + '4 - del all tasks' + '\t' + 'x - exit')


def show_tasks():
    if len(todo_list) < 1:
        print('There are no tasks')
    else:
        print('Your tasks:')
        for ind, task in enumerate(todo_list, 1):
            print(f'{ind} - {task}')


def add_task():
    cmd = input('What to add?' + '\n')
    todo_list.append(cmd)
    print(f'The new task was added: {cmd}' + '\n')
    show_tasks()


def del_task():
    cmd = input('Enter the number of the task you want to delete' + '\n')
    if cmd.isdigit() and len(todo_list) != 0:
        cmd = int(cmd)
        if 0 <= cmd <= len(todo_list):
            deleting_task = todo_list[cmd-1]
            del todo_list[cmd - 1]
            print(f'The task was deleted: {deleting_task}' + '\n')
        else:
            print('Wrong number')
    else:
        print('The command cannot be executed')
    show_tasks()


def del_all_tasks():
    todo_list.clear()
    show_tasks()


def tasks():
    if path.isfile(path_to_tasks):
        with open(path_to_tasks) as f:
            tasks_list = [task.strip() for task in f.readlines()]
    else:
        tasks_list = []
        with open(path_to_tasks, 'w') as f:
            f.write('')
    return tasks_list


def record_new_tasks_to_file():
    with open(path_to_tasks, 'w') as f:
        todo_str = '\n'.join(todo_list)
        f.writelines(todo_str)


path_to_tasks = getcwd() + '/tasks.txt'

todo_list = tasks()

show_tasks()

keys_list = [str(i) for i in range(1, 5)]
values_list = [show_tasks, add_task, del_task, del_all_tasks]
dict_act_menu = dict(zip(keys_list, values_list))


while True:
    print()
    menu()
    command = input('Enter your command' + '\n')
    if command == 'x':
        record_new_tasks_to_file()
        break
    else:
        if command not in list(dict_act_menu.keys()):
            continue
        else:
            dict_act_menu[command]()
