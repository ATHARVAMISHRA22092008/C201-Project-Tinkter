from tkinter import *
window=Tk()

# add widgets here
def calculate_interest():
    p = int(p_entry.get())
    r = int(r_entry.get())
    t = int(t_entry.get())
    i = (p*r*t)/100
    name = username.get()
    result_label.destroy()
    output_message=Label(result_frame,text=name+", your interest on CAD"+str(p)+" at the interest rate of "+str(r)+"\n over the duration of"+str(t)+" years is CAD "+str(i), bg = "lightcyan", font=("Calibri", 8), width=42, height = 5)
    output_message.place(x=20, y=40)
    output_message.pack()

window.title('BMI Calculator')
window.geometry("400x465")
window.configure(bg='lightcyan')


app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

r_label = Label(window, text = "enter interest rate (%)", fg = "black", bg="lightcyan", font = ("Calibri", 12))
r_label.place(x=20, y=140)

r_entry = Entry(window, text = "", bd=2, width = 15)
r_entry.place(x=150, y=142)

p_label = Label(window, text = "enter principal value", fg = "black", bg="lightcyan", font = ("Calibri", 12))
p_label.place(x=20, y=185)

p_entry = Entry(window, text = "", bd=2, width = 15)
p_entry.place(x=150, y=187)

t_label = Label(window, text = "enter time (years)", fg = "black", bg="lightcyan", font = ("Calibri", 12))
t_label.place(x=20, y=230)

t_entry = Entry(window, text = "", bd=2, width = 15)
t_entry.place(x=150, y=232)

calculate_button = Button(window, text = "Calculate", fg = "black", bg = "cyan", bd = 4, command = calculate_interest)
calculate_button.place(x=20, y=295)




result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 8))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=345)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()