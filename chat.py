import streamlit as st

from dotenv import load_dotenv
from llm import get_ai_response

st.set_page_config(page_title = "소득세 챗봇", page_icon="🐱‍👤")

st.title("🐱‍👤 소득세 챗봇")
st.caption("소득세에 관련된 모든것을 답해드립니다!")

load_dotenv()

# Session State also supports attribute based syntax
if 'message_list' not in st.session_state:
    st.session_state.message_list = []

# 우리의 chat_input은 사용자의 질문이다.    
for message in st.session_state.message_list:
    with st.chat_message(message["role"]): # 채팅이 입력될 때마다 메세지창에 대화 출력
        st.write(message["content"])
        
        
if user_question := st.chat_input(placeholder="소득세에 궁금한 내용들을 말씀해주세요!"):
    with st.chat_message("user"): # 채팅이 입력될 때마다 메세지창에 대화 출력
        st.write(user_question)
    st.session_state.message_list.append({"role":"user", "content":user_question}) # 채팅 정보에 user정보와 user_question(채팅내역)이 함께 들어감
    
    with st.spinner("답변을 생성하는 중입니다."):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"): # 채팅이 입력될 때마다 메세지창에 대화 출력
            ai_message = st.write_stream(ai_response)
        st.session_state.message_list.append({"role":"ai", "content":ai_message})
