import tkinter as tk

from Model.AdminModel import AdminModel
from View.AdminView import AdminView
from Controller.AdminController import AdminController


root = tk.Tk()

model = AdminModel()
view = AdminView(root)
controller = AdminController(model, view)

root.mainloop()
