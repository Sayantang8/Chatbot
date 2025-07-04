print("Welcome to the Rule-based Chatbot! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()
# Rule-based chatbot queries
    if 'hello'in user_input or 'hi' in user_input:
        print("Chatbot: Hello! How can I assist you today?")
    elif 'your name' in user_input:
        print ("Chatbot: I am a rule-based chatbot created to assist you.")
    elif 'how are you' in user_input:
        print("Chatbot: I'm just a program, but thanks for asking! How can I help you?")
    elif 'help' in user_input:
        print("Chatbot: Sure! What do you need help with?")
    elif 'weather' in user_input:
        print("Chatbot: I can't check the weather, but you can use a weather app or website.")
    elif 'joke' in user_input:
        print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
    elif 'thank you' in user_input:
        print("Chatbot: You're welcome! If you have more questions, feel free to ask.")
    elif 'bye' in user_input:
        print("Chatbot: Goodbye! Have a great day!")
        break
    else:
        print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")