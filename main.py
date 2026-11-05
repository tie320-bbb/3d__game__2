from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="3D First Person World",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# index.html과 main.py를 같은 GitHub 저장소 폴더에 올려 주세요.
html_path = Path(__file__).parent / "index.html"

st.markdown(
    """
    <style>
      .block-container {
        padding-top: 1.2rem;
        padding-bottom: 0.5rem;
        max-width: 1500px;
      }
      header[data-testid="stHeader"] { background: transparent; }
      footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎮 3D 자유 이동 게임")
st.caption(
    "1인칭 시점 · WASD 이동 · SPACE 점프 · 마우스 이동으로 시점 회전 · ESC 일시정지"
)

if not html_path.is_file():
    st.error(
        "index.html 파일을 찾을 수 없습니다. "
        "main.py와 같은 폴더에 index.html을 넣어 주세요."
    )
    st.stop()

# 중요: Pointer Lock은 sandbox iframe에서 차단될 수 있습니다.
# st.html은 iframe을 만들지 않으므로 FPS 방식의 마우스 고정이 가능합니다.
# 로컬 저장소에 있는 신뢰할 수 있는 게임 코드만 실행하세요.
html = html_path.read_text(encoding="utf-8")
st.html(html, width="stretch", unsafe_allow_javascript=True)

st.caption(
    "조작: 게임 시작을 클릭하면 마우스가 화면 중앙에 고정됩니다. "
    "마우스 이동으로 시점을 돌리고, ESC를 누르면 일시정지되어 커서가 해제됩니다. "
    "계속하려면 게임 화면의 계속하기 버튼을 누르세요."
)
