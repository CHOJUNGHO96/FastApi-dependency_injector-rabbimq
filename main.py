from fastapi import FastAPI
from containers import RabbitMQContainer

# FastAPI 앱 인스턴스 생성
app = FastAPI()

# 의존성 컨테이너 구성 및 실행
RabbitMQContainer()

