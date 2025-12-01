import json

import requests
from dotenv import load_dotenv
import os

from constants import build_cover_letter_prompt

load_dotenv()  # read .env file
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL = os.getenv("LLM_MODEL")


def isJuniorJob(job_description):
    payload = {
        "model": MODEL,
        "prompt": f"Respond ONLY with true or false.\nIs the following job a junior level role?\n\n{job_description}"
    }

    response = requests.post(f"{OLLAMA_BASE_URL}/api/generate", json=payload, stream=True)

    full_response = ""
    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                full_response += data.get("response", "")
            except json.JSONDecodeError:
                continue

    result = full_response.strip().lower()
    print("MODEL RESULT:", result)

    return result == "true"

def generate_improved_cover_letter():
    with open("extractedJobs.json", "r", encoding="utf-8") as f:
        jobs = json.load(f)

    job_description = jobs[0]["jobDescription"]

    url = f"{OLLAMA_BASE_URL}/api/generate"
    payload = {
        "model": MODEL,
        "prompt": build_cover_letter_prompt(job_description)
    }

    response = requests.post(url, json=payload, stream=True)

    full_text = ""

    for line in response.iter_lines():
        if not line:
            continue

        data = json.loads(line.decode("utf-8"))

        if "response" in data:
            full_text += data["response"]

        if data.get("done"):
            break

    print("Final output:\n")
    print(full_text)
