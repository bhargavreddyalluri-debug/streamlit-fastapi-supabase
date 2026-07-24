from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client

app = FastAPI()

SUPABASE_URL = "https://gnpszplqeypygkaagmzo.supabase.co"
SUPABASE_KEY = "sb_publishable_W6BshPuGf9NNIsI61LRg1w_IFPOi_cT"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class User(BaseModel):
    name: str
    email: str
    password: str

@app.post("/register")
def register(user: User):

    data = {
        "name": user.name,
        "email": user.email,
        "password": user.password
    }

    result = supabase.table("users").insert(data).execute()

    return {
        "message": "Registration Successful",
        "data": result.data
    }