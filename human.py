# CHILD CLASS


from unicodedata import name
from player import Player
from time import sleep
class Human(Player):

    def __init__(self, name):
        super().__init__()        # ❓ Question with name
        self.name = name
        self.score = 0
       
    def choose_gesture(self):

        print('Make your move')
        sleep(1)
        move = self.gesture[0,4] # will have to verify (move matches name on the list)
        return move
        
        
        

    # def get_name(self):
    #     print('Name yourself')
    #     name = input()
    #     return name



# Question: Will i need to put points function in the player class? 