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
    "초원/용암 전장 · 중앙 조준선 · ENTER 투사체/충전 사격(최대 7발, 0.7초당 1발 충전) · F 참격 연계 · Ctrl 대시 참격 · X자 후 수평 파동 참격 · 더블 점프 후 Shift 급강하 충격파 · 레벨 10 용암 드래곤 보스전 · 플레이어 무적 · ESC 일시정지"
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
    "더블 점프를 습득한 뒤 급강하 충격파 스킬까지 배우면 공중에서 두 번째 점프를 한 후 Shift를 눌러 빠르게 착지하며 주변에 충격파를 일으킵니다. Ctrl 대시 참격을 배우면 Ctrl을 눌러 바라보는 방향으로 돌진하고 경로상의 적을 베어냅니다. 충전 사격은 투사체 하나를 모으는 데 0.7초가 걸리며, 확장 장전 스킬을 추가로 배우면 최대 7발까지 저장할 수 있습니다. 레벨 10을 달성하고 레벨업 스킬 선택을 마치면 보스 도전 안내가 나타납니다. O 키를 누르면 일반 큐브가 사라지고 용암 전장에서 거대한 날아다니는 드래곤과 전투합니다. 드래곤은 날개를 퍼덕이며 플레이어 주변을 선회하고, 약 4.4초마다 공격력 24의 화염구 4발을 부채꼴로 발사합니다. 현재 보스전의 플레이어는 무적이며 화염구에 맞아도 피해를 받지 않습니다. 드래곤은 체력 2400으로 설정되어 있으며 플레이어의 투사체 공격으로 피해를 줄 수 있습니다. N 또는 ESC를 누르면 보스 도전을 거절하고 일반 전투를 계속합니다. 초원에서는 빨간 적 큐브 하나가 플레이어를 따라옵니다. 적을 맞히면 명중 수와 경험치가 올라가며, 레벨업하면 공격력 증가, F 참격, 더블 점프, 강화 투사체(푸른색), 충전 사격 등 조건에 맞는 아직 습득하지 않은 무작위 스킬 최대 3개 중 하나를 1/2/3 키로 선택합니다. X자 참격 후 수평 파동 참격은 X자 연계 습득 후, 급강하 충격파는 더블 점프 습득 후, 확장 장전은 충전 사격 습득 후 후보에 포함됩니다. 한 번 배운 스킬은 다시 등장하지 않으며, 스킬 선택 중에는 게임 시간이 멈춥니다. "
    "ESC로 일시정지합니다."
)
