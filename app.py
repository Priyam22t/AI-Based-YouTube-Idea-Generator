import streamlit as st

from backend.ai_engine import generate_youtube_ideas
from backend.trends_service import get_trending_topics
from backend.youtube_service import search_youtube
from backend.viral_score import calculate_viral_score

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AI YouTube Idea Generator",
    page_icon="🎬",
    layout="centered"
)

# ---------- STYLES ----------
st.markdown("""
<style>
    .card {
        background-color: #1e1e1e;
        padding: 16px;
        border-radius: 14px;
        margin-bottom: 14px;
        border: 1px solid #2a2a2a;
    }
    .idea {
        font-size: 18px;
        font-weight: 600;
        color: #ffffff;
    }
    .badge {
        display: inline-block;
        background-color: #ff4b4b;
        color: white;
        padding: 4px 12px;
        border-radius: 18px;
        font-size: 12px;
        margin-left: 10px;
    }
    .reason {
        font-size: 13px;
        color: #bbbbbb;
        margin-top: 6px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🎬 AI-Based YouTube Idea Generator")
st.caption("Generate viral YouTube ideas using trends + smart scoring")

# ---------- INPUTS ----------
niche = st.text_input("📌 Channel Niche", "AI Tools")
audience = st.selectbox(
    "🎯 Target Audience",
    ["Beginners", "Students", "Creators", "Professionals"]
)
tone = st.selectbox(
    "🎭 Tone",
    ["Educational", "Entertaining", "Motivational", "Technical"]
)
content_type = st.radio(
    "📹 Content Type",
    ["Long Videos", "Shorts"],
    horizontal=True
)

# ---------- SESSION STATE ----------
if "trends" not in st.session_state:
    st.session_state.trends = get_trending_topics(niche)

if "selected_trend" not in st.session_state:
    st.session_state.selected_trend = niche

# ---------- GENERATE IDEAS ----------
if st.button("🚀 Generate Ideas"):

    ideas = generate_youtube_ideas(
        st.session_state.selected_trend,
        audience,
        tone
    )

    st.subheader("💡 AI-Generated Ideas")

    for i, idea in enumerate(ideas, 1):
        viral_score, reasons = calculate_viral_score(idea, content_type)

        st.markdown(
            f"""
            <div class="card">
                <span class="idea">{i}. {idea}</span>
                <span class="badge">🔥 {viral_score}% Viral</span>
                <div class="reason">
                    Why it works: {", ".join(reasons)}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ---------- DOWNLOAD ----------
    st.download_button(
        label="📥 Download Ideas",
        data="\n".join(ideas),
        file_name="youtube_ideas.txt",
        key="download_ideas_main"
    )

# ---------- TRENDING TOPICS ----------
st.subheader("🔥 Trending Topics")

cols = st.columns(2)
for idx, trend in enumerate(st.session_state.trends):
    with cols[idx % 2]:
        if st.button(trend, key=f"trend_{idx}"):
            st.session_state.selected_trend = trend
            st.success(f"Using trend: **{trend}**")
            st.rerun()

# ---------- REFRESH TRENDS ----------
if st.button("🔄 Refresh Trending Topics"):
    st.session_state.trends = get_trending_topics(niche)
    st.rerun()

# ---------- RELATED YOUTUBE VIDEOS ----------
st.subheader("📺 Related YouTube Videos")

videos = search_youtube(niche)

for video in videos:
    st.markdown(
        f"""
        <div class="card">
            ▶️ <a href="{video['url']}" target="_blank"
                 style="color:#ffffff; text-decoration:none;">
                {video['title']}
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
