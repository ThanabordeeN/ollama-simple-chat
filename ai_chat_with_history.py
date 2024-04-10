
import ollama

def chat():
    """
    This function allows the user to have a conversation with an AI assistant.
    It initializes an empty list to store the chat history and prompts the user for input.
    The input is then added to the chat history and passed to the AI model for processing.
    The model's response is printed and added to the chat history.
    The conversation continues until the user decides to exit.
    """
    chat_history = []  # Initialize an empty list to store the chat history
    
    while True:
        system_prompt = "Your Name is Paul ,You are a knowledgeable and helpful AI assistant. Answer questions in a concise and informative way."
        input_text = input("You: ")
        fullchat = []
        
        if input_text.strip():
            chat_history.append({'role': 'user', 'content': f'{input_text}'})  # Append the user's message to the chat history
            
            messages = [{'role': 'system', 'content': system_prompt}] + chat_history  # Add the system prompt and chat history
            
            stream = ollama.chat(
                model='mistral:7b-instruct-v0.2-q5_K_M',
                messages=messages,
                stream=True,
            )
            
            print("Assistant: ", end='', flush=True)
            
            for chunk in stream:
                print(chunk['message']['content'], end='', flush=True)  # Print the model's message
                fullchat.append(chunk['message']['content'])  # Append the model's message to the chat history
            print('\n')
            fullchat = ''.join(fullchat)
            chat_history.append({'role': 'assistant', 'content': fullchat})
            

chat()

