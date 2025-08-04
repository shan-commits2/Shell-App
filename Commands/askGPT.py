import google.generativeai as genai

def main(args):
    if not args:
        print("[!] Usage: askgpt [your prompt]")
        return
    genai.configure(api_key="YOUR_GEMINI_API_KEY")
    prompt = " ".join(args)
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    print(response.text)
