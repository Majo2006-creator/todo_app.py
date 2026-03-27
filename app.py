import tkinter as tk
from tkinter import messagebox

# Clase principal de la aplicación
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Lista interna para almacenar tareas (texto + estado)
        self.tasks = []

        # =======================
        # Entrada de texto
        # =======================
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Evento: presionar Enter para añadir tarea
        self.entry.bind("<Return>", self.add_task_event)

        # =======================
        # Botones
        # =======================
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Marcar como Completada", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # =======================
        # Lista de tareas
        # =======================
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Evento opcional: doble clic para completar tarea
        self.listbox.bind("<Double-Button-1>", self.complete_task_event)

    # =======================
    # Función: Añadir tarea
    # =======================
    def add_task(self):
        task_text = self.entry.get().strip()

        if task_text == "":
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")
            return

        # Guardamos como diccionario (texto + estado)
        self.tasks.append({"text": task_text, "completed": False})
        self.update_listbox()

        # Limpiar entrada
        self.entry.delete(0, tk.END)

    # Evento Enter
    def add_task_event(self, event):
        self.add_task()

    # =======================
    # Función: Completar tarea
    # =======================
    def complete_task(self):
        selected = self.listbox.curselection()

        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona una tarea.")
            return

        index = selected[0]
        self.tasks[index]["completed"] = True
        self.update_listbox()

    # Evento doble clic
    def complete_task_event(self, event):
        self.complete_task()

    # =======================
    # Función: Eliminar tarea
    # =======================
    def delete_task(self):
        selected = self.listbox.curselection()

        if not selected:
            messagebox.showwarning("Advertencia", "Selecciona una tarea.")
            return

        index = selected[0]
        del self.tasks[index]
        self.update_listbox()

    # =======================
    # Actualizar Listbox
    # =======================
    def update_listbox(self):
        self.listbox.delete(0, tk.END)

        for task in self.tasks:
            if task["completed"]:
                # Mostrar tarea completada con check
                display_text = f"✔ {task['text']}"
            else:
                display_text = task["text"]

            self.listbox.insert(tk.END, display_text)


# =======================
# Ejecutar aplicación
# =======================
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
