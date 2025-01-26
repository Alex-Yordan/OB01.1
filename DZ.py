class Task:
    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status

    def mark_as_completed(self):
        self.status = True

    def __str__(self):
        status = "Выполнено" if self.status else "Не выполнено"
        return f'Описание: {self.description}, Срок: {self.deadline}, Статус: {status}'

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Неверный индекс задачи")

    def show_pending_tasks(self):
        print("Список текущих задач:")
        for task in self.tasks:
            if not task.status:
                print(task)


if __name__ == "__main__":
    manager = TaskManager()

    manager.add_task("Сделать домашнее задание", "2025-01-25")
    manager.add_task("Подготовиться к экзамену", "2025-06-01")

    manager.mark_task_as_completed(0)

    manager.show_pending_tasks()