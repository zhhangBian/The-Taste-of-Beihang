import httpx
from openai import OpenAI

from WhatToEatInHang import settings

# with open('api_key.json', 'r') as file:
#     api_key = json.load(file).get("llm_api")
api_key = settings.LLM_API

client = OpenAI(
    base_url="https://api.xty.app/v1",
    api_key=api_key,
    http_client=httpx.Client(
        base_url="https://api.xty.app/v1",
        follow_redirects=True,
    ),
)


url = "https://stardustlm.zhipin.com/api/gpt/open/chat/openai/send/msg"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IiIsInV1aWQiOiJuYmdfY3NsX3BhcnRuZXJfcGxheWVyOS02NTkzNDhlZS1lZDcyLTQxZGEtYWYwZi05N2E2MGE1MGExMGUifQ.9hTvhNxwncrLvVPG-utFFdUmZDNXA3YmvkWl-RGDJm8'
}

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


if __name__ == "__main__":
    print(getLLMresponse("你好吗"))
