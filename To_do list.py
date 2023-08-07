import tkinter as tk

def add():
    new_item = entry_box.get()
    list_box.insert(tk.END, new_item)
def deletion():
    selected_index = list_box.curselection()
    if selected_index:
        index_to_delete = selected_index[0]
        list_box.delete(index_to_delete)

def edit_item():
    selected_index = list_box.curselection()
    if selected_index:
        index_to_edit = selected_index[0]
        item_to_edit = list_box.get(index_to_edit)

        # Hide the Listbox and show the Entry widget with the selected text
        list_box.pack_forget()
        entry_box.delete(0, tk.END)
        entry_box.insert(0, item_to_edit)
        entry_box.pack()

def save_changes():
    updated_text = entry_box.get()
    selected_index = list_box.curselection()
    if selected_index:
        index_to_edit = selected_index[0]
        list_box.delete(index_to_edit)
        list_box.insert(index_to_edit, updated_text)
       # entry_box.pack_forget()
        list_box.pack()

def clear():
    entry_box.delete(0,tk.END)

window = tk.Tk()
window.geometry("685x650")
window.title("To-do list")

frame = tk.Frame(window)
frame.pack()

label1 = tk.Label(frame, text="To Do List", font=("Script MT Bold",30), bg="LightSeaGreen", fg="White", width=29, height=2)
label1.pack()

list_box = tk.Listbox(frame, font=("Calibri",18),width=56,height=15,selectbackground="LightSteelBlue",highlightthickness=0,selectforeground="Black",background="White")
list_box.pack(side="left",fill="both")

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right",fill="both")

list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)

entry_box = tk.Entry(window,font=("Calibri",16),width=53,background="Lavender")
entry_box.pack(pady=5)

frame2 = tk.Frame(window)
frame2.pack()

btn_add = tk.Button(frame2,text="ADD",font=("Arial Black",11),background="LightSeaGreen",width=10,command=add)
btn_add.pack(side="left",padx=6,pady=7)

btn_del = tk.Button(frame2,text="DELETE",font=("Arial Black",11),background="Red",width=10,command=deletion)
btn_del.pack(side="left",padx=6,pady=7)

btn_edit = tk.Button(frame2,text="EDIT",font=("Arial Black",11),background="Yellow",width=10,command=edit_item)
btn_edit.pack(side="right",padx=6,pady=7)

btn_save = tk.Button(frame2,text="SAVE",font=("Arial Black",11),background="SteelBlue",width=10,command=save_changes)
btn_save.pack(side="right",padx=6,pady=7)

btn_clear= tk.Button(frame2,text="CLEAR",font=("Arial Black",11),background="Grey",width=10,command=clear)
btn_clear.pack(side="right",padx=6,pady=7)

window.mainloop()
