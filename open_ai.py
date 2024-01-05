import openai
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key= "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" #"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",
)
MODEL = "gpt-3.5-turbo"

def make_openai_api_call(attack, watermarked_text):
    prompt = attack +" : "+ watermarked_text
    response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": prompt},
    ],
    temperature=0,)
    choices = response.choices
    return choices[0].message.content

