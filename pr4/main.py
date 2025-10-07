import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime

CURRENT = "current"
FUTURE = "future"
OVERDUE = "overdue"

def get_task_status(due_date):
    today = datetime.now().date()
    if due_date == "NOW":
        return CURRENT
    date = datetime.strptime(due_date, "%Y-%m-%d").date()
    if date < today:
        return OVERDUE
    else:
        return FUTURE


def read_tasks_from_file(filename):
    tasks = []
    if not os.path.exists(filename):
        return tasks
    with open(filename, encoding='utf-8') as f:
        for line in f:
            if ";" in line:
                name, date_str = line.strip().split(";", 1)
                tasks.append((name, date_str))
    return tasks


def sort_tasks(tasks):
    status_order = {OVERDUE: 0, CURRENT: 1, FUTURE: 2}

    def sort_key(task):
        name, due_date = task
        status = get_task_status(due_date)
        if due_date == "NOW":
            date = datetime.min.date() 
        else:
            date = datetime.strptime(due_date, "%Y-%m-%d").date()
        return (status_order[status], date)

    return sorted(tasks, key=sort_key)


def display_tasks():
    for widget in frame.winfo_children():
        widget.destroy()

    tasks = read_tasks_from_file('tasks.txt')
    if not tasks:
        label = tk.Label(frame, text="Нет задач для отображения.", fg="gray")
        label.pack()
        return

    tasks = sort_tasks(tasks)

    for task_description, due_date in tasks:
        try:
            status = get_task_status(due_date)
            if status == CURRENT:
                label = tk.Label(frame, text=f"Текущая задача: {task_description} (Срок: {due_date})", fg="orange")
            elif status == FUTURE:
                label = tk.Label(frame, text=f"Будущая задача: {task_description} (Срок: {due_date})", fg="green")
            elif status == OVERDUE:
                label = tk.Label(frame, text=f"Просроченная задача: {task_description} (Срок: {due_date})", fg="red")
            label.pack()
        except ValueError:
            messagebox.showerror("Ошибка", f"Неверный формат даты для задачи: {task_description} (Срок: {due_date})")


root = tk.Tk()
root.title("Мои задачи")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=10)

button = tk.Button(root, text="Показать задачи", command=display_tasks)
button.pack(pady=10)

display_tasks()

root.mainloop()
