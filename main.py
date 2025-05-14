from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from llm_utils import analyze_text
import logging
from dotenv import load_dotenv
load_dotenv()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/book/{book_id}")
def get_book_analysis(book_id: int):
    logger.info(f"Processing request for book ID: {book_id}")
    
    content_url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"
    try:
        logger.info(f"Fetching book content from: {content_url}")
        response = requests.get(content_url)
        response.raise_for_status()
        content = response.text
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching book: {e}")
        raise HTTPException(status_code=404, detail="Book not found")

    try:
        logger.info("Analyzing book content")
        limited_content = content[:3000]
        result = analyze_text(limited_content)
        logger.info("Analysis completed successfully")
        return {"book_id": book_id, "analysis": result}
    except Exception as e:
        logger.error(f"Error analyzing book: {e}")
        raise HTTPException(status_code=500, detail=str(e))
