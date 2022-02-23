from taskaty.Task import Task
from datetime import date
from tabulate import tabulate
from argparse import Namespace



class TaskController:
    def __init__(self, file_name):
        self.file_name = file_name
        self.unfinished_tasks = []
        self.tasks = []

    def add_task(self, args):
        """Writes the given task to the file"""
        if not args.start_date:
            now = date.today().isoformat()
            args.start_date = now

        task = Task(args.title, args.description, args.start_date, args.end_date, args.done)
        with open(self.file_name, 'a') as file:
            file.write(str(task) + '\n')


    def tabulate(self, args):
        """Shows the tasks in a nicely formatted table"""
        all_tasks = self.list_all_tasks()
        unchecked_tasks = self.list_tasks()

        if not all_tasks:
            print('There are no tasks. To add a task use add <task>')
            return

        if args.all:
            self.print_table(all_tasks)
        else:
            if unchecked_tasks:
                self.print_table(unchecked_tasks)
            else:
                print('All tasks are checked!')


    def print_table(self, tasks):
        formatted_tasks = []
        for number, task in enumerate(tasks, 1):
            if task['start_date'] and task['end_date']:
                due_date = self.due_date(task['start_date'], task['end_date'])
            else:
                due_date = 'Open'

            formatted_tasks.append({'no': number, **task, 'due_date': due_date})

        print(tabulate(formatted_tasks, headers="keys"))

    def do_task(self, args):
        """Marks the given task as done"""
        #index = int(args.number)
        index = args.task

        tasks = self.list_all_tasks()

        if index <= 0 or index > len(tasks):
            print(f'Task number ({index}) does not exist')
            return

        tasks[index - 1]['done'] = True

        with open(self.file_name, 'w') as file:
             for task in tasks:
                 self.add_task(Namespace(**task))

    def remove(self, args):
        """Removes the given task"""
        tasks = self.list_all_tasks()
        if args.task:
            index = args.task
        else:
            index = len(tasks) - 1

        if index <= 0 or index > len(tasks):
            print(f'Task number ({index}) does not exist')
            return

        tasks.pop(index - 1)

        with open(self.file_name, 'w') as file:
             for task in tasks:
                 self.add_task(Namespace(**task))

    def reset(self, *args):
        """Removes all tasks from the file"""
        with open(self.file_name, 'w') as file:
            file.write('')
        print('You have deleted all tasks!')

    def due_date(self, start, end):
        """Calculates the number of days left for finishing the task"""
        start_date = date.fromisoformat(start)
        end_date = date.fromisoformat(end)
        date_delta = end_date - start_date
        return f'{date_delta.days} days left'

    def list_tasks(self):
        """Lists the undone tasks"""
        unfinished_tasks = []
        with open(self.file_name, 'r') as file:
            for line in file:
                title, description, start_date, end_date, done = line.split(', ')
                end_date = None if end_date == 'None' else end_date
                done = False if done.strip('\n') == 'False' else True
                if done:
                    continue

                unfinished_tasks.append({'title': title, 'description': description, 'start_date': start_date, 'end_date': end_date})

        return unfinished_tasks


    def list_all_tasks(self):
        """Lists all the tasks"""
        tasks = []
        with open(self.file_name, 'r') as file:
            for line in file:
                title, description, start_date, end_date, done = line.split(', ')
                done = False if done.strip('\n') == 'False' else True
                end_date = None if end_date == 'None' else end_date

                tasks.append({'title': title, 'description': description, 'start_date': start_date, 'end_date': end_date, 'done': done})

        return tasks

