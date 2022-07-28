#intro of the game
print('|-----------------------------|')
print('|-----------------------------|')
print('|--        Blackjack        --|')
print('|-----------------------------|')
print('|-----------------------------|')
print('')
print('')
print('')
print('')
print('')
print('Welcome to Blackjack, here are the rules.')
print('The aim of black jack is to get as close to 21 as possible.')
print('If you get 21 exactly, you win, but if you go over you lose.')
print('If nobody gets exacly 21 the person closest to 21 but below 21')
print('')
print('To get a new number to add to your score you say "twist",')
print('or if you want stick to yor score you say "stick"')
print('')
print('')
print('')

#all values at 0
score = 0
maximum = 21

#the game code
import random
carryon = input("would you like to stick or twist?(t/s)")
while carryon == "t" and int(score)<int(maximum):
  number = random.randint(1,10)
  score = score + number
  if score > maximum:
    break
  elif  score < maximum:
    print("you score is now " + str(score) + ".")
    carryon = input("would you like to stick or twist?(y/n)")

#the results (tells you if youve won)

if score < maximum:
  print("your score is " + str(score) + ", how did you friends do?")
elif score == maximum:
  print("your a winner!")
elif score > maximum:
  print("bad luck!, you over drew")
