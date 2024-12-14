from tkinter import *
from controller import Controller

class Gui:
    def __init__(self, window):

        """
        Creates GUI elements.
        :param window: The window that elements are housed in
        """

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

        self.controller = None

    def set_controller(self, controller: Controller) -> None:

        """
        Establishes a connection back to a controller as per MVC structure.
        :param controller: Connected controller
        :return: None
        """

        self.controller = controller

    def vote(self) -> None:

        """
        Points to the controller's dealer_turn method, retrieving the text from the input field and radio button choice
        :return: None
        """

        if self.controller:
            self.controller.vote(self.input_id.get().strip(), self.radio_answer.get())
