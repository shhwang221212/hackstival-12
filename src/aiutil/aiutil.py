from openai import AzureOpenAI
import os

from dotenv import load_dotenv


'''
AZURE의 OpenAI API를 사용하기 위한 환경 변수를 로드하고, OpenAI Client를 반환하는 함수를 포함한 모듈
'''


# Load environment variables from .env file
def load_env():
    load_dotenv()


# Get OpenAI API key
def get_openai_api_key():
    return os.getenv("AZURE_OPENAI_API_KEY")


# Get OpenAI API endpoint
def get_openai_api_endpoint():
    return os.getenv("AZURE_OPENAI_API_ENDPOINT")


# Get OpenAI API version
def get_openai_api_version():
    return os.getenv("AZURE_OPENAI_API_VERSION")


# Get OpenAI API version date
def get_openai_api_version_date():
    return os.getenv("OPENAI_API_VERSION")


# Get OpenAI API model
def get_deployment_name():
    return os.getenv("DEPLOYMENT_NAME")


# Get OpenAI API model
def get_deployment_embedding_name():
    return os.getenv("DEPLOYMENT_EMBEDDING_NAME")


# Get OpenAI Client
def get_openai_client():
    return AzureOpenAI(
        azure_endpoint=get_openai_api_endpoint(),
        api_key=get_openai_api_key(),
        api_version=get_openai_api_version()
    )
