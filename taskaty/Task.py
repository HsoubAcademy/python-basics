class Task:

    def __init__(self, title: str, description: str = None, start_date: str = None, end_date: str = None, done: bool = False):
        self.title = title
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.done = done

    def __str__(self) -> str:
        return f'{self.title}, {self.description}, {self.start_date}, {self.end_date}, {self.done}'



if __name__ == '__main__':
    task = Task('Go to the store')
    print(task)
