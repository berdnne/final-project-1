def vote_menu():

    choice = input('------------------------------\nVOTE MENU\n------------------------------\nv: Vote\nx: Exit\nOption: ').lower().strip()
    while not(choice == 'v' or choice == 'x'):
        choice = input('Invalid (v/x): ').lower().strip()

    return choice

def candidate_menu():

    vote = input('------------------------------\nCANDIDATE MENU\n------------------------------\n1: John\n2: Jane\nCandidate: ').strip()
    while not (vote == '1' or vote == '2'):
        vote = input('Invalid (1/2): ').strip()

    return int(vote)

def main():

    john_votes = 0
    jane_votes = 0

    choice = vote_menu()
    while not(choice == 'x'):
        vote = candidate_menu()
        if vote == 1:
            print('Voted John')
            john_votes += 1
        else:
            print('Voted Jane')
            jane_votes += 1

        choice = vote_menu()

    print('------------------------------\nJohn - ', john_votes, ', Jane - ', jane_votes, ', Total - ', (john_votes + jane_votes), '\n------------------------------', sep = '')

main()