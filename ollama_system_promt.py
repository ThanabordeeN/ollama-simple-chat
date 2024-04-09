import ollama
chat_history = [] 

def chat(model='openhermes'):
    system_prompt = "Your Name is Paul ,You are a knowledgeable and helpful AI assistant. Answer questions in a concise and informative way."

    while True:
        user_message = input("You: ")
        chat_history.append({'role': 'user', 'content': user_message})

        messages = [
             {'role': 'system', 'content': system_prompt} # Add the system prompt
        ] + chat_history  

        response = ollama.chat(model=model, messages=messages ,stream=True)
        
        ai_response = response['message']['content']
        print(f"AI: {ai_response}")
        chat_history.append({'role': 'assistant', 'content': ai_response})

chat()
