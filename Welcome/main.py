# FastAPI import
from fastapi import FastAPI

# FastAPI instance 생성.
app = FastAPI()


# Path 오퍼레이션 생성. Path는 도메인명을 제외하고 / 로 시작하는 URL 부분
# 만약 url이 https://example.com/items/foo 라면 path는 /items/foo
# Operation은 GET, POST, PUT/PATCH, DELETE등의 HTTP 메소드임.
@app.get("/", summary="간단한 API", tags=["Simple"])
async def root():
    """
    매우 간단한 API 입니다.
    """

    # dict > json 으로 return (Content-Type: application/json)
    return {"message": "Hello World"}
