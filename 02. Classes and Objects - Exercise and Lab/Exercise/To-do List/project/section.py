from project.task import Task


class Section:
    tasks_completed_counter = 0

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        # add new_task of type Task
        # look at this and study why it is working
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        for el in range(len(self.tasks)):
            if self.tasks[el].name == task_name:
                Section.tasks_completed_counter += 1
                self.tasks[el].completed = True
                self.tasks.remove(self.tasks[el])
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"


    @staticmethod
    def clean_section():
        return f"Cleared {Section.tasks_completed_counter} tasks."

    def view_section(self):
        res = ""
        res += f"Section {self.name}:\n"
        for el in self.tasks:
            res += f"{el.details()}\n"
        return res.strip()




