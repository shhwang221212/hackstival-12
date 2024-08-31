import os

'''
프롬프트 파일의 내용을 반환하는 함수를 포함한 모듈
'''


def get_prompt_file_content(file_name):
    current_dir = os.path.dirname(__file__)
    parant_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    prompt_file_content = os.path.join(parant_dir, file_name)
    with open(prompt_file_content, 'r') as file:
        return file.read()


def chat_first_prompt():
    return get_prompt_file_content('firstprompt.txt')