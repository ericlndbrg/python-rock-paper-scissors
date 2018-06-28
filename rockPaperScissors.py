import random

def rockPaperScissors(player1):
  computer = random.randint(0, 2)
  choices = ['rock', 'paper', 'scissors']
  player2 = choices[computer]
  
  if player1 == player2:
    result = 'STALEMATE, PLAY AGAIN!'
  elif (player1 == 'rock' and player2 == 'paper') or \
       (player1 == 'paper' and player2 == 'scissors') or \
       (player1 == 'scissors' and player2 == 'rock'):
    result = 'COMPUTER WINS!'
  else:
    result = 'YOU WIN!'
    
  return result

playGame = True
while playGame:
  print('rock, paper or scissors?')
  player1 = input()
  outcome = rockPaperScissors(player1)
  record = open('rpc-outcomes.txt', 'a')
  record.write(outcome + '\n')
  record.close()
  print(outcome)

  if outcome != 'STALEMATE, PLAY AGAIN!':
    break
  else:
    continue

stevenWrightQuotes = ['A lot of people are afraid of heights. Not me, I\'m afraid of widths.', \
                      'Whenever I think of the past, it brings back so many memories.', \
                      'Everywhere is within walking distance if you have the time.', \
                      'There\'s a fine line between fishing and just standing on the shore like an idiot.']
partingThought = stevenWrightQuotes[random.randint(0, 3)]
print('Parting thought:\n' + partingThought + '\n-Steven Wright')

#TODO add a way to play the game again if the user wants to play again
