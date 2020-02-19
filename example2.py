####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '1*Team to be determined*'
strategy_name = 'Random (leaning collude)'
strategy_description = 'Random choice. 66% chance of colluding, 33% chance of betraying.'


import random

def move(my_history, their_history, my_score, their_score):
  '''Makes choice based on weighted random choice (but leans towards colluding) Does not account for opponent's or self's history since it always chooses randomly. '''
  random_choice = random.randint(0,4)
  if random_choice >= 2:
    return 'c'
  else:
    return 'b'
    
'''Since the strategy uses a weighted random choice, it doesn't need to know any stats about itself or it's opponent.'''
move(0,0,0,0)