from fastapi import FastAPI
from pydantic import BaseModel
import yt_dlp

app = FastAPI()

class Item(BaseModel):
    url: str

@app.post("/get-link")
async def get_link(item: Item):
    ydl_opts = {
        'format': 'best[ext=mp4]', 
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = yt_dlp.extract_info(item.url, download=False)
        return {"url": info['url'], "title": info['title']}