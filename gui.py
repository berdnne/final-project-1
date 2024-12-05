import csv
from tkinter import *

class Gui:
    def __init__(self, window):
        self.window = window

        self.frame_one = Frame(self.window)
        self.label_title = Label(self.frame_one, text='Voting Application')

        self.label_name.pack(padx=10, pady=10)
        self.frame_one.pack(anchor='w')

        self.frame_two = Frame(self.window)
        self.label_age = Label(self.frame_two, text='Age   ')
        self.input_age = Entry(self.frame_two, width=20)

        self.label_age.pack(side='left', padx=10, pady=10)
        self.input_age.pack(side='right')
        self.frame_two.pack(anchor='w')

        self.frame_three = Frame(self.window)
        self.label_status = Label(self.frame_three, text='Status')

        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radio_student = Radiobutton(self.frame_three, text='Student', value=1, variable=self.radio_answer)
        self.radio_staff = Radiobutton(self.frame_three, text='Staff', value=2, variable=self.radio_answer)
        self.radio_both = Radiobutton(self.frame_three, text='Both', value=3, variable=self.radio_answer)

        self.label_status.pack(side='left', pady=10)
        self.radio_student.pack(side='left', pady=10)
        self.radio_staff.pack(side='right', pady=10)
        self.radio_both.pack(side='right', pady=10)
        self.frame_three.pack()

        self.frame_four = Frame(self.window)
        self.button_save = Button(self.frame_four, width=4, text='SAVE', command=self.save)
        self.label_info = Label(self.frame_four, text='Please fill out all values')

        self.button_save.pack(pady=10)
        self.label_info.pack()
        self.frame_four.pack()

    def save(self):

        name = self.input_name.get().strip()
        if name == '':
            name = 'Anonymous'

        age = self.input_age.get().strip()
        try:
            age = int(age) * 10
            if age < 0:
                raise ValueError
        except ValueError:
            self.label_info.config(text='Enter correct age value')

        status = self.radio_answer.get()
        if status == 0:
            status = 'NA'
        elif status == 1:
            status = 'Student'
        elif status == 2:
            status = 'Staff'
        else:
            status = 'Both'

        csv_file = open('data.csv', 'a', newline='')
        contents = csv.writer(csv_file)

        contents.writerow([name,age,status])