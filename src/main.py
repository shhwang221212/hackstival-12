import streamlit as st

import util.ai_util as aiutil
import util.prompt as prompt
import util.news_crawler as crawler


def main():
    # 환경변수 로드
    aiutil.load_env()

    # OpenAI Client 생성
    openai_client = aiutil.get_openai_client()

    # 챗봇 생성
    create_chat(openai_client)

    # 뉴스 크롤러 생성
    # crawler.crawler_naver_test()
    crawler.crawler_google_test()

    st.title("hackathon12")
    st.write("헥스티벌 12조")


def create_chat(client):
    client = aiutil.get_openai_client()
    response = client.chat.completions.create(
        model=aiutil.get_deployment_name(),
        messages=[
            {
                "role": "system",
                "content": prompt.chat_first_prompt()
            }
        ]
    )

    st.write(response.choices[0].message.content)


if __name__ == "__main__":
    main()


