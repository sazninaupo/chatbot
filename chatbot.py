import re

print("Chatbot: Hello! I am your friendly chatbot. Type 'exit' to end the chat.")
while True:
    user_input = input("You: ").strip().lower()

    print(f"DEBUG: User Input - {user_input}")  # Debugging line to check input

    # Predefined responses
    if user_input == "exit":
        print("Chatbot: Bye! Have a great day!")
        break
    elif re.search(r"\bhello\b|\bhi\b", user_input):
        print("Chatbot: Hi there! How can I help you?")
    elif re.search(r"how are you", user_input):
        print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
    elif re.search(r"your name", user_input):
        print("Chatbot: I'm your Python-made chatbot! What's your name?")
    elif re.search(r"\bupo\b", user_input):
        print("Chatbot: pagla 😆")
    elif re.search(r"who is mahin", user_input):
        print("Chatbot: Mahin is a calm, shy, and intelligent person! 😌")
    
    else:
        print("Chatbot: Sorry, I don't understand that. Can you try asking something else?")
