import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification

def show():
    toast = ToastNotification(
    title= etrTitle.get(),
    message= etrMessage.get(),
    duration=3000,)
    toast.show_toast()

root = ttk.Window(themename="darkly", resizable=(False, False))
root.title("ToastGen")
root.place_window_center()

etrTitle = ttk.Entry()
etrMessage = ttk.Entry()

labTitle = ttk.Label(text="Title")
labMess = ttk.Label(text="Message")
btnGen = ttk.Button(command=show, text="Generate")

etrTitle.grid(row=0, column=1, sticky=W, padx=10, pady=10)
etrMessage.grid(row=1, column=1, sticky=W, padx=10, pady=10)
labTitle.grid(row=0, column=0, sticky=W, padx=10, pady=10)
labMess.grid(row=1, column=0, sticky=W, padx=10, pady=10)
btnGen.grid(row=3, column=1, sticky=W, padx=10, pady=10)

root.mainloop()