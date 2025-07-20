# 🎬 Vedantu YouTube Performance Optimizer

A Streamlit‑based web app that automatically suggests improvements for underperforming educational YouTube videos. Paste any Vedantu (or other) YouTube video URL and get back:

- **Optimized Title** (catchy, SEO‑friendly)  
- **Optimized Description** (clear, keyword‑rich)  
- **Optimized Tags** (relevant, diverse)  
- **Thumbnail Concept** (with brief rationale)  

All suggestions come with a short explanation of **why** they’ll perform better.

---

## 🚀 Features

- **Transcript + Metadata Fetch**  
  - Uses the YouTube Data API to pull **title**, **description**, and **tags**.  
  - Uses `youtube-transcript-api` to fetch the auto‑captions transcript (if available).

- **AI‑Powered Optimization**  
  - Calls OpenAI’s GPT‑4 (or GPT‑3.5‑Turbo) via the ChatCompletion API.  
  - Structured prompt ensures clearly labeled output sections.

- **Graceful Fallback**  
  - If no transcript is available, it still optimizes based on metadata only.  
  - Input URLs without valid captions or metadata are detected and handled.

- **Easy Setup**  
  - Pure Python + Streamlit.  
  - Runs locally—no heavy infrastructure required.

---

## 📦 Project Structure

