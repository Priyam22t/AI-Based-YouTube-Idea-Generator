# 🎬 AI-Based YouTube Idea Generator

An AI-powered YouTube video idea generator built with **Streamlit + Python** that helps creators discover **viral video ideas** using trending topics, smart viral-scoring logic, and real YouTube data.

---

## 🚀 Features

### ✅ AI-Powered Idea Generation
Generate YouTube video ideas based on:
- Channel niche
- Target audience
- Content tone
- Video type (Long-form or Shorts)

### 🔥 Viral Score System
Each idea receives a **viral probability score** calculated using:
- Power words (Why, Top, Secrets, Mistakes, etc.)
- Title length optimization
- CTR-friendly phrasing patterns
- Content type (Shorts vs Long Videos)

### 🧠 “Why This Works” Explanation
Every generated title includes:
- Reason for high click-through potential
- Power words detected in the title
- Audience relevance logic
- Long-form vs Shorts suitability

### 📈 Trending Topics Integration
- Fetches trending topics dynamically
- Click a trend to instantly regenerate ideas
- Refresh trends anytime

### 📺 Real YouTube Video Research
- Displays real related YouTube videos
- Click any title to open the video directly on YouTube
- Helps with competitor analysis and inspiration

### 🎯 Shorts Hook Generator (0–3 Seconds)
- Generates scroll-stopping hooks for Shorts
- Optimized for attention and retention

### 🗓️ 7-Day Content Calendar
- Automatically converts ideas into a weekly content plan
- Helps creators stay consistent and organized

### 📥 Export & Download
- Download all generated ideas as a `.txt` file
- Duplicate download button issues handled using unique keys

---

## 🖥️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **APIs & Logic:**
  - YouTube Data API (video search & research)
  - PyTrends (Google Trends – optional)
  - Custom viral scoring engine
- **Environment Management:** `.env`
- **Version Control:** Git + GitHub

---

## 📁 Project Structure

```
ai-based-youtube-idea-generator/
│
├── app.py
├── requirements.txt
├── .env
│
├── backend/
│   ├── ai_engine.py
│   ├── viral_score.py
│   ├── youtube_service.py
│   └── trends_service.py
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-based-youtube-idea-generator.git
cd ai-based-youtube-idea-generator
```

### 2️⃣ Create & Activate Environment (Anaconda Recommended)
```bash
conda create -n yt_idea_gen python=3.10
conda activate yt_idea_gen
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the root directory:
```env
YOUTUBE_API_KEY=your_youtube_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here   # optional
SERPAPI_KEY=your_serpapi_key_here         # optional
```

---

## ▶️ Run the App
```bash
streamlit run app.py
```

Open your browser at:
```
http://localhost:8501
```

---

## 🧪 Current AI Mode
- Uses **logic-based AI generation** for stability and reliability
- Architecture supports **drop-in replacement** with:
  - Gemini API
  - OpenAI API
- No UI changes required when switching to real AI models

---

## 🔮 Future Enhancements
- Real-time Gemini / OpenAI prompt tuning
- SEO keyword & hashtag generator
- Thumbnail text suggestions
- Monetization strategy insights
- Multi-language support
- User login and saved projects
- Analytics-based idea scoring

---

## 🛡️ Security Notes
- Never commit your `.env` file
- Keep API keys private
- Always add `.env` to `.gitignore`

---

## 🤝 Contributing
Contributions are welcome!
1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a pull request

---

## 📜 License
This project is licensed under the **MIT License**.

---

## ⭐ Support
If you found this project helpful:
- ⭐ Star the repository
- 🐛 Report issues
- 💡 Suggest new features

Happy creating & go viral 🚀🎥
