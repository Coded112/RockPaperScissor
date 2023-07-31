rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
c = int(input("enter the choice 0 for rock, 1 for paper and 2 for sissors: "))
figures = [rock,paper,scissors]
d = random.randint(0,2)
print(f"you chose:\n{figures[c]}")
print(f"computer chose:\n{figures[d]}")

if (c == d):
  print("draw")
elif (d == 1 and c == 0) or (d == 0 and c == 2) or (d == 1 and c == 0):
  print("computer wins!!")
else:
  print("u win")
