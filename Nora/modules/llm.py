import requests
from config import LLMsetup as LS
import pandas as pd
import re
import time

# Load and parse training data
df = pd.read_csv("raw_dataset.csv")
training_pairs = []
for _, row in df.iterrows():
    match = re.match(r".*### Human:\s*(.*?)\s*### Assistant:\s*(.*)", row["text"])
    if match:
        training_pairs.append({
            "prompt": match.group(1).strip(),
            "completion": match.group(2).strip()
        })

# Create context from dataset
context = ""
for pair in training_pairs:
    context += f"Q: {pair['prompt']}\nA: {pair['completion']}\n\n"

def LLM(user_input, stop_event=None):
    if stop_event and stop_event.is_set():
        return None  # exit early

    start_time = time.time()
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "mistral",
            "stream": False,
            "messages": [
                {"role": "system", "content": context},
                {"role": "user", "content": user_input}
            ]
        }
    )
    elapsed_time = time.time() - start_time
    
    return (int(elapsed_time), 
            response.json()["message"]["content"])
