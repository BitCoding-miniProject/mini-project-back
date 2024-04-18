# uvicorn.run 함수는 이 애플리케이션을 지정된 호스트와 포트에서 실행합니다.
# reload=True 옵션은 개발 중 코드 변경이 있을 때마다 서버를 자동으로 재시작하게 해줍니다,
# 이는 개발 과정을 효율적으로 만들어줍니다.

import uvicorn  # uvicorn 모듈을 임포트합니다.

# 메인 모듈로 실행될 때 아래 코드가 실행됩니다.
if __name__ == "__main__":
    uvicorn.run("main:app",  # "main:app"은 main.py 파일의 app 인스턴스를 가리킵니다.
                host='localhost',  # 서버는 localhost에서 실행됩니다.
                port=8000,  # 서버는 8000 포트를 사용합니다.
                reload=True)  # 코드에 변경이 있을 때 서버를 자동으로 재시작합니다.
