from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

class Assessment(BaseModel):
    name: str
    url: str
    remote_testing: str
    adaptive_irt: str
    duration: str
    test_type: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend", response_model=List[Assessment])
def recommend(data: QueryRequest):
    query = data.query.lower()
    assessments = [
        {
            "name": "Java Developer Test",
            "url": "https://www.shl.com/java-test",
            "remote_testing": "Yes",
            "adaptive_irt": "No",
            "duration": "40 mins",
            "test_type": "Technical"
        },
        {
            "name": "Cognitive Ability Test",
            "url": "https://www.shl.com/cognitive-test",
            "remote_testing": "Yes",
            "adaptive_irt": "Yes",
            "duration": "30 mins",
            "test_type": "Cognitive"
        },
        {
            "name": "Python Developer Test",
            "url": "https://www.shl.com/python-test",
            "remote_testing": "Yes",
            "adaptive_irt": "Yes",
            "duration": "60 mins",
            "test_type": "Technical"
        },
        {
            "name": "Personality Profile Assessment",
            "url": "https://www.shl.com/personality-test",
            "remote_testing": "Yes",
            "adaptive_irt": "No",
            "duration": "25 mins",
            "test_type": "Personality"
        }
    ]
    results = [a for a in assessments if any(word in a["name"].lower() for word in query.split())]
    return results[:10] if results else assessments[:2]