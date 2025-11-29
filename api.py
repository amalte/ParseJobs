import requests
import json

url = "http://localhost:11434/api/generate"
payload = {
    "model": "mistral",
    "prompt": "Tell me a joke about cats."
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
