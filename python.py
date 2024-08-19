print("Hello")
#Asking the user for input
inp= input("Tell me your name: \n")
print("Your name is: "+ inp)

prompt = 'What the speed of light?\n'
speed_of_light = int(input(prompt))
time = 'what time does it take to reach the earth?\n'
time_taken= int(input(time))
distance = int(speed_of_light * time_taken)
print(str(distance) + 'Km')