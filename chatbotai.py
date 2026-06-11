#list of responses
greeting = ["hello","hey","hello there","hi"]
how_are_you = ["how are you"]
name = ["what is your name","what's your name"]
thanks = ["thanks", "thank you"]
bye_message = ["exit","bye"]
good_night = ["good night"]
creator = ["who made you", "who created you"]
good_morning = ["good morning"]
help= ["help me"]

#loop
while True:
    #user input
    user_input = input("you: ").strip().lower()
    #if condition
    if user_input in greeting:
        print("Hello")
    elif user_input in how_are_you:
        print("I am good, Thanks for asking!")
    elif user_input in name:
        print("I am a rule-based AI chatbot.")
    elif user_input in thanks:
        print("You're welcome!")
    elif user_input in good_night:
        print("Good night!")
    elif user_input in good_morning:
        print("Good Morning! Hope you have a great day.")
    elif user_input in creator:
        print("I was created as a simple rule-based AI chatbot project.")
    elif user_input in help:
        print("yes sure! what can I help you")
    elif user_input in bye_message:
        print("Goodbye! Have a nice day!")
        break
    else:
        print("Sorry! I don't understand")