# Make fastapi tool
    실행 법 : 
    1. python main.py -path {원하는 경로의 폴더 이름까지}
    2. 만들어진 폴더에서 'python3 -m venv venv' 실행 (가상환경 make) 
    (+) pip install mysql -- mysql 이용자 
    (+) pip install fastapi 
    (+) pip install uvicorn
    3. 만들어진 폴더에서 uvicorn main:app --reload --port 9000 ( 혹은 원하는 포트 지정) 
    4. 127.0.0.1:9000/docs 문서 확인



# 구조 

    --folder-- 
    |----init.py
    |----main.py 
    |----db.py
    |----model.py[db.py](..%2Ftest2%2Fdb.py)
    |----routes
    |----|____[db.py](..%2Ftest2%2Fdb.py)___init.py 
    |----|_______route*.py


# 기타

    db.py / model.py 는 init.py 와 내용이 동일 
    py 파일로 내용이 없는 파일임.
    **venv\Scripts\activate 



