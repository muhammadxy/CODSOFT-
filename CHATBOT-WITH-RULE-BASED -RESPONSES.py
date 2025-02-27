import re

# Define rules as a dictionary
rules = {
    r'hello|hi': "Hello! How can I assist you today?",
    r'how are you': "I'm just a bot, but I'm here to help you!",
    r'what is your name': "I'm a customer service chatbot created to assist you.",
    r'bye': "Goodbye! Have a great day!",
    r'help|support': "Sure, I'm here to help. Can you please provide more details about the issue?",
    r'order status': "Please provide your order number, and I'll check the status for you.",
    r'refund': "I'm sorry to hear that you want a refund. Please provide your order number, and I'll assist you with the process.",
    r'return': "Returning an item? Please provide your order number and the reason for the return.",
    r'shipping': "Shipping information? Please provide your location and I'll give you the details.",
    r'product details': "Sure, please specify the product name or model number, and I'll provide the details.",
    r'complaint': "I'm sorry to hear that you have a complaint. Please provide the details, and I'll address it as soon as possible.",
    r'feedback': "Thank you for your feedback! Please share your thoughts, and we'll use them to improve our services.",
}

# Function to process input and match it to rules
def match_rule(user_input):
    user_input = user_input.lower().strip()  # Convert to lowercase and strip whitespace
    user_input = re.sub(r'[^\w\s]', '', user_input)  # Remove punctuation
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
    return "Can you please rephrase?"

# Main function to run the chatbot
def chatbot():
    print("Chatbot: Hi! How can I help you today? (Type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = match_rule(user_input)
        print(f"Chatbot: {response}")
##calling the chatbots functions
if __name__ == "__main__":
    chatbot()
