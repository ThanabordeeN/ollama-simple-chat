import ollama

chat_history = []  # Start with an empty conversation history

def chat(model='openhermes'):
    while True:
        user_message = input("You: ")
        chat_history.append({'role': 'user', 'content': user_message})

        response = ollama.chat(
            model=model, 
            messages=chat_history  # Include the history in every request
        )
        ai_response = response['message']['content']
        print(f"AI: {ai_response}")

        chat_history.append({'role': 'assistant', 'content': ai_response})

chat()