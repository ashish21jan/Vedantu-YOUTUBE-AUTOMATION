import streamlit as st
import re, requests, os
from youtube_transcript_api import YouTubeTranscriptApi
import openai
from dotenv import load_dotenv

# ─── Load environment ──────────────────────────────────────────────────────────
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
openai.api_key       = os.getenv("OPENAI_API_KEY")

# ─── Helpers ───────────────────────────────────────────────────────────────────
def extract_video_id(url: str) -> str | None:
    for pat in (r"youtu\.be/([^?&]+)", r"youtube\.com/watch\?v=([^?&]+)"):
        m = re.search(pat, url)
        if m:
            return m.group(1)
    return None

def get_transcript(video_id: str) -> str:
    try:
        segs = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([s["text"] for s in segs])
    except:
        return ""

def fetch_metadata(video_id: str, key: str) -> dict:
    resp = requests.get(
        "https://www.googleapis.com/youtube/v3/videos",
        params={"part":"snippet","id":video_id,"key":key}
    ).json()
    items = resp.get("items", [])
    if not items:
        return {}
    sn = items[0]["snippet"]
    return {
        "title":       sn.get("title",""),
        "description": sn.get("description",""),
        "tags":        sn.get("tags", [])
    }

# ─── Core: call OpenAI ─────────────────────────────────────────────────────────
def optimize_content(transcript: str, title: str, description: str, tags: list[str]) -> str:
    system = (
        "You are a YouTube content optimization expert.\n"
        "Given an underperforming educational video, you will suggest:\n"
        "1. An optimized Title (catchy, SEO‑friendly)\n"
        "2. An improved Description (clear, keyword‑rich)\n"
        "3. Better Tags (relevant, diverse)\n"
        "4. A Thumbnail concept with a brief rationale\n"
        "Explain why each suggestion is better.\n"
    )
    user = (
        f"TRANSCRIPT: {transcript or '[Not available]'}\n\n"
        f"CURRENT TITLE: {title}\n\n"
        f"CURRENT DESCRIPTION: {description}\n\n"
        f"CURRENT TAGS: {', '.join(tags)}\n\n"
        "Please respond exactly in this format:\n\n"
        "Optimized Title:\n<your title>\n\n"
        "Why it’s better:\n<reason>\n\n"
        "Optimized Description:\n<your description>\n\n"
        "Why it’s better:\n<reason>\n\n"
        "Optimized Tags:\n<tag1>, <tag2>, …\n\n"
        "Why they’re better:\n<reason>\n\n"
        "Thumbnail Concept:\n<short concept>\n\n"
        "Why it’s better:\n<reason>\n"
    )
    resp = openai.chat.completions.create(
        model="gpt-4.1",                # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": system},
            {"role": "user",   "content": user}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    return resp.choices[0].message.content

# ─── Streamlit UI ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="Vedantu YouTube Performance Optimizer")
st.title("🎬 Vedantu YouTube Performance Optimizer")

url = st.text_input("YouTube URL:", placeholder="https://www.youtube.com/watch?v=…")

if st.button("Optimize"):
    vid = extract_video_id(url.strip())
    if not vid:
        st.error("❌ Invalid YouTube URL.")
    else:
        transcript = get_transcript(vid)
        meta       = fetch_metadata(vid, YOUTUBE_API_KEY)

        if not transcript and not meta:
            st.error("❌ No transcript *and* no metadata found for this video.")
        else:
            if not transcript:
                st.warning("⚠️ Transcript missing — optimizing on metadata only.")
            with st.spinner("🚀 Generating suggestions…"):
                suggestions = optimize_content(
                    transcript,
                    meta.get("title",""),
                    meta.get("description",""),
                    meta.get("tags",[])
                )
            st.markdown("### ⭐️ Suggestions")
            st.write(suggestions)
