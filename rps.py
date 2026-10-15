import random

rps_dict = {
  'r' : 'Rock',
  'p' : 'Paper',
  's' : 'Scissors',
  'e' : 'Exit'
}

user_Score = 0
comp_Score = 0

def game():
  global user_Score
  global comp_Score

  print('''
====ROCK PAPER SCISSORS====
    Choose R for Rock
    Choose P for Paper
    Choose S for Scissors
    Choose E to Exit program
''')

  # Input Validation
  flag = True
  while flag:
    try:
      user = input('Ur Call? ').lower()[0:1]
      if user == 'r' or user == 'p' or user == 's' or user =='e':
        flag = False
      else:
        print('Not valid')
        flag = True
    except ValueError:
      print('Not valid')
    
  user = rps_dict[user]
  comp = rps_dict[random.choice(['r','p','s'])].capitalize()

  # Program Esc
  if user == rps_dict['e']:
      print('\n --- Final Score --- \n')
      print('\tYou :', user_Score)
      print('\tAI :', comp_Score)
      raise SystemExit()
    
  print(user, 'X', comp)
  check(user,comp)
  print('\n --- Live Score --- \n')
  print('\tYou :', user_Score)
  print('\tAI :', comp_Score)
  game()

def check(user,comp):
  global user_Score
  global comp_Score
# ROCK BEAT SCISSORS OR SCISSORS BEAT PAPER OR PAPER BEATS ROCK
  # WIN Cases
  if (user == rps_dict['r'] and comp == rps_dict['s']) or (user == rps_dict['s'] and comp == rps_dict['p']) or (user == rps_dict['p'] and comp == rps_dict['r']):
    user_Score += 1
    print('YOU WIN !!!')

  # TIE Case   
  elif user == comp:
    print("It's A Tie !!!")

  # LOSE
  else:
    comp_Score += 1
    print('YOU LOSE !!!')

game()

