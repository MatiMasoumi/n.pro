task={}
def add(name):
    if name not in task:
        task[name]={'status':False,'duration': None}
        print('added')
    else:
        print('already Exits')
def display():
    for i ,(name,detalis) in enumerate(task.items()):
        print(i+1,name,detalis['status'],detalis['duration'])
def remove(name):
    if name in task:
        task.pop(name)
        print('removed')
    else:
        print('not found')
def edit(name):
    if name in task:
        new_name=input('new name').lower()
        if new_name not in task:
            task[new_name]=new_name.pop(name)
            print('edited')
        else:
            print('already exit')
    else:
        print('not found')
def search(name):
    if name in task:
        status=task[name]['status']
        duration=task[name]['duration']
        print(f'status:{status},duration:{duration}')
    else:
        print('not found')
def mark(name):
    if name in task:
        if not task[name]['status']:
            duration=float(input('enter the duration (in hours)it took to complete:'))
            task[name]['status']=True
            task[name]['duration']=duration
            print(f'task:{name},duration:{duration:.2f}')
        else:
            print('done')
    else:
        print('not found')
def detalis():
    number=len(task)
    not_done=sum(1 for tasks in task.values() if not tasks['status'])
    done=sum(1 for tasks in task.values() if tasks['status'])
    total_duration=sum(task['duration'] for tasks in task.values() if tasks['duration'] is not None)
    print(f'number of task:{number}')
    print(f'not done:{not_done}')
    print(f'done:{done}')
    print(f'total duration:{total_duration:.2f}')
def help():
    print('\nAvaiable answer:')
    print('add - Add a new task')
    print('display - Display all tasks')
    print('remove - Remove a task')
    print('edit - Edit a task name')
    print('search - search for a task')
    print('mark - Mark a task for done')
    print('detalis - Show task Detalis')
    print('help - Show this help message')
    print('exit - Exit the program')

def main():
    while True:
        answer=input('add,display,remove,edit,serch,mark,detalis,help,exit:').lower()
        if answer=='add':
           name=input('name for add:').lower()
           add(name)
        elif answer=='display':
           display()
        elif answer=='remove':
           name=input('name for remove:').lower()
           remove(name)
        elif answer=='edit':
           name=input('name for edit:').lower()
           edit(name)
        elif answer=='search':
           name=input('name for search:').lower()
           search(name)
        elif answer=='mark':
           name=input('name for mark:').lower()
           mark(name)
        elif answer=='detalis':
           detalis()
        elif answer=='help':
           help()
        elif answer == "exit":
           break
        elif answer == "":
           continue
        else:
           print(f'{answer}:not founded')
main()
