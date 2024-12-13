def main():
        print("\n===== To-Do List =====")
        print("1. Add")
        print("2. Show")
        print("3. Mark as Done")
        print("4. Exit")

        number = input("Enter: ")

        if number == '1':
            print()
            n_task = int(input("How may task you want to add: "))
            
            for i in range(n_task):
                task = input("Enter the task: ")
                task.append({"task": task, "done": False})
                print("Task added!")

        elif number == '2':
            print("\nTasks:")
            for index, task in enumerate(task):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif number == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(task):
                task[task_index]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number.")

        elif number == '4':
            print("Exiting the To-Do List.")
            

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
