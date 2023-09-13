from fastapi import FastAPI,HTTPException
from typing import Optional, List

app = FastAPI()
users = []

@app.post("/create_user/")
def create_user(user_id: int, user_name: str, user_email: str, age: Optional[int] = None, recommendations: Optional[List[str]] = None):
    if user_id in users:
        raise HTTPException(status_code=400, detail="User ID already exists")
    users.append({"user_id": user_id, "user_name": user_name, "user_email": user_email, "age": age, "recommendations": recommendations})
    return {"message": "created", "user_id": user_id}

@app.put("/update_user/{user_id}")
def update_user(user_id: int, user_name: Optional[str] = None, user_email: Optional[str] = None, age: Optional[int] = None, recommendations: Optional[List[str]] = None):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    if user_name is not None:
        users[user_id]["user_name"] = user_name
    if user_email is not None:
        users[user_id]["user_email"] = user_email
    if age is not None:
        users[user_id]["age"] = age
    if recommendations is not None:
        users[user_id]["recommendations"] = recommendations
    return {"message": "updated"}

@app.get("/get_user/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.delete("/delete_user/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return {"message": "deleted"}


create = create_user(1, "axel", "axel@iteso.com")
print(create)

upda = update_user(1, user_name="axel")
print(upda)

get = get_user(1)
print(get)

delete = delete_user(1)
print(delete)