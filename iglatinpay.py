while True:
  print("please enter the stuff you want to translate or q to quit!")
  text = input()
  if text == "q":
    break
  letter = text[0]
  text = text[1:]
  letter = letter + 'ay'
  print(text + letter)
#test