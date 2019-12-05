from random import randint

answer=randint(1,10)

while True:
    try:
      print(answer)
      guess=int(input('please enter a number between 1 -10: '))
      if 0 < guess < 11:
        if answer == guess:
             print('your guess is right')
             break
      else:
        print('hey enter number between 1 to 10')

    except ValueError:
        print('print only number between 1 to 10')
        continue


