"""
RESTful API для лабораторной работы по FastAPI.
"""

import json
import os
import uuid
import hashlib
import time
from datetime import datetime
from typing import List, Optional
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request, Response, Form, UploadFile, File, Cookie
from fastapi.responses import FileResponse, RedirectResponse
from pydantic import BaseModel, field_validator

# Временное "хранилище" данных
users_db = []
FILES_STORAGE = "uploaded_files"
SECRET_KEY = "your-secret-key-here"

# Создаем папку для файлов
os.makedirs(FILES_STORAGE, exist_ok=True)


class UserRegister(BaseModel):
    """Модель для регистрации нового пользователя."""

    username: str
    email: str
    password: str

    @field_validator('password')
    @classmethod
    def validate_password_length(cls, password_value: str) -> str:
        """Проверяет, что пароль содержит минимум 6 символов."""
        if len(password_value) < 6:
            raise ValueError('Пароль должен содержать минимум 6 символов')
        return password_value

    @field_validator('username')
    @classmethod
    def validate_username_length(cls, username_value: str) -> str:
        """Проверяет, что имя пользователя содержит минимум 3 символа."""
        if len(username_value) < 3:
            raise ValueError('Имя пользователя должно содержать минимум 3 символа')
        return username_value

    @field_validator('email')
    @classmethod
    def validate_email_format(cls, email_value: str) -> str:
        """Проверяет базовый формат email адреса."""
        if '@' not in email_value:
            raise ValueError('Некорректный email адрес')
        return email_value


class UserLogin(BaseModel):
    """Модель для входа пользователя."""

    username: str
    password: str


class User(BaseModel):
    """Модель пользователя системы."""

    id: int
    username: str
    email: str
    password: str


async def initialize_test_data():
    """Инициализирует тестовые данные при запуске приложения."""
    if not users_db:
        users_db.append(User(
            id=1,
            username="test_user",
            email="test@example.com",
            password="password123"
        ))


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Управляет событиями жизненного цикла приложения.
    """
    # Startup
    await initialize_test_data()
    yield
    # Shutdown
    print("Application shutting down")


# Создание экземпляра FastAPI с lifespan
app = FastAPI(
    title="My Lab API",
    version="1.0.0",
    description="RESTful API для лабораторной работы по FastAPI",
    lifespan=lifespan
)


@app.get("/")
async def root() -> dict:
    """
    Возвращает приветственное сообщение.
    """
    return {"message": "Hello, World!"}


@app.get("/greet/{name}")
async def greet_user(name: str) -> dict:
    """
    Приветствует пользователя по имени.
    """
    return {"message": f"Hello, {name}!"}


@app.get("/search")
async def search_query(query: str, limit: Optional[int] = 10) -> dict:
    """
    Обрабатывает поисковый запрос.
    """
    return {
        "message": f"You searched for: {query}",
        "limit": limit
    }


@app.get("/json")
async def get_json_data() -> dict:
    """
    Возвращает JSON с данными о студенте.
    """
    user_data = {
        "name": "Лубенец Александр",
        "age": 20,
        "hobbies": ["программирование", "чтение"],
        "university": "Политех",
        "course": 3
    }
    return user_data


@app.get("/file")
async def get_text_file() -> FileResponse:
    """
    Генерирует и возвращает текстовый файл.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_content = f"""Это содержимое текстового файла.
Создано для лабораторной работы по FastAPI.
Дата создания: {current_time}
Студент: Лубенец Александр
Группа: 231-333
"""

    filename = "example.txt"
    filepath = os.path.join(FILES_STORAGE, filename)

    with open(filepath, "w", encoding="utf-8") as file_obj:
        file_obj.write(file_content)

    return FileResponse(filepath, filename=filename, media_type='text/plain')


@app.get("/redirect")
async def redirect_to_root() -> RedirectResponse:
    """
    Выполняет перенаправление на главную страницу.
    """
    return RedirectResponse(url="/")


@app.get("/headers")
async def get_request_headers(request: Request) -> dict:
    """
    Возвращает все заголовки входящего запроса.
    """
    headers = dict(request.headers)
    return {
        "headers": headers,
        "client_host": request.client.host,
        "method": request.method
    }


