from tkinter import *

root = Tk()

root.title('PZ_17')
root.geometry('400x400')

canvas = Canvas(root, width=400, height=400)
canvas.pack()

var = IntVar()
breakfast = IntVar()
lunch = IntVar()
dinner = IntVar()

continents = ('Arctic', 'Eurasia', 'South America')

frame = Frame(root)
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='Test form')
name_lb = Label(frame, text='Name')
name_text = Entry(frame, width=20)
password_lb = Label(frame, text='Password')
password_text = Entry(frame, width=20, show='*')
gender_lb = Label(frame, text='Gender')
gender_radio1 = Radiobutton(frame, text="Male", variable=var, value='male')
gender_radio2 = Radiobutton(frame, text="Female", variable=var, value='female')

continent_lb = Label(frame, text='Continent')
continent_list = Listbox(frame, width=15, height=2, selectmode=SINGLE)
for continent in continents:
    continent_list.insert(END, continent)

meals_lb = Label(frame, text='Meals')
meals_check1 = Checkbutton(frame, text='breakfast', variable=breakfast, onvalue=1, offvalue=0)
meals_check2 = Checkbutton(frame, text='lunch',  variable=lunch, onvalue=1, offvalue=0)
meals_check3 = Checkbutton(frame, text='dinner', variable=dinner, onvalue=1, offvalue=0)

remark_lb = Label(frame, text='Remark')
remark_text = Text(frame, width=20, height=5)

send_btn = Button(frame, text="Send")
cancel_btn = Button(frame, text="Cancel")

title.grid(row=0, column=0)
name_lb.grid(row=1, column=0)
name_text.grid(row=1, column=1)
password_lb.grid(row=2, column=0)
password_text.grid(row=2, column=1)
gender_lb.grid(row=3, column=0)
gender_radio1.grid(row=3, column=1)
gender_radio2.grid(row=4, column=1)
continent_lb.grid(row=5, column=0)
continent_list.grid(row=5, column=1)

meals_lb.grid(row=6, column=0)
meals_check1.grid(row=6, column=1)
meals_check2.grid(row=7, column=1)
meals_check3.grid(row=8, column=1)

remark_lb.grid(row=9, column=0)
remark_text.grid(row=9, column=1)

cancel_btn.grid(row=11, column=3)
send_btn.grid(row=11, column=4)

root.mainloop()
