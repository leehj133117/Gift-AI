import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def recommend_gift(user_info):

    prompt = f"""
너는 선물 추천 전문가야.

사용자 정보:
{user_info}

조건:
- 선물 3개 추천
- 가격 고려
- 추천 이유 설명
- 너무 흔한 선물 제외

답변 형식:
선물:
이유:
"""

    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            { "role": "user", "content": prompt }
        ]
    )

    return response.choices[0].message.content


info = input(
"""
관계, 나이, 성격, 예산, 상황을 입력하세요:
"""
)

result = recommend_gift(info)

print("\n===== 추천 결과 =====")
print(result)
