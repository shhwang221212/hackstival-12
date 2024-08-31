import streamlit as st

import aiutil.aiutil as aiutil


def main():
    st.title("사내뉴스")
    st.write("This is a Streamlit app.")

    aiutil.get_openai_client()




if __name__ == "__main__":
    main()
