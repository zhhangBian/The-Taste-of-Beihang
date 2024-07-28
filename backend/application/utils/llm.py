import httpx
from openai import OpenAI

with open('api_key', 'r') as file:
    api_key = file.readline().strip()

client = OpenAI(
    base_url="https://api.xty.app/v1",
    api_key=api_key,
    http_client=httpx.Client(
        base_url="https://api.xty.app/v1",
        follow_redirects=True,
    ),
)


def getLLMresponse(content: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an assistant to help people find out what they dishes would like to eat."},
            {"role": "user", "content": content}
        ]
    )
    return completion.choices[0].message.content
