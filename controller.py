from tkinter.constants import END

class Controller:

    def __init__(self, model, view):

        """
        Establishes a model and view as per MVC structure.
        :param model: Voting class
        :param view: Gui class
        """

        self.model = model
        self.view = view

    def vote(self, voter_id: str, choice: int) -> None:

        """
        Submits vote or displays error text if applicable
        :param voter_id: The six-digit ID of the voter
        :param choice: John or Jane
        :return: None
        """

        self.view.input_id.delete(0, END)

        try:
            self.model.vote(voter_id, choice)
        except ValueError as error:
            self.view.label_info.config(text=error, fg='red')
        else:
            self.view.label_info.config(text='Vote submitted', fg='black')