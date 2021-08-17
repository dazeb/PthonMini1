# Python mini projects 2021
# DazEB 2021

print("Welcome to the game!")

#playing = daz user input
#playing = input()
#"Name: "daz

playing = input("Would you like to play? ")

if playing.lower() != "yes":
  quit()

print("Ok, Lets's Play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
  print("Correct!")
  score += 1
else:
  print("Incorrect")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
  print("Correct!")
  score += 1
else:
  print("Incorrect")

print("You got " + str(score) + " questions correct")  

