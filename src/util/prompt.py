import os

'''
프롬프트 파일의 내용을 반환하는 함수를 포함한 모듈
'''


def get_prompt_file_content(file_name):
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
    prompt_file_content = os.path.join(parent_dir, 'prompt', file_name)

    with open(prompt_file_content, 'r') as file:
        return file.read()


def chat_first_prompt():
    return get_prompt_file_content('news_summary_prompt')