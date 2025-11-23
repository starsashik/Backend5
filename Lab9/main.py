# main.py
from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import get_db
from models import User, Post

app = FastAPI()
templates = Jinja2Templates(directory="templates")


# --- USERS ---

@app.get("/users")
def list_users(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse(
        "users.html",
        {"request": request, "users": users}
    )


@app.get("/users/create")
def create_user_form(request: Request):
    return templates.TemplateResponse(
        "user_form.html",
        {"request": request, "user": None}
    )


@app.post("/users/create")
def create_user(
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        db: Session = Depends(get_db)
):
    user = User(username=username, email=email, password=password)
    db.add(user)
    db.commit()
    return RedirectResponse(url="/users", status_code=303)


@app.get("/users/{user_id}/edit")
def edit_user_form(user_id: int, request: Request, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    return templates.TemplateResponse(
        "user_form.html",
        {"request": request, "user": user}
    )


@app.post("/users/{user_id}/edit")
def edit_user(
        user_id: int,
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        db: Session = Depends(get_db)
):
    user = db.query(User).get(user_id)
    user.username = username
    user.email = email
    user.password = password
    db.commit()
    return RedirectResponse(url="/users", status_code=303)


@app.post("/users/{user_id}/delete")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if user:
        db.delete(user)
        db.commit()
    return RedirectResponse(url="/users", status_code=303)


# --- POSTS ---

@app.get("/posts")
def list_posts(request: Request, db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return templates.TemplateResponse(
        "posts.html",
        {"request": request, "posts": posts}
    )


@app.get("/posts/create")
def create_post_form(request: Request, db: Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse(
        "post_form.html",
        {"request": request, "post": None, "users": users}
    )


@app.post("/posts/create")
def create_post(
        title: str = Form(...),
        content: str = Form(...),
        user_id: int = Form(...),
        db: Session = Depends(get_db)
):
    post = Post(title=title, content=content, user_id=user_id)
    db.add(post)
    db.commit()
    return RedirectResponse(url="/posts", status_code=303)


@app.get("/posts/{post_id}/edit")
def edit_post_form(post_id: int, request: Request, db: Session = Depends(get_db)):
    post = db.query(Post).get(post_id)
    users = db.query(User).all()
    return templates.TemplateResponse(
        "post_form.html",
        {"request": request, "post": post, "users": users}
    )


@app.post("/posts/{post_id}/edit")
def edit_post(
        post_id: int,
        title: str = Form(...),
        content: str = Form(...),
        user_id: int = Form(...),
        db: Session = Depends(get_db)
):
    post = db.query(Post).get(post_id)
    post.title = title
    post.content = content
    post.user_id = user_id
    db.commit()
    return RedirectResponse(url="/posts", status_code=303)


@app.post("/posts/{post_id}/delete")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).get(post_id)
    if post:
        db.delete(post)
        db.commit()
    return RedirectResponse(url="/posts", status_code=303)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)