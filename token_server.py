from fastapi import FastAPI, Query
from jose import jwt
from datetime import datetime, timedelta

# Replace with your actual values from LiveKit Cloud Console
LIVEKIT_API_KEY = "your_api_key_here"
LIVEKIT_API_SECRET = "your_api_secret_here"

app = FastAPI()

@app.get("/token")
def generate_token(identity: str = Query(...), room: str = Query(...)):
    now = datetime.utcnow()
    exp = now + timedelta(hours=1)

    payload = {
        "iss": LIVEKIT_API_KEY,
        "sub": identity,
        "exp": int(exp.timestamp()),
        "video": {
            "roomJoin": True,
            "room": room
        }
    }

    token = jwt.encode(payload, LIVEKIT_API_SECRET, algorithm="HS256")
    return {"token": token}
