from gui import *
from logic import Voting

def main():

    window = Tk()
    window.title('Voting App')
    window.geometry('240x220')
    window.resizable(False, False)

    view = Gui(window)
    controller = Controller(Voting(), view)
    view.set_controller(controller)

    window.mainloop()

if __name__ == '__main__':
    main()
