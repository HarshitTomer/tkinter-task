import tkinter as tk

def create_counter(master, title, initial_value):
    frame = tk.Frame(master, pady=10)
    frame.pack()

    tk.Label(frame, text=f"{title} Counter:").pack()

    counter_var = tk.StringVar(value=initial_value)
    counter_label = tk.Label(frame, textvariable=counter_var, fg='blue')
    counter_label.pack(pady=5)

    paused = False

    def update_counter():
        if not counter_var.get().isdigit() or paused:
            return
        value = int(counter_var.get())
        value += 2
        counter_var.set(str(value))
        master.after(1000, update_counter)

    def stop_counter():
        nonlocal paused
        paused = True

    def resume_counter():
        nonlocal paused
        if not paused:
            return  
        paused = False
        update_counter()

    tk.Button(frame, text=f"Start {title}", command=update_counter, padx=10, pady=5).pack(side=tk.LEFT)
    tk.Button(frame, text=f"Stop {title}", command=stop_counter, padx=10, pady=5).pack(side=tk.LEFT, padx=10)
    tk.Button(frame, text=f"Resume {title}", command=resume_counter, padx=10, pady=5).pack(side=tk.LEFT)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Odd Even Counter")

    create_counter(root, "Odd", "1")
    create_counter(root, "Even", "2")

    root.mainloop()
