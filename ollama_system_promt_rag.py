import ollama
chat_history = [] 
def load_context(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
    
def chat(model='openhermes'):
    context = load_context("./context.txt")  # Load context before loop
    context = str(context)
    system_prompt = f"Your Name is Paul ,You are a knowledgeable and helpful AI assistant. Answer questions in a concise and informative way, and answer with context :{context}"

    while True:
        user_message = input("You: ")
        chat_history.append({'role': 'user', 'content': user_message})

        messages = [
            {'role': 'system', 
             'content': system_prompt}  # System prompt
        ] + chat_history
        response = ollama.chat(model=model, messages=messages )
        ai_response = response['message']['content']

        print(f"AI: {ai_response}")
        chat_history.append({'role': 'assistant', 'content': ai_response})

chat()
