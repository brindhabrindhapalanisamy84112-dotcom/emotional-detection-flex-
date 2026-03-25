# EmotionSense AI

Multimodal emotion detection — face + voice — running entirely in the browser.

## Deploy on Render

1. Push this folder to a GitHub repo
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Render auto-detects `render.yaml` — just click **Deploy**

Or set manually:
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Environment:** Python 3

## File Structure

```
├── app.py            ← Flask server (serves the two HTML files)
├── index.html        ← Landing page  →  yourapp.onrender.com/
├── detect.html       ← Main app      →  yourapp.onrender.com/detect
├── requirements.txt  ← flask + gunicorn
└── render.yaml       ← Render config (optional)
```

## How it works

All AI runs in the browser — no model files on the server.
Flask only serves the static HTML pages.
