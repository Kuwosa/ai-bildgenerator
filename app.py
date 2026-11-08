import os
import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client, Client

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SUPABASE_URL = "https://nvmcqrgorswwjldlqaqi.supabase.co"
SUPABASE_ANON_KEY = "sb_publishable__Ew3Su-rdIHaXRfag7oWVg_-jWSDN-j"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

class PromptRequest(BaseModel):
    prompt_text: str

@app.get("/")
def read_root():
    return {"status": "AI Backend för Llama & Flux körs på Vast.ai!"}

@app.post("/generate")
def generate_image(request: PromptRequest):
    try:
        print(f"Tar emot prompt: {request.prompt_text}")
        time.sleep(2)
        mock_image_url = "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe"

        return {
            "success": True, 
            "prompt": request.prompt_text, 
            "image_url": mock_image_url
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
