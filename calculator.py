from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        try:
            if scvalue.get().isdigit():
                value = int(scvalue.get())
            else:
                value = eval(scvalue.get())
                scvalue.set(value)
                screen.update()
        except Exception as e:
            scvalue.set("Error")
    elif text == "C":
        scvalue.set("")
        scvalue.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("644x900")
root.title("Calculator")
root.config(bg='white')

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvariable=scvalue, font='lucida 25 bold')
screen.pack(fill=X, ipadx=8, padx=10, pady=10)

button_frame = Frame(root, bg='grey')

button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    '(', ')', '**', 'C'
]

row_val = 1
col_val = 0

pad_x = 15
pad_y = 10

for button_text in button_texts:
    button = Button(button_frame, text=button_text, padx=pad_x, pady=pad_y, font='lucida 20 bold')
    button.grid(row=row_val, column=col_val, padx=10, pady=10)
    button.bind("<Button-1>", click)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

button_frame.pack()

root.mainloop()
