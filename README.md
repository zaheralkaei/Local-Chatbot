# Chatbot with Ollama Model

This is a Python-based chatbot using the Ollama language model from the `langchain_community.llms` package. The chatbot allows users to interact with an AI model in real-time, providing dynamic responses based on conversation history. 
## Features

- Interactive chatbot with real-time input/output
- Use of the Ollama model from LangChain for generating responses
- Conversation history maintained to provide coherent responses
- A "thinking" animation that runs in a separate thread while the model is processing
- Simple exit mechanism by typing `exit`

## Prerequisites

To run this chatbot, you will need Python 3.7 or higher and the following libraries installed:

### Required Libraries

- `langchain_community`: This library is required to load and use the Ollama model.
- `threading` and `time`: These are standard Python libraries used to handle the "thinking" animation and timed events.
- `logging`: Used to suppress unwanted logging output from some external libraries (like `urllib3`).

### Ollama Model

The chatbot uses the Ollama language model, which must be installed separately. 

To install the Ollama model:

1. **Download the Ollama CLI tool** from the [Ollama official website](https://ollama.com/download).
   - You will need to follow the installation instructions for your operating system (Windows, macOS, or Linux).
  
2. **Once installed**, verify that the Ollama CLI is working by running the following command in your terminal:
   `ollama --help`

3. Install the desired Ollama model, for example llama2, using the following command:

`ollama pull llama3.1`

After installing the model, the chatbot will be able to load it via the Ollama interface in the langchain_community.llms library.

### Python Library Installation
You can install the necessary Python libraries using pip. Run the following command in your terminal:

`pip install langchain_community`

### Usage
Run the Chatbot: You can start the chatbot by running the main function in your terminal:

`python chatbot.py`
Interacting with the Bot: Once the chatbot is running, you can type your messages after the You: prompt, and the bot will generate responses. You can exit the chat at any time by typing exit.

Thinking Animation: While the bot is generating a response, you'll see an animated "thinking" symbol that runs until the bot completes its response.

### Code Explanation
-Thinking Animation: A separate thread is created to run the show_thinking_symbol function, which displays a rotating symbol to indicate the bot is thinking. This thread stops once the bot generates a response.

-Ollama Model: The chatbot uses the Ollama model from LangChain to generate responses. You can specify the model variant by changing the llm = Ollama(model="llama3.1") line.

-Conversation History: The bot keeps track of all messages in the conversation, ensuring that responses are contextual. If the conversation history becomes too long, it is truncated to prevent memory overflow.

### Customization
Model Selection: You can customize the chatbot to use different Ollama models by modifying the llm = Ollama(model="llama3.1") line.

Conversation Management: You can adjust the conversation history limits by modifying the max_tokens variable to suit your memory requirements.

### Error Handling
The code includes basic error handling for cases where the model initialization or response generation fails. Errors are printed to the console without breaking the program.
