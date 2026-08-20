from fastapi import FastAPI
from pydantic import BaseModel
import yt_dlp

app = FastAPI()

# 👇 1. Yeh check karne ke liye ki server live hai ya nahi
@app.get("/")
async def home():
    return {"status": "success", "message": "VidMate Backend is Live and Running!"}

class Item(BaseModel):
    url: str

# 👇 2. Yeh YouTube link nikalne ke liye
@app.post("/get-link")
async def get_link(item: Item):
    ydl_opts = {
        'format': 'best[ext=mp4]', 
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(item.url, download=False)
        return {"url": info['url'], "title": info['title']}
