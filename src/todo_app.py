import tkinter as tk
from tkinter import messagebox

# Clase principal
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.tasks = []

        # Entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Evento Enter
        self.entry.bind("<Return>", self.add_task_event)

        # Botones
        frame = tk.Frame(root)
        frame.pack()

        tk.Button(frame, text="Añadir Tarea", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Completar", command=self.complete_task).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Eliminar", command=self.delete_task).grid(row=0, column=2, padx=5)

        # Lista
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Doble clic
        self.listbox.bind("<Double-Button-1>", self.complete_task_event)

    def add_task(self):
        task = self.entry.get().strip()
        if task == "":
            messagebox.showwarning("Error", "Tarea vacía")
            return

        self.tasks.append({"text": task, "done": False})
        self.update_list()
        self.entry.delete(0, tk.END)

    def add_task_event(self, event):
        self.add_task()

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index]["done"] = True
            self.update_list()
        except:
            messagebox.showwarning("Error", "Selecciona una tarea")

    def complete_task_event(self, event):
        self.complete_task()

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tasks[index]
            self.update_list()
        except:
            messagebox.showwarning("Error", "Selecciona una tarea")

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            text = f"✔ {task['text']}" if task["done"] else task["text"]
            self.listbox.insert(tk.END, text)

# Ejecutar app
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
