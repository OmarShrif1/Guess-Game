import random
import eel

number = random.randint(1, 1000)

print("\n")

@eel.expose
def CheckNumber(input):
    input = int(input)
    if input == number:
        return "You Win!"
    elif input > number:
        return "Down"
    else:
        return "Up"
    
@eel.expose
def start(number1,number2):
    global number
    number = random.randint(int(number1),int(number2))

@eel.expose
def restart():
    global number
    number = random.randint(1, 1000)

eel.init("gui")
eel.start("index.html", size=(500, 500))