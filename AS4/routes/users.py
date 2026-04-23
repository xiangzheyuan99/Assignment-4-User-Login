from fastapi import APIRouter
from models.user import User, UserSignUp, UserSignIn

user_router = APIRouter()

@user_router.post("/signup")
async def sign_up(user: UserSignUp):
    existing_user = await User.find_one(User.username == user.username)
    if existing_user:
        return {"message": "Username already exists"}

    existing_email = await User.find_one(User.email == user.email)
    if existing_email:
        return {"message": "Email already exists"}

    new_user = User(
        email=user.email,
        username=user.username,
        password=user.password
    )
    await new_user.insert()
    return {"message": "User created successfully"}

@user_router.post("/signin")
async def sign_in(user: UserSignIn):
    existing_user = await User.find_one(User.username == user.username)

    if not existing_user:
        return {"message": "User not found"}

    if existing_user.password != user.password:
        return {"message": "Incorrect password"}

    return {
        "message": "Sign in successful",
        "username": existing_user.username,
        "email": existing_user.email
    }

@user_router.post("/signout")
async def sign_out():
    return {"message": "Sign out successful"}