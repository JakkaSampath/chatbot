import ollama

def chat_with_local_model(prompt, history=[]):
    # Add the user's message to the history
    history.append({'role': 'user', 'content': prompt})

    response = ollama.chat(
        model='llama3',  # or 'mistral', 'gemma', etc.
        messages=history
    )

    message = response['message']['content']
    history.append({'role': 'assistant', 'content': message})
    return message, history

if __name__ == "__main__":
    print("Chat with me:")
    chat_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        reply, chat_history = chat_with_local_model(user_input, chat_history)
        print("Bot:", reply)