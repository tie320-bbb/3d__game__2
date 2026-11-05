from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="3D First Person World",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Streamlit Cloud 저장소에 index.html과 main.py를 함께 올려 주세요.
html_path = Path(__file__).parent / "index.html"

st.markdown(
    """
    <style>
      .block-container {padding-top: 1.2rem; padding-bottom: 0.5rem; max-width: 1500px;}
      header[data-testid="stHeader"] {background: transparent;}
      footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎮 3D 자유 이동 게임")
st.caption("1인칭 시점 · WASD 이동 · SPACE 점프 · 회색 바닥 · 외부 CDN 및 3D 라이브러리 미사용")

if not html_path.exists():
    st.error("index.html 파일을 찾을 수 없습니다. main.py와 같은 폴더에 index.html을 넣어 주세요.")
    st.stop()

html = html_path.read_text(encoding="utf-8")
components.html(html, height=740, scrolling=False)

st.caption("조작: 게임 화면을 한 번 클릭한 뒤 WASD 또는 방향키로 이동하세요. 스페이스바로 점프하고, 마우스 왼쪽 버튼을 누른 채 움직이면 시점이 회전합니다.")
