# app.py
# 💖 升级版（修复星空显示问题）
# pip install streamlit
# streamlit run app.py

import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="写给最爱的你 ❤️", page_icon="💖", layout="wide")

# ---------------- 修复后的真正全屏星空背景 ----------------
st.markdown("""
<style>
/* 让 Streamlit 默认白背景透明 */
[data-testid="stAppViewContainer"] {
    background: transparent;
}

.main {
    background: transparent;
}

/* 星空层（关键：放在最底层 fixed + z-index） */
body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: #000;
    z-index: -2;
}

body::after {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 200%;
    height: 200%;
    background-image:
        radial-gradient(2px 2px at 20px 30px, white, transparent),
        radial-gradient(2px 2px at 40px 70px, white, transparent),
        radial-gradient(1px 1px at 90px 40px, white, transparent),
        radial-gradient(2px 2px at 160px 120px, white, transparent),
        radial-gradient(1px 1px at 200px 200px, white, transparent),
        radial-gradient(2px 2px at 300px 150px, white, transparent),
        radial-gradient(1px 1px at 350px 80px, white, transparent);
    background-repeat: repeat;
    background-size: 400px 400px;
    animation: starsMove 60s linear infinite;
    z-index: -1;
    opacity: 0.8;
}

@keyframes starsMove {
    from {transform: translateY(0);} 
    to {transform: translateY(-400px);} 
}

h1, h2, h3 {
    text-align: center;
    color: white;
}

/* 卡片半透明，制造悬浮感 */
section[data-testid="stSidebar"],
div[data-testid="stMetric"],
div.stButton {
    backdrop-filter: blur(6px);
}

.stButton>button {
    background: linear-gradient(45deg,#ff4b6e,#ff758c);
    color: white;
    border-radius: 25px;
    height: 3em;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- session 状态 ----------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "quote_index" not in st.session_state:
    st.session_state.quote_index = 0

# ---------------- 页面内容 ----------------
st.title("🌌 写给世界上最可爱的你")
st.subheader("在同一片星空下，我们刚好相爱")
st.markdown("---")

# 恋爱时间
st.header("⏳ 我们已经在一起多久了")
start_date = st.date_input("选择我们在一起的那一天", date(2024,1,1))

today = date.today()
days = (today - start_date).days

c1, c2, c3 = st.columns(3)
c1.metric("已经相爱", f"{days} 天 ❤️")
c2.metric("小时", f"{days*24:,}")
c3.metric("分钟", f"{days*24*60:,}")

st.markdown("---")

# 爱心小游戏
st.header("🎮 爱心收集小游戏")
st.write("每点一次，就多喜欢你一点 💕")

if st.button("❤️ 点我"):
    st.session_state.score += 1

st.metric("当前爱意值", st.session_state.score)

if st.session_state.score == 20:
    st.balloons()
    st.success("喜欢你这件事，正在指数级增长！")

st.markdown("---")

# 情话切换
st.header("💬 今日情话")

quotes = [
"你是我宇宙里的唯一确定性。",
"所有星星都在证明，我正在爱你。",
"如果世界是代码，你就是最终运行结果。",
"我不看月亮，只看你。",
"浪漫不是突然，是我蓄谋已久的喜欢。"
]

st.success(quotes[st.session_state.quote_index])

if st.button("换一句看看 💞"):
    st.session_state.quote_index = (st.session_state.quote_index + 1) % len(quotes)
    st.rerun()

st.markdown("---")

# 照片墙
st.header("📸 我们的回忆")
st.info("把照片命名为 photo1.jpg / photo2.jpg / photo3.jpg 放同目录")

col1, col2, col3 = st.columns(3)
col1.image("photo1.jpg", use_container_width=True)
col2.image("photo2.jpg", use_container_width=True)
col3.image("photo3.jpg", use_container_width=True)

st.markdown("---")

st.markdown("<h3 style='text-align:center;color:white;'>❤️ 抬头是星空，低头是你 ❤️</h3>", unsafe_allow_html=True)


