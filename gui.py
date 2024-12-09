import csv
import re
from tkinter import *

class Gui:
    def __init__(self, window):
        self.window = window

        self.frame_one = Frame(self.window)
        self.label_title = Label(self.frame_one, text='Voting Application')

        self.label_title.pack(padx=10, pady=10)
        self.frame_one.pack()

        self.frame_two = Frame(self.window)
        self.label_id = Label(self.frame_two, text='ID      ')
        self.input_id = Entry(self.frame_two, width=20)

        self.label_id.pack(side='left', padx=10, pady=10)
        self.input_id.pack(side='right')
        self.frame_two.pack(anchor='w')

        self.frame_three = Frame(self.window)
        self.label_status = Label(self.frame_three, text='Candidates')
        self.label_status.pack(pady=10)

        self.frame_four = Frame(self.window)

        self.radio_answer = IntVar()
        self.radio_answer.set(0)
        self.radio_john = Radiobutton(self.frame_four, text='John', value=1, variable=self.radio_answer)
        self.radio_jane = Radiobutton(self.frame_four, text='Jane ', value=2, variable=self.radio_answer)

        self.radio_john.pack(side='top', pady=2)
        self.radio_jane.pack(side='bottom', pady=2)
        self.frame_four.pack()

        self.frame_five = Frame(self.window)
        self.button_vote = Button(self.frame_five, width=12, text='SUBMIT VOTE', command=self.vote)
        self.label_info = Label(self.frame_five)

        self.button_vote.pack(pady=10)
        self.label_info.pack()
        self.frame_five.pack()

    def vote(self):

        voter_id = self.input_id.get().strip()
        self.input_id.delete(0, END)

        if len(voter_id) != 6 or re.search('[^0-9]', voter_id): # only accepts 6-digit numerical IDs
            self.label_info.config(text='Invalid ID', fg='red')
            return

        unique_voters = []

        with open('votes.csv', 'r') as votes_file:
            for line in votes_file:
                unique_voters.append(line.rstrip('\n').split(',')[0])

        print(unique_voters)
        if voter_id in unique_voters:
            self.label_info.config(text='Already voted', fg='red')
            return

        choice = self.radio_answer.get()

        if choice == 1:
            choice = 'John'
        elif choice == 2:
            choice = 'Jane'
        else:
            self.label_info.config(text='Select a candidate', fg='red')
            return

        with open('votes.csv', 'a', newline='') as votes_file:
            content = csv.writer(votes_file)
            content.writerow([voter_id, choice])

        self.label_info.config(text='Vote submitted', fg='black')