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
Vedantu-Channel-Optimizer/
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── .env # Environment variables (API keys)
└── README.md # Project documentation



---

## 🛠 Prerequisites

- **Python 3.9+**  
- A **YouTube Data API Key**  
- An **OpenAI API Key** (for GPT‑4 or GPT‑3.5‑Turbo)  
- (Optional) [`pipenv`](https://pipenv.pypa.io/) or [`venv`](https://docs.python.org/3/library/venv.html) for virtual environments  

---

## ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/Vedantu-Channel-Optimizer.git
   cd Vedantu-Channel-Optimizer

**Create & activate a virtual environment**
    python -m venv myenv
    source myenv/bin/activate      # on macOS/Linux
    .\myenv\Scripts\activate       # on Windows

**Install dependencies**

   pip install -r requirements.txt

**Configure your API keys**
   YOUTUBE_API_KEY=YOUR_YOUTUBE_DATA_API_KEY
   OPENAI_API_KEY=YOUR_OPENAI_API_KEY

**Run the app**
   streamlit run app.py


📖 Usage
Paste any YouTube video URL into the input field.

Click Optimize.

Review the AI‑generated:

Optimized Title

Why it’s better

Optimized Description

Why it’s better

Optimized Tags

Why they’re better

Thumbnail Concept

Why it’s better

The app handles videos with or without transcripts, and explains its reasoning for each suggestion.

🔍 How It Works
extract_video_id(url)

Parses standard YouTube URL patterns to pull the video ID.

get_transcript(video_id)

Attempts to fetch the transcript via the youtube-transcript-api.

Returns an empty string if unavailable.

fetch_metadata(video_id, key)

Calls the YouTube Data API to retrieve title, description, and tags.

optimize_content(transcript, title, description, tags)

Builds a system + user prompt for GPT‑4.

Sends it via openai.ChatCompletion.create(...).

Returns the AI’s formatted suggestions.

Streamlit UI

Renders the input field, buttons, and displays the AI output.

🔧 Troubleshooting
“Invalid YouTube URL”

Make sure your URL matches one of:
https://www.youtube.com/watch?v=VIDEO_ID
https://youtu.be/VIDEO_ID

“Transcript missing — optimizing on metadata only”

The video has no public captions; the app will still generate metadata‑based suggestions.

“Error fetching metadata”

Check your YOUTUBE_API_KEY and quota usage.

OpenAI Authentication Errors

Verify your OPENAI_API_KEY in the .env file and ensure it’s active.

💡 Tips & Next Steps
Long Transcripts

GPT‑4’s 8K token window handles most full transcripts, but you can chunk or summarize very long videos before optimizing.

Thumbnail Previews

For a fully automated pipeline, integrate DALL·E (or any image‑generation API) to produce thumbnail mockups from the “Thumbnail Concept.”

Alternative Models

You can also use gpt-3.5-turbo for a lower‑cost option. Just swap the model name in app.py:

python
Copy
Edit
resp = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    …
)
🤝 Contributing
Contributions, issues, and feature requests are welcome! Please:

Fork the repo

Create a feature branch (git checkout -b feature/YourFeature)

Commit your changes (git commit -m 'Add YourFeature')

Push to your branch (git push origin feature/YourFeature)

Open a Pull Request

📜 License
This project is released under the MIT License. See LICENSE for details.

Built with ❤️ by Aashish Ranjan
Project for Vedantu YouTube Performance Optimizer Challenge













