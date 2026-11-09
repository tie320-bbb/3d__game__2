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
    "1인칭 시점 · WASD 이동 · 방향키 시점 조정 · SPACE 점프 · "
    "초록 잔디 바닥 · 중앙 조준선 · ENTER 투사체/충전 사격 · F 참격 연계 · X자 후 수평 파동 참격 · 더블 점프 후 Shift 급강하 충격파 · 무작위 레벨업 스킬 · ESC 일시정지"
)

if not html_path.is_file():
    st.error(
        "index.html 파일을 찾을 수 없습니다. "
        "main.py와 같은 폴더에 index.html을 넣어 주세요."
    )
    st.stop()

html = html_path.read_text(encoding="utf-8")
st.html(html, width="stretch", unsafe_allow_javascript=True)

st.caption(
    "조작: P로 게임 시작/계속, WASD로 이동, 방향키로 시점 회전, "
    "SPACE로 점프하고 화면 중앙 조준선으로 조준해 ENTER로 발사합니다. 충전 사격 습득 후에는 ENTER를 짧게 눌러 단발 발사하거나 길게 눌러 투사체를 장전한 뒤 놓아 연속 발사합니다. F 참격은 X자 연계 스킬 습득 시 두 번째 참격이 이어지고, 수평 파동 참격까지 배우면 마지막에 청록색 원거리 파동을 날립니다. "
    "더블 점프를 습득한 뒤 급강하 충격파 스킬까지 배우면 공중에서 두 번째 점프를 한 후 Shift를 눌러 빠르게 착지하며 주변에 충격파를 일으킵니다. 초록 잔디 바닥에서 빨간 적 큐브 하나가 플레이어를 따라옵니다. 적을 맞히면 명중 수와 경험치가 올라가며, 레벨업하면 공격력 증가, F 참격, 더블 점프, 강화 투사체(푸른색), 충전 사격 등 조건에 맞는 아직 습득하지 않은 무작위 스킬 최대 3개 중 하나를 1/2/3 키로 선택합니다. X자 참격 후 수평 파동 참격은 X자 연계 습득 후, 급강하 충격파는 더블 점프 습득 후 후보에 포함됩니다. 한 번 배운 스킬은 다시 등장하지 않으며, 스킬 선택 중에는 게임 시간이 멈춥니다. "
    "ESC로 일시정지합니다."
)
