import re
import csv

class Voting:

    def vote(self, voter_id: str, choice: int) -> None:

        """
        Verifies valid user ID, gets answer, and stores the vote in votes.csv
        :param voter_id: The six-digit ID of the voter
        :param choice: John or Jane
        :return: None
        """

        if len(voter_id) != 6 or re.search('[^0-9]', voter_id):  # only accepts 6-digit numerical IDs
            raise ValueError('Invalid ID')

        unique_voters = []

        with open('votes.csv', 'r') as votes_file:
            for line in votes_file:
                unique_voters.append(line.rstrip('\n').split(',')[0])

        if voter_id in unique_voters:
            raise ValueError('Already voted')

        if choice == 1:
            choice = 'John'
        elif choice == 2:
            choice = 'Jane'
        else:
            raise ValueError('Select a candidate')

        with open('votes.csv', 'a', newline='') as votes_file:
            content = csv.writer(votes_file)
            content.writerow([voter_id, choice])