@app.get("/set-cookie")
async def set_cookie_values(response: Response) -> dict:
    """
    Устанавливает cookies для клиента.
    """
    response.set_cookie(
        key="username",
        value="Lubenets_Alexander",
        max_age=3600,
        httponly=True
    )
    response.set_cookie(
        key="session_id",
        value=str(uuid.uuid4()),
        max_age=3600
    )
    return {"message": "Cookies установлены"}


@app.get("/get-cookie")
async def get_cookie_values(
        username: Optional[str] = Cookie(None),
        session_id: Optional[str] = Cookie(None)
) -> dict:
    """
    Возвращает значения cookies из запроса.
    """
    cookies = {}
    if username:
        cookies["username"] = username
    if session_id:
        cookies["session_id"] = session_id

    if cookies:
        return {"cookies": cookies}

    return {"message": "Cookies не найдены"}


@app.post("/login")
async def login_user(username: str = Form(...), password: str = Form(...)) -> dict:
    """
    Выполняет аутентификацию пользователя через форму.
    """
    if username == "admin" and password == "password":
        return {"message": f"Welcome, {username}!"}

    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.post("/register")
async def register_user(user_data: UserRegister) -> dict:
    """
    Регистрирует нового пользователя в системе.
    """
    # Проверяем, нет ли уже пользователя
    for user in users_db:
        if user.username == user_data.username:
            raise HTTPException(status_code=400, detail="Username already exists")
        if user.email == user_data.email:
            raise HTTPException(status_code=400, detail="Email already registered")

    # Создаем нового пользователя
    new_user = User(
        id=len(users_db) + 1,
        username=user_data.username,
        email=user_data.email,
        password=user_data.password
    )

    users_db.append(new_user)

    return {
        "message": f"User {user_data.username} registered successfully!",
        "user_id": new_user.id
    }


@app.get("/users", response_model=List[User])
async def get_all_users() -> List[User]:
    """
    Возвращает список всех зарегистрированных пользователей.
    """
    return users_db


@app.get("/users/{user_id}", response_model=User)
async def get_user_by_id(user_id: int) -> User:
    """
    Возвращает пользователя по-указанному ID.
    """
    for user in users_db:
        if user.id == user_id:
            return user

    raise HTTPException(status_code=404, detail="User not found")


@app.post("/upload")
async def upload_file_handler(file: UploadFile = File(...)) -> dict:
    """
    Загружает файл на сервер.
    """
    file_location = os.path.join(FILES_STORAGE, file.filename)

    with open(file_location, "wb") as file_obj:
        content = await file.read()
        file_obj.write(content)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content),
        "message": "File uploaded successfully"
    }


def create_jwt_token(data: dict) -> str:
    """
    Создает JWT токен для аутентификации.
    """
    # Простая реализация без внешних библиотек
    payload = data.copy()
    payload['exp'] = time.time() + 3600  # 1 час
    token = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    return token


@app.post("/auth/login")
async def authenticate_user(login_data: UserLogin) -> dict:
    """
    Выполняет аутентификацию и возвращает JWT токен.
    """
    if login_data.username == "admin" and login_data.password == "password":
        token = create_jwt_token({"sub": login_data.username})
        return {
            "access_token": token,
            "token_type": "bearer",
            "message": "Login successful"
        }

    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/protected")
async def access_protected_route(token: str) -> dict:
    """
    Предоставляет доступ к защищенному маршруту при наличии валидного токена.
    """
    try:
        if token:  # Простая проверка наличия токена
            return {
                "message": "This is a protected route",
                "user": "admin",
                "data": "Secret information here!"
            }

        raise HTTPException(status_code=401, detail="Invalid token")
    except Exception as exc:
        raise HTTPException(status_code=401, detail="Invalid token") from exc


@app.get("/info")
async def get_application_info() -> dict:
    """
    Возвращает общую информацию о приложении.
    """
    return {
        "app_name": "My Lab API",
        "version": "1.0.0",
        "developer": "Студент",
        "total_users": len(users_db),
        "total_files": len(os.listdir(FILES_STORAGE)) if os.path.exists(FILES_STORAGE) else 0
    }


@app.get("/test")
async def test_application() -> dict:
    """
    Тестовый маршрут для проверки работоспособности API.
    """
    return {
        "status": "success",
        "message": "API работает корректно!",
        "timestamp": datetime.now().isoformat()
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
