
# 🎬 Vedantu YouTube Performance Optimizer

A Streamlit web app that automatically analyzes underperforming Vedantu (or any educational) YouTube videos and suggests improvements to their metadata and thumbnail concept.  
Paste a YouTube video URL and get AI-generated recommendations for:

- Optimized Title (catchy, SEO-friendly)  
- Enhanced Description (clear, keyword-rich)  
- Improved Tags (relevant, diverse)  
- Thumbnail Concept with rationale  

Each suggestion is accompanied by an explanation of why it will help improve performance.

---

## 🚀 Features

- Fetches video transcript (if available) and metadata (title, description, tags) using YouTube APIs  
- Uses OpenAI GPT-4 (or GPT-3.5 Turbo) for intelligent content optimization  
- Gracefully handles videos without transcripts by optimizing based on metadata only  
- Clean, user-friendly interface via Streamlit  
- Clear, structured output for easy implementation

---

## 📦 Project Structure



Vedantu-Channel-Optimizer/
 1. app.py             # Main Streamlit application
 2. requirements.txt   # Python dependencies
 3. .env               # Environment variables (API keys)
 4. README.md          # This documentation file

````

---

## 🛠 Prerequisites

- Python 3.9 or higher  
- YouTube Data API Key ([Get here](https://developers.google.com/youtube/v3/getting-started))  
- OpenAI API Key ([Get here](https://platform.openai.com/account/api-keys))  

---

## ⚙️ Installation

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/Vedantu-Channel-Optimizer.git
   cd Vedantu-Channel-Optimizer
````

2. Create and activate a virtual environment

   ```bash
   python -m venv myenv
   # Windows
   .\myenv\Scripts\activate
   # macOS/Linux
   source myenv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your API keys:

   ```env
   YOUTUBE_API_KEY=your_youtube_data_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

---

## 🚀 Running the App

Start the Streamlit app with:

```bash
streamlit run app.py
```

Open your browser to [http://localhost:8501](http://localhost:8501), paste the YouTube video URL, and click **Optimize**.

---

## 🧩 How It Works

* Extracts the video ID from the URL
* Fetches the transcript (if available) and metadata (title, description, tags)
* Sends this data in a structured prompt to OpenAI’s GPT model
* Receives and displays AI-generated suggestions with explanations

---

## 📝 Usage Notes

* If the transcript is unavailable, the app will optimize based on metadata alone
* The output includes clearly labeled sections for easy copy-paste
* Supports any public YouTube video URL

---

## 🔧 Troubleshooting

* **Invalid YouTube URL:** Ensure the URL is complete and correct
* **Missing Transcript:** Some videos do not have transcripts; this is normal
* **API Errors:** Verify your API keys and quota limits
* **OpenAI Rate Limits:** If you hit limits, try reducing frequency or switch to `gpt-3.5-turbo` in `app.py`

---

## 💡 Customization

* Change the model in `app.py` between `"gpt-4"` and `"gpt-3.5-turbo"` for cost/performance tradeoffs
* Enhance prompt templates inside `optimize_content()` for different output formats or additional fields
* Integrate thumbnail image generation APIs (e.g., DALL·E) for full automation

---

## 🤝 Contribution

Contributions are welcome! Please open issues or pull requests for bugs, improvements, or feature ideas.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by Aashish Ranjan
Project for Vedantu YouTube Performance Optimizer Challenge

```
```
