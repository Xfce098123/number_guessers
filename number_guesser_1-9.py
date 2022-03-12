import random

number = "1234567890"
length = 1

temp = random.sample(number,length)
random_number = "".join(temp)


print("welcome to the guessing game(i have 3 more types with 3 digits, 9-0, 1-100, 1-1000)")
print("")
print("you have 3 tries to guess the number, good luck")
ans = input ("go, YOU CURRENTLY HAVE 3 TRIES REMAINING :")
if ans.lower() == random_number:
  print("WELL DONE")
else:
  print("wrong, -1")

ans = input ("guess the number, YOU CURRENTLY HAVE 2 TRIES :")
if ans.lower() == random_number:
  print("well done")
else:
  print("wrong, -1")

ans = input ("guess the number, YOU CURRENTLY HAVE 1 TRY :")
if ans.lower() == random_number:
  print("well done")
else:
  print("wrong, -1")

saved_score = input ("how much did you get? :")
print("oh thats great, " + saved_score + " is my lucky number!")
print("")
print("tell us how much you got by supporting our github, https://github.com/Xfce098123")