class Todo:
    todolist = {'1': 'Добавить дело', '2': 'Список дел', '3': 'Выйти'} 
    def __init__(self):
        self.todo_items = []
 
    def add_todo(self, items):
        self.todo_items.append(items)
 
    def list(self):
        print('Список дел:')
        for item in self.todo_items:
            print(str(item.num) + '. ' + item.todo + ' (Выполнено)' * int(item.is_done))
        print()
 
    def find(self, find_str):
        return ((item.num, item.todo) for item in self.todo_items if item.todo.find(find_str) != -1)
 
    def run(self):
 
        while True:
            print('Меню:')
            for num, val in Todo.todolist.items():
                print(num + '. ' + val, end='\n')
            command = input()
            if command == '1':
                self.add_todo(Todolist2(input('Какое дело?: ')))
                print('Новое дело добавлено!')
            elif command == '2':
                self.list()
            elif command == '3':
                print('Программа завершена!')
                break
 
class Todolist2:
    todo = 0
 
    def __init__(self, new_do):
        self.is_done = False
        Todolist2.todo += 1
        self.num = Todolist2.todo
        self.todo = new_do
 
    def check(self):
        self.is_done = True
 
    def uncheck(self):
        self.is_done = False
 
 
if __name__ == '__main__':
    todo_1 = Todo()
    todo_1.run()