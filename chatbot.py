# CodeOrbit Tech - Artificial Intelligence Internship
# Task 1: Rule-Based Chatbot


# This function decides the chatbot's response
# using predefined rules and keywords.
def chatbot_response(user_input):

    # Convert the user's input to lowercase.
    # This allows "Hello", "HELLO", and "hello"
    # to be treated in the same way.
    user_input = user_input.lower().strip()

    # Rule 1: Handle greetings
    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I help you?"

    elif "good morning" in user_input:
        return "Good morning! How can I help you?"

    elif "good afternoon" in user_input:
        return "Good afternoon! How can I help you?"

    elif "good evening" in user_input:
        return "Good evening! How can I help you?"

    # Rule 2: Handle common questions
    elif "how are you" in user_input:
        return "I'm doing well. Thank you for asking!"

    elif "your name" in user_input:
        return "I am a simple rule-based chatbot."

    elif "what can you do" in user_input:
        return "I can answer simple questions using predefined rules."

    elif "ai" in user_input:
        return "AI stands for Artificial Intelligence."

    elif "python" in user_input:
        return "Python is a popular programming language used in Artificial Intelligence."

    elif "thank" in user_input:
        return "You're welcome!"

    # Rule 3: Handle exit words
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a nice day."

    # Rule 4: Fallback response
    # This response is used when no rule or keyword matches.
    else:
        return "Sorry, I don't understand that. Please try asking something else."


# Display the chatbot title
print("===================================")
print("        RULE-BASED CHATBOT")
print("===================================")
print("Chatbot: Hello! Type 'bye' to exit.")


# Keep asking for user input until the user exits.
while True:

    user_message = input("\nYou: ")

    # Get the chatbot's response.
    response = chatbot_response(user_message)

    # Display the response.
    print("Chatbot:", response)

    # End the chatbot when the user enters an exit word.
    if user_message.lower().strip() in ["bye", "goodbye", "exit"]:
        break