from gui import *

def main():

    window = Tk()
    window.title('Voting App')
    window.geometry('240x220')
    window.resizable(False, False)
    Gui(window)
    window.mainloop()

    #john_votes = 0
    #jane_votes = 0

    #choice = vote_menu()
    #while not(choice == 'x'):
    #    vote = candidate_menu()
    #    if vote == 1:
    #        print('Voted John')
    #        john_votes += 1
    #    else:
    #        print('Voted Jane')
    #        jane_votes += 1

    #    choice = vote_menu()

    #print('------------------------------\nJohn - ', john_votes, ', Jane - ', jane_votes, ', Total - ', (john_votes + jane_votes), '\n------------------------------', sep = '')

if __name__ == '__main__':
    main()
