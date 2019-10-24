import random

money = 100

def rolling(bet_made, the_word):
  num = random.randint(0, 1)
  if the_word == 'Heads' and num == 1:
    total = bet_made
    print('You won %s coins' % (bet_made))
  elif the_word == 'Tails' and num == 0:
    total = bet_made
    print('You won %s coins' % (bet_made))
  else:
    total = - bet_made
    print('You lost %s coins' % (bet_made))
  return total
rolling(10, 'Heads')

def double_rolling(bet_made, predict_number):
  num1 = random.randint(1, 6)
  num2 = random.randint(1, 6)
  if (num1 + num2) % 2 == 0 and predict_number % 2 == 0:
    total = money + bet_made
    print('You won, now you have %s coins' % (total))
  elif (num1 + num2) % 2 != 0 and predict_number % 2 != 0:
    total = money + bet_made
    print('You won, now you have %s coins' % (total))
  else:
    total = money - bet_made
    print('You lost, now you have %s coins' % (total))
  return total
double_rolling(10, 1)

def card_picking(bet_made1, bet_made2):
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  if num1 > num2:
    total = bet_made1 + bet_made2
    print('Player one won %s coins and have %s now' % (bet_made2, total))
    return total
  elif num1 < num2:
    total = bet_made2 + bet_made1
    print('Player two win %s coins and have %s now' % (bet_made1, total))
    return total
  else:
    print('Tie, money back')
card_picking(10, 20)


def roulette(bet_made1, bet_made2, bet_made3, money_bet
             ): #  bet_made1 - чёт нечёт, bet_made2 - красное или чёрное, bet_made3 - конкретное число
  num1 = random.randint(1, 100)
  num2 = random.choice (['Red', 'Black'])
  num3 = 0
  if bet_made1 = num 1

