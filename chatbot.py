# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 14:45:29 2024
This is a basic local chatbot powered by Ollama
@author: zaher Alkaei
"""
import threading
import time
from langchain_community.llms import Ollama
import logging

logging.getLogger("urllib3").setLevel(logging.WARNING)

# Function to display the "thinking" symbol
def show_thinking_symbol(stop_event):
    symbols = ['|', '/', '-', '\\']
    i = 0
    while not stop_event.is_set():
        print(f"\rBot is thinking {symbols[i % len(symbols)]}", end="")
        time.sleep(0.2)
        i += 1
    print("\r", end="")  # Clear the line when done

# Chatbot powered by Ollama from langchain.llms
def main():
    print("Welcome to Chat! You are chatting with Ollama.\n")
    print("At anytime you can type 'exit' to leave this chat.\n")
    role_prompt = "You are a useful chatbot."

    # Initialize conversation history
    conversation_history = role_prompt + "\n"
    
    try:
        # Choose the model you want to use
        llm = Ollama(model="llama3.1")
    except Exception as e:
        print(f"Error initializing the model: {e}")
        return

    while True:
        user_input = input("You: ")
        
        # A command to end the chat
        if user_input.lower() == 'exit':
            print("Exiting Chat. Goodbye!")
            break
        
        print()  # Line break after user input

        # Append user input to the conversation history
        conversation_history += f"User: {user_input}\nBot:"
        
        # Create an event to signal when to stop the thinking animation
        stop_event = threading.Event()

        # Start the thinking animation in a separate thread
        thinking_thread = threading.Thread(target=show_thinking_symbol, args=(stop_event,))
        thinking_thread.start()
        
        try:
            # Generate response from the LLM using conversation history 
            response = llm.invoke(conversation_history)
        except Exception as e:
            print(f"Error generating response: {e}")
            stop_event.set()  # Stop thinking animation in case of error
            thinking_thread.join()  # Wait for the animation thread to finish
            continue
        
        # Stop the thinking animation once the response is ready
        stop_event.set()
        thinking_thread.join()  # Wait for the animation thread to finish
        
        # Append the response to the conversation history
        conversation_history += f" {response}\n"
        
        # Optional: Truncate or summarize the history if it becomes too long
        max_tokens = 3000  # You can adjust this value based on your model limits
        if len(conversation_history.split()) > max_tokens:
            # Simple truncation, or you could implement a summarization technique here
            conversation_history = role_prompt + "\n" + conversation_history.split("User:")[-2]
            print("(Conversation history truncated to manage memory)\n")
        
        # Print the response
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    main()

