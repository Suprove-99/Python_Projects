import tkinter as tk


count = -1
run = False


def clock_head(flag):
    def value():
        if run:
            global count
            if count == -1:
                show = "Here we go!"
            else:
                show = str(count)
            flag['text'] = show
            flag.after(1000, value)
            count += 1

    value()


# Run
def Start(flag2):
    global run
    run = True
    clock_head(flag2)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


# stop
def Stop():
    global run
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    run = False


# Reset
def Reset(label):
    global count
    count = -1
    if run == False:
        reset['state'] = 'disabled'
        mark['text'] = 'Ready to run again?'
    else:
        mark['text'] = 'Start'


base = tk.Tk()
base.title("Stopwatch")
base.minsize(width=300, height=200)
mark = tk.Label(base, text="Ready to run!?", fg="green", font="Times 20 italic")
mark.pack()
start = tk.Button(base, text='Start', fg='blue', width=50, command=lambda: Start(mark))
stop = tk.Button(base, text='Stop', fg='red', width=50, state='disabled', command=Stop)
reset = tk.Button(base, text='Reset', width=50, state='disabled', command=lambda: Reset(mark))
start.pack()
stop.pack()
reset.pack()
base.mainloop()
