# app.py
# 💖 写给女朋友的专属浪漫网站（全中文版本）
# 运行方法：
# pip install streamlit
# streamlit run app.py

import streamlit as st
from datetime import datetime, date
import time

st.set_page_config(page_title="写给最爱的你 ❤️", page_icon="💖", layout="wide")

# ---------------- 页面美化 ----------------
st.markdown("""
<style>
.main {background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);} 
h1, h2, h3 {text-align:center; color:white;}
.stButton>button {background:#ff4b6e; color:white; border-radius:20px; height:3em; font-size:18px;}
</style>
""", unsafe_allow_html=True)

# ---------------- 标题 ----------------
st.title("💌 写给世界上最可爱的你")
st.subheader("这是我专门为你做的小网站")
st.markdown("---")

# ---------------- 在一起多久 ----------------
st.header("⏳ 我们已经在一起多久了")
start_date = st.date_input("选择我们在一起的那一天", date(2024,1,1))

today = date.today()
days = (today - start_date).days

c1, c2, c3 = st.columns(3)
c1.metric("已经相爱", f"{days} 天 ❤️")
c2.metric("小时", f"{days*24:,}")
c3.metric("分钟", f"{days*24*60:,}")

st.markdown("---")

# ---------------- 惊喜按钮 ----------------
st.header("🎁 点这里有惊喜")
if st.button("点我 💕"):
    with st.spinner("正在准备惊喜..."):
        time.sleep(1.5)
    st.success("我会一直一直喜欢你，不止今天，是每一天。")
    st.balloons()

st.markdown("---")

# ---------------- 留言 ----------------
st.header("📝 给我留言")
name = st.text_input("你的名字")
msg = st.text_area("想对我说的话")

if st.button("发送 ❤️"):
    if name and msg:
        st.success(f"已收到 {name} 的留言 💌")
    else:
        st.warning("要写完才能发送哦～")

st.markdown("---")

# ---------------- 照片墙 ----------------
st.header("📸 我们的回忆")
st.info("把你们的照片命名为 photo1.jpg / photo2.jpg 放在同目录即可显示")

col1, col2, col3 = st.columns(3)
col1.image("photo1.jpg", caption="第一次约会", use_container_width=True)
col2.image("photo2.jpg", caption="一起去的地方", use_container_width=True)
col3.image("photo3.jpg", caption="我最喜欢的一张", use_container_width=True)

st.markdown("---")

# ---------------- 每日情话 ----------------
st.header("💬 今日情话")
quotes = [
"遇见你之后，所有的等待都值得。",
"你不是突然闯进我的生活，是我等了很久的人。",
"世界很大，但我只想去有你的地方。",
"你在的话，日子就不普通。",
"喜欢你这件事，我打算用一辈子证明。"
]

st.success(quotes[datetime.now().day % len(quotes)])

st.markdown("---")

# ---------------- 倒计时 ----------------
st.header("🎂 下一个纪念日倒计时")
future = st.date_input("选择一个重要的日子", date(2026,1,1))
remain = (future - today).days

if remain >= 0:
    st.metric("还有", f"{remain} 天")
else:
    st.warning("这个日子已经过去啦，我们换一个～")

st.markdown("---")

st.markdown("<h3>❤️ 这个网站不是模板，是我认真写给你的 ❤️</h3>", unsafe_allow_html=True)
