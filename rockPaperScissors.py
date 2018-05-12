import random

stevenWrightQuotes = ['A lot of people are afraid of heights. Not me, I\'m afraid of widths.', \
                      'Whenever I think of the past, it brings back so many memories.', \
                      'Everywhere is within walking distance if you have the time.', \
                      'There\'s a fine line between fishing and just standing on the shore like an idiot.']
partingThought = stevenWrightQuotes[random.randint(0, 3)]

gameInPlay = True
while gameInPlay:
    
    print('rock, paper or scissors?')
    p1 = input()
    p2 = random.randint(0, 2)
    choices = ['rock', 'paper', 'scissors']
    print('computer: ' + choices[p2])

    if p1 == choices[p2]:
        print('STALEMATE, PLAY AGAIN!')
        continue
    elif (p1 == 'rock' and choices[p2] == 'paper') or \
         (p1 == 'paper' and choices[p2] == 'scissors') or \
         (p1 == 'scissors' and choices[p2] == 'rock'):
        print('COMPUTER WINS!')
        break
    else:
        print('YOU WIN!')
        break

print('Parting thought: ' + partingThought + '\n-Steven Wright')
