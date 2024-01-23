# Python 이미지 사용
FROM python:3.11

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 설치
COPY pyproject.toml poetry.lock* /app/
RUN pip install poetry
RUN poetry install

# 소스 코드 복사
COPY . /app

# FastAPI 실행
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
