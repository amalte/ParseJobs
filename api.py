import requests
import json

# Parse jobs from a local JSON file
with open("extractedJobs.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

job_description = jobs[0]["jobDescription"]

cover_letter = """Dear Hiring Manager,

I am excited to apply for the position at your company. With over five years of experience in software development, I have built and maintained web and mobile applications using a variety of technologies including React, Node.js, and Python.

In my previous role at AcmeTech, I led a team of developers to deliver scalable solutions for high-traffic applications. I pride myself on writing clean, maintainable code and collaborating effectively with cross-functional teams.

I am enthusiastic about the opportunity to contribute my skills and experience to your organization and am confident that I can help achieve your technical goals.

Thank you for your time and consideration. I look forward to the possibility of discussing my application further.

Sincerely,  
Alex Johnson  
alex.johnson@example.com  
(555) 123-4567
"""

model = "mistral"  # or llama3, qwen2, deepseek, etc.


prompt = f"""
You are an expert career writer and hiring manager. Rewrite the following cover letter
so it aligns directly with the job requirements found in the scraped Indeed job description.

Instructions:
- Clean and interpret the job description even if it contains noise or formatting issues.
- Identify required skills, responsibilities, and tone.
- Rewrite the cover letter to emphasize the applicant's most relevant strengths.
- Preserve the applicant’s voice and background.
- Remove irrelevant content.
- Improve clarity, structure, and professionalism.
- Output only the final polished cover letter.

### JOB DESCRIPTION 
{job_description}

### ORIGINAL COVER LETTER
{cover_letter}

### UPDATED COVER LETTER (TAILORED TO JOB)
"""

url = "http://localhost:11434/api/generate"
payload = {
    "model": model,
    "prompt": prompt
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
