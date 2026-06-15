import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st
import streamlit.components.v1 as components

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

st.markdown(
"""
<style>

.main {
    background-color:#faf7f2;
}

h1 {
    text-align:center;
    color:#5a4636;
}

</style>
""",
unsafe_allow_html=True
)

st.title("Gift AI")
st.caption("상대의 취향을 분석하는 AI 선물 큐레이터")
st.subheader("AI 맞춤 선물 추천 서비스")

relationship = st.text_input("관계")
age = st.text_input("나이")
preference = st.text_input("취향")
budget = st.selectbox(
    "예산",
    ["1만원 이하", "1~3만원", "3~5만원", "5~10만원", "10만원 이상"]
)
occasion = st.text_input("상황")

if st.button("선물 추천 받기"):

    prompt = f"""
    상대 정보

    관계: {relationship}
    나이: {age}
    취향: {preference}
    예산: {budget}
    상황: {occasion}

    선물 3개 추천하고
    추천 이유도 작성해줘.

    작성할 때:
    - 너무 긴 문장 금지
    - 항목별 줄바꿈 사용
    - 특수문자 ** 사용하지 않기
    """

    response = client.chat.completions.create(
        model="gpt-5.5",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response.choices[0].message.content

    st.success("추천 완료!")

    components.html(
        f"""
        <div style="
        background-color:#f7f5f2;
        padding:25px;
        border-radius:20px;
        font-family:Arial;
        ">

        <h2>AI 추천 선물</h2>

        <p style="font-size:18px; white-space:pre-line;">
        {result}
        </p>

        </div>
        """,
        height=1000
        )