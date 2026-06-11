#list of responses
greeting = ["hello","hey","hello there","hi"]
how_are_you = ["how are you"]
name = ["what is your name","what's your name"]
thanks = ["thanks", "thank you"]
bye_message = ["exit","bye"]
good_night = ["good night"]
creator = ["who made you", "who created you"]
good_morning = ["good morning"]
help = ["help me"]

#arithmetic keywords
add_keywords = ["add", "plus", "sum"]
sub_keywords = ["subtract", "minus"]
mul_keywords = ["multiply", "times", "product"]
div_keywords = ["divide", "divided by"]

#query keywords
time_keywords = ["what time is it", "current time"]
date_keywords = ["what is today's date", "today's date", "what date is it"]
joke_keywords = ["tell me a joke", "joke"]
age_keywords = ["how old are you", "what is your age"]

#import for date/time queries
import datetime
import re

#helper: extract two numbers from user input
def extract_numbers(text):
    nums = re.findall(r'-?\d+\.?\d*', text)
    if len(nums) >= 2:
        return float(nums[0]), float(nums[1])
    return None, None

#loop
while True:
    #user input
    user_input = input("you: ").strip().lower()

    #if condition
    if user_input in greeting:
        print("Hello!")
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

    #arithmetic commands
    elif any(kw in user_input for kw in add_keywords):
        a, b = extract_numbers(user_input)
        if a is not None:
            print(f"The answer is {a + b}")
        else:
            print("Please provide two numbers. Example: add 5 and 3")
    elif any(kw in user_input for kw in sub_keywords):
        a, b = extract_numbers(user_input)
        if a is not None:
            print(f"The answer is {a - b}")
        else:
            print("Please provide two numbers. Example: subtract 10 from 4")
    elif any(kw in user_input for kw in mul_keywords):
        a, b = extract_numbers(user_input)
        if a is not None:
            print(f"The answer is {a * b}")
        else:
            print("Please provide two numbers. Example: multiply 6 and 7")
    elif any(kw in user_input for kw in div_keywords):
        a, b = extract_numbers(user_input)
        if a is not None:
            if b != 0:
                print(f"The answer is {a / b}")
            else:
                print("Cannot divide by zero!")
        else:
            print("Please provide two numbers. Example: divide 10 by 2")

    #query commands
    elif any(kw in user_input for kw in time_keywords):
        now = datetime.datetime.now().strftime("%I:%M %p")
        print(f"The current time is {now}")
    elif any(kw in user_input for kw in date_keywords):
        today = datetime.datetime.now().strftime("%B %d, %Y")
        print(f"Today's date is {today}")
    elif any(kw in user_input for kw in joke_keywords):
        print("Why do programmers prefer dark mode? Because light attracts bugs!")
    elif any(kw in user_input for kw in age_keywords):
        print("I am a chatbot, I don't have an age!")

    #exit
    elif user_input in bye_message:
        print("Goodbye! Have a nice day!")
        break
    else:
        print("Sorry! I don't understand")