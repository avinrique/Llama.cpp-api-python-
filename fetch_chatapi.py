import requests
import json

API_URL = "http://127.0.0.1:8080"

CHAT = [
    "Hello, Assistant.",
    "Hello. How may I helpou today?",
    "Please tell me the largest city in Europe.",
    "Sure. The largest city in Europe is Moscow, the capital of Russia.",
]

INSTRUCTION = "A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions."

def trim(string):
    return string.strip()

def trim_trailing(string):
    return string.rstrip()

def format_prompt(question):
    prompt = f"{INSTRUCTION}\n### Human: {question}\n### Assistant: "
    return trim_trailing(prompt)

def tokenize(text):
    response = requests.post(f"{API_URL}/tokenize", headers={"Content-Type": "application/json"}, json={"content": text})
    tokens = response.json()["tokens"]
    return tokens

N_KEEP = len(tokenize(INSTRUCTION))

def chat_completion(question):
    prompt = format_prompt(question)
    data = {
        "prompt": prompt,
        "temperature": 0.2,
        "top_k": 40,
        "top_p": 0.9,
        "n_keep": N_KEEP,
        "n_predict": 256,
        "stop": ["\n### Human:"],
        "stream": True
    }

    response = requests.post(f"{API_URL}/completion", headers={"Content-Type": "application/json"}, json=data, stream=True)
    answer = ""

    for line in response.iter_lines():
        if line.startswith(b'data:'):
            content = json.loads(line[5:])["content"]
            print(content, end="")
            answer += content

    print()

    CHAT.extend([question, trim(answer)])


while True:
    question = input(">")
    while  question =="" or question == " ":
        question = input(">")
    chat_completion(question)
