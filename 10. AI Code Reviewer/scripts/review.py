import subprocess
from google import genai
import os
import smtplib   # we can send mail through smtp

def getDiff():
    subprocess.run(["git", "diff"], text=True)
    return diff

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    diff = getDiff()
    prompt = f"Review the code and provide feedback:\n\n Mandatory: provide the output in html that can use to send in mail\n\n{diff}"
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        content=prompt
    )
    html = response.text
    
main()