def simple_chatbot(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input.lower():
        return "I'm just a chatbot, but I'm here to help you!"
    elif "what is your name" in user_input.lower():
        return "I'm ChatBot, your virtual assistant."
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"

    else:
        return "I'm sorry, I don't understand that."

# Main loop
print("ChatBot: Hello! I'm here to help. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatBot: Goodbye! Have a great day!")
        break
    response = simple_chatbot(user_input)
    print("ChatBot:", response)
