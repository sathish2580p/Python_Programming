# WAP to build card game between computer and user consider the foloowing the list of cards 
# cards=[2,3,4,5,6,7,8,9,10,K,Q,A] 
# create a two methods card value and play game
# card value should returns score of the card based on the card name
# [2:2],[3:3],[4:4],[5:5],[6:6],[7:7],[8:8],[9:9],[10:10],[11:J],[12:Q],[13:K],[14:A]
# play game method should start the game between user and computer,
# they need to play total rounds of total no of cards, 
# in ecah round find the score of card played by user and computer, 
# at last compare the score of user and computer and display the winner 


import random 

class CARD_GAME:
    def __init__(self,cards,username):
        self.cards = cards
        self.username = self.username
        self.computer_score = 0
        self.user_score = 0

    def card_value(self,card):
        card_score = {v:k for k,v in enumerate(self.cards,2)}[card]

    def play_game(self):
        print('Game started ')
        for i in range(len(self.cards)):
            uc = input('Enter the card :')
            if uc in self.cards:
                print(f"{self.username} played :",uc)
                self.user_score == self.card_value(uc)


            cs_card = random.choice(self.cards)
            print("computer played :", cs_card)
            self.computer_score += self.card_value(cs_card)

        

            
cards = [
    '2','3','4','5','6','7','8','9','10','J','Q','K','A'
]



