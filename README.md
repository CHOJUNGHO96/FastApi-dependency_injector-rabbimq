# FastApi-dependency_injector-rabbimq

이 프로젝트는 FastAPI, Dependency Injector, rabbitmq를 사용하여 구현하는데 참고할수있는 프로젝트입니다.

## 설치 및 실행 방법
1. Docker 및 Docker Compose가 설치되어 있는지 확인하세요.
2. 이 리포지토리를 클론하세요: `git clone [GitHub 리포지토리 URL]`
3. 다음 명령으로 서비스를 실행하세요: `docker-compose up --build`
4. docker ps 명령어로 fastapi 컨테이너ID를 찾아서 docker exec -it 컨테이너ID /bin/bash 로접속
5. consumer를 백그라운드로 실행 하기위해 poetry run python /app/background/receiver.py 명령어 실행
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-rabbitmq/assets/61762674/5f55afc5-730f-4f62-ae74-2885689cb1e0)
6. 브라우저에서 `localhost:8000/docs`으로 애플리케이션에 접속하세요.
   

## 실행TEST
1. message 입력후 api 요청
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-rabbitmq/assets/61762674/ded5bd94-54ec-448e-8b21-7fefdf585286)

2. queues에 해당 message가 쌓임
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-rabbitmq/assets/61762674/f0db325f-afb5-4b44-a86b-adbf8ce68ed6)

3. 백그라운드로 consumer 실행시 queues에 먼저쌓인 메세지 구독
<br/>![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-rabbitmq/assets/61762674/b9a11ca9-5036-4db4-b389-4b82474a8f2d)
![image](https://github.com/CHOJUNGHO96/FastApi-dependency_injector-rabbitmq/assets/61762674/98729b23-f9cb-41af-a2a7-58c34e60a9c3)


