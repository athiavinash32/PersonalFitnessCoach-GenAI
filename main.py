import os
from dotenv import load_dotenv
from google import genai
from utils.config import SYSTEM_PROMPT

import time
import random

load_dotenv()

class ChatAssistant:
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("API key not found")
        
        # creating genai client
        self.client = genai.Client(api_key=self.api_key)

        # system prompt will be the 1st element
        self.history = [{"role":"system","content":SYSTEM_PROMPT}]

        # setting max history as 20
        self.max_history = 20
    
    def add_to_history(self, role, content):
        # adding to history
        self.history.append({"role":role,"content":content})

        # if exceeds 10 turns(20 chats) then keeping the system and the last 10 turn conversation
        if len(self.history) > 20:
            first_ele = [self.history[0]]
            last_twenty_ele = self.history[-self.max_history:]
            self.history = first_ele + last_twenty_ele
    
    def get_conversation_context(self):
        # formatting history as a string
        context = ""
        for msg in self.history:
            context += f"{msg["role"]}: {msg["content"]} \n"
        return context
    
    def chat(self, user_input):
        try:
            # adding user_input to history as "user" role
            self.add_to_history("user",user_input)

            # getting whole formatted context
            context = self.get_conversation_context()

            # calling llm
            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=context
            )
            model_reply = response.text.strip()

            # adding llm response to history with role "assistant"
            self.add_to_history("assistant",model_reply)
            return model_reply
        except Exception as e:
            raise e
    
    def reset_conversation(self):
        # clear chat history expect system prompt
        self.history = [self.history[0]]

def safe_chat(assistant, query, retries=3):
    "Retries with exponential backoff"
    for attempt in range(retries+1):
        try:
            return assistant.chat(query)
        except Exception as e:
            wait_time = 2**attempt + random.random()*0.2
            print(f"Attempt {attempt+1} failed, Retrying in {wait_time} sec {'-'*25}")
            time.sleep(wait_time)
    return "Sorry, the model is busy. Please try again later"


def answer_fitness_query(query, assistant=None):
    try:
        if assistant is None:
            assistant = ChatAssistant()
        return safe_chat(assistant,query)
    except Exception as e:
        print("Error occured while answering query: ",e)
        return e


def main():
    """Main function to demonstrate the fitness coach assistant."""
    print("Personal Fitness Coach - Multi-Turn Chat")
    print("Type 'quit' to exit, 'reset' to start new conversation")
    print("=" * 50)
    
    sample_conversations = [
        [
            "I'm new to working out and want to build muscle. Where should I start?",
            "I can work out 3 days a week.",
            "I can't do pull-ups yet, what alternatives do you suggest?"
        ],
        [
            "I want to lose weight but don't know what to eat.",
            "I eat out a lot and drink soda daily.",
            "I like Italian and Mexican food."
        ]
    ]
    
    assistant = ChatAssistant()
    
    for i, conversation in enumerate(sample_conversations):
        print(f"\n--- Sample Conversation {i+1} ---")
        for query in conversation:
            print(f"\nUser: {query}")
            response = answer_fitness_query(query, assistant)
            print(f"Coach: {response}")
        assistant.reset_conversation() if assistant else None

if __name__ == "__main__":
    main()
