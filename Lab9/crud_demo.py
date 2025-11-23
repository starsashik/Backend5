# crud_demo.py
from sqlalchemy.orm import Session

from database import SessionLocal
from models import User, Post


def add_users(db: Session):
    users = [
        User(username="alice", email="alice@example.com", password="pass1"),
        User(username="bob", email="bob@example.com", password="pass2"),
        User(username="charlie", email="charlie@example.com", password="pass3"),
    ]
    db.add_all(users)
    db.commit()


def add_posts(db: Session):
    # допустим, посты для alice и bob
    alice = db.query(User).filter_by(username="alice").first()
    bob = db.query(User).filter_by(username="bob").first()

    posts = [
        Post(title="Alice first post", content="Hello from Alice", user_id=alice.id),
        Post(title="Alice second post", content="More text", user_id=alice.id),
        Post(title="Bob's post", content="Bob is here", user_id=bob.id),
    ]
    db.add_all(posts)
    db.commit()


def get_all_users(db: Session):
    users = db.query(User).all()
    print("\nВсе пользователи:")
    for u in users:
        print(u.id, u.username, u.email)


def get_all_posts_with_users(db: Session):
    posts = db.query(Post).all()
    print("\nВсе посты с пользователями:")
    for p in posts:
        print(p.id, p.title, "->", p.user.username, p.user.email)


def get_posts_by_username(db: Session, username: str):
    user = db.query(User).filter_by(username=username).first()
    print(f"\nПосты пользователя {username}:")
    if not user:
        print("Пользователь не найден")
        return
    for p in user.posts:
        print(p.id, p.title, p.content)


def update_user_email(db: Session, username: str, new_email: str):
    user = db.query(User).filter_by(username=username).first()
    if user:
        user.email = new_email
        db.commit()
        print(f"Email пользователя {username} обновлён на {new_email}")


def update_post_content(db: Session, post_id: int, new_content: str):
    post = db.query(Post).get(post_id)
    if post:
        post.content = new_content
        db.commit()
        print(f"Контент поста {post_id} обновлён.")


def delete_post(db: Session, post_id: int):
    post = db.query(Post).get(post_id)
    if post:
        db.delete(post)
        db.commit()
        print(f"Пост {post_id} удалён.")


def delete_user_and_posts(db: Session, username: str):
    user = db.query(User).filter_by(username=username).first()
    if user:
        db.delete(user)
        db.commit()
        print(f"Пользователь {username} и все его посты удалены.")


if __name__ == "__main__":
    db = SessionLocal()

    # 1) добавление
    add_users(db)
    add_posts(db)

    # 2) выборка
    get_all_users(db)
    get_all_posts_with_users(db)
    get_posts_by_username(db, "alice")

    # 3) обновление
    update_user_email(db, "alice", "alice_new@example.com")
    update_post_content(db, 1, "Updated content for post 1")

    # 4) удаление
    delete_post(db, 3)
    delete_user_and_posts(db, "bob")

    db.close()
