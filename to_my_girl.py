# app.py
# 💖 升级版：星空动画 + 爱心小游戏 + 情话点击切换
# 运行：
# pip install streamlit
# streamlit run app.py

import streamlit as st
from datetime import datetime, date
import random
import time

st.set_page_config(page_title="写给最爱的你 ❤️", page_icon="💖", layout="wide")

# ---------------- 星空动画背景 ----------------
st.markdown("""
<style>
.main {
    background: radial-gradient(ellipse at bottom, #0d1b2a 0%, #000000 100%);
    overflow: hidden;
}

/* 星星 */
.stars {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    width: 100%; height: 100%;
    background: transparent;
    box-shadow:
        100px 200px #FFF, 200px 50px #FFF, 300px 300px #FFF,
        400px 150px #FFF, 500px 250px #FFF, 600px 100px #FFF,
        700px 200px #FFF, 800px 50px #FFF, 900px 300px #FFF,
        1000px 150px #FFF, 1100px 250px #FFF, 1200px 100px #FFF;
    animation: animStar 60s linear infinite;
}

@keyframes animStar {
    from {transform: translateY(0px);} 
    to {transform: translateY(-2000px);} 
}

h1, h2, h3 {text-align:center; color:white;}

.stButton>button {
    background: linear-gradient(45deg,#ff4b6e,#ff758c);
    color:white; border-radius:25px; height:3em; font-size:18px;
}

.block-container {z-index:1;}
</style>
<div class="stars"></div>
""", unsafe_allow_html=True)

# ---------------- 初始化 session ----------------
if "score" not in st.session_state:
    st.session_state.score = 0

if "quote_index" not in st.session_state:
    st.session_state.quote_index = 0

# ---------------- 标题 ----------------
st.title("🌌 写给世界上最可爱的你")
st.subheader("在宇宙的某个角落，我们刚好相遇")
st.markdown("---")

# ---------------- 恋爱时间 ----------------
st.header("⏳ 我们已经在一起多久了")
start_date = st.date_input("选择我们在一起的那一天", date(2024,1,1))

today = date.today()
days = (today - start_date).days

c1, c2, c3 = st.columns(3)
c1.metric("已经相爱", f"{days} 天 ❤️")
c2.metric("小时", f"{days*24:,}")
c3.metric("分钟", f"{days*24*60:,}")

st.markdown("---")

# ---------------- 爱心点击小游戏 ----------------
st.header("🎮 爱心收集小游戏")
st.write("规则：每点一次爱心，就代表我多喜欢你一点 💕")

col1, col2 = st.columns([1,2])

with col1:
    if st.button("❤️ 点我"):
        st.session_state.score += 1

with col2:
    st.metric("当前爱意值", st.session_state.score)

# 达到不同分数触发彩蛋
if st.session_state.score == 10:
    st.success("喜欢你已经无法隐藏了！")
if st.session_state.score == 50:
    st.balloons()
    st.success("已经超级超级喜欢你了！")
if st.session_state.score == 100:
    st.snow()
    st.success("满分喜欢，只有你一个人。")

st.markdown("---")

# ---------------- 今日情话（可点击切换） ----------------
st.header("💬 今日情话")

quotes = [
"遇见你，是我写过最美的程序。",
"如果生活是代码，你就是唯一的主函数。",
"世界有很多变量，而你是我的常量。",
"喜欢你不是三分钟热度，是无限循环。",
"想和你从函数开始，一直运行到白头。",
"你一笑，我的世界就完成了一次正确编译。",
"别人是心动，我是持续心动。",
]

st.success(quotes[st.session_state.quote_index])

if st.button("换一句看看 💞"):
    st.session_state.quote_index = (st.session_state.quote_index + 1) % len(quotes)
    st.rerun()

st.markdown("---")

# ---------------- 照片墙 ----------------
st.header("📸 我们的回忆")
st.info("把照片命名为 photo1.jpg / photo2.jpg / photo3.jpg 放同目录")

col1, col2, col3 = st.columns(3)
col1.image("photo1.jpg", caption="我们的某一天", use_container_width=True)
col2.image("photo2.jpg", caption="一起去过的地方", use_container_width=True)
col3.image("photo3.jpg", caption="我最喜欢的瞬间", use_container_width=True)

st.markdown("---")

# ---------------- 纪念日倒计时 ----------------
st.header("🎂 下一个纪念日")
future = st.date_input("选择一个重要的日子", date(2026,1,1))
remain = (future - today).days

if remain >= 0:
    st.metric("还有", f"{remain} 天")
else:
    st.warning("这个日子已经过去啦，我们再创造新的回忆吧～")

st.markdown("---")

st.markdown("<h3 style='text-align:center;color:white;'>❤️ 这个宇宙很大，但我只想和你一起探索 ❤️</h3>", unsafe_allow_html=True)


