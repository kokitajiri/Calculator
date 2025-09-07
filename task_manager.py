class taskmanager():
    
    def __init__(self):
        self.task = []
    
    def add_task(self):
            name = input("Please enter your task: ")
            if not name:
                print("Task name can not be empty.")
                return
            self.task.append({"name": name, "done": False})
            print(f"Task '{name}' has been added.")
    
    def show_task(self):
        if not self.task:
            print("There is no task.")
            return
        print("Tasks:")
        for i, task in enumerate(self.task, 1):
            status = "Done ✓" if task["done"] else "incomplete ✕"
            print (f"{i}. {task['name']} - {status}")
    
    def complete_task(self, index):
        if 0 < index <= len(self.task):
            self.task[index - 1]["done"] = True 
            print(f"Task {self.task[index - 1]['name']} completed.")
        else:
            print("The task with taht number does not exist.")
                
    def remove_task(self, index: int):
        if 0 < index <= len(self.task):
            removed = self.task.pop(index - 1)
            print(f"Task{removed['name']}is deleted.")
        else:
            print("The task with that number does not exsist.")
                
def main():
    tm = taskmanager()
    while True:
        print("[1] Add   [2] Show   [3]Complete   [4]Remove")
        choice = input("Select: ")
        
        if choice == "1":
            tm.add_task()
        elif choice == "2":    
            tm.show_task()
        elif choice == "3":
            tm.show_task()
            try:
                number = int(input("Enter task number to complete: "))
                tm.complete_task(number)
            except ValueError:
                print("Please enter the correct number.")
        elif choice == "4":
            tm.show_task()
            try:
                number = int(input("Enter task number to remove: "))
                tm.remove_task(number)
            except ValueError:
                print("Please enter the correct number.")
                
if __name__ == "__main__":
    main()
