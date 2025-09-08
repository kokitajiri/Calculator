import os
import sqlite3

class taskmanager():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, db_name)
    def __init__(self, db_name="task.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            done INTEGER DEFAULT 0
            );
        """)
        self.conn.commit()
    
    def add_task(self):
            name = input("Please enter your task: ")
            if not name:
                print("Task name can not be empty.")
                return
            self.cursor.execute("INSERT INTO tasks (name, done) VALUES (?, 0)", (name,))
            self.conn.commit()
            print(f"Task '{name}' has been added.")
    
    def show_task(self):
        self.cursor.execute("SELECT id, name, done FROM tasks ORDER BY id")
        tasks = self.cursor.fetchall()
        if not tasks:
            print("There is no task.")
            return
        print("Tasks:")
        for i, (task_id, name, done) in enumerate(tasks, 1):
            status = "Done ✓" if done else "Incomplete ✕"
            print (f"{i}. {name} - {status} (ID:{task_id})")
    
    def complete_task(self, index):
        self.cursor.execute("SELECT id FROM tasks ORDER BY id")
        tasks = self.cursor.fetchall()
        if 0 < index <= len(tasks):
            task_id = tasks[index - 1][0]
            self.cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?",
            (task_id,))
            self.conn.commit()
            print(f"Task ID {task_id} completed.")
        else:
            print("The task with taht number does not exist.")
                
    def remove_task(self, index: int):
        self.cursor.execute("SELECT id, name FROM tasks ORDER BY id")
        tasks = self.cursor.fetchall()
        if 0 < index <= len(tasks):
            task_id, name = tasks[index - 1]
            self.cursor.execute("DELETE FROM tasks WHERE id = ?",
            (task_id,))
            self.conn.commit()
            print(f"Task '{name}' is deleted.")
        else:
            print("The task with that number does not exsist.")
                
def main():
    tm = taskmanager()
    while True:
        print("[1] Add   [2] Show   [3]Complete   [4]Remove   [5]Exit")
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
        elif choice == "5":
            print("Bye.")
            break
                
if __name__ == "__main__":
    main()
