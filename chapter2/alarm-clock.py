# import and global vars
import tkinter as tk

window = tk.Tk()
window.title("Alarm App")
window.resizable(width=False, height=False)
window.geometry("500x500")

# function for getting current time
def get_current_time():
    pass



# set alarm timer
def set_alarm():
    print("Alarm Has Been Set",f"{hour_alarm_entry.get()}:{ minute_alarm_entry.get()}")



# function for comparing time with alarm



# ui design


# text time
time_label = tk.Label(window, text="Welcome to Alarm App",font=("Tahoma", 32))

time_label.pack()
# text input hour
# input entry
tk.Label(window, text="Hour").pack()
hour_alarm_entry = tk.Entry(window)
hour_alarm_entry.pack()

# text input minute
# input entry
tk.Label(window, text="Minute").pack()
minute_alarm_entry = tk.Entry(window)
minute_alarm_entry.pack()

# button set alarm
tk.Button(window, text="Submit",command=set_alarm).pack()
# showing last alarm
latest_alarm_label = tk.Label(window, text="Latest Alarm")
latest_alarm_label.pack()
# run the app
window.mainloop()