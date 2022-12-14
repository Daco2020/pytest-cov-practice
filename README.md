
# pytest-cov 란?

`pytest-cov`는 `--cov` 옵션 추가하여 테스트 대상의 coverage를 확인할 수 있습니다. 사용자는 coverage 수치를 통해 테스트의 적용범위를 파악할 수 있습니다.

<br><br><br>


# 실습 방법 


### 레포지토리 복사
```
git clone https://github.com/Daco2020/pytest-cov-practice.git
```

<br>

### 라이브러리 설치
```
pip install pytest-cov
```

<br>

### 실행 명령어
```
pytest --cov
```
또는
```
pytest --cov=[src] [test]
```

- `[src]` 위치에 대상을 명시하면 대상에 대해서만 Cover를 확인할 수 있습니다. 

- `[test]` 위치에 경로를 입력하면 해당 경로의 테스트만 수행합니다.


<br><br><br>

# 명령어 예시

`pytest-cov` 는 명령어 조합에 따라 다음과 같은 경우의 수를 가집니다. 소스코드를 클론 받아 따라해보세요.

<br>

### 1. `pytest --cov` 는 모든 테스트를 실행하고, 대상 전체의 Cover를 보여줍니다.
```sh
# 실행

pytest --cov
```
```sh
# 결과

collected 4 items

tests/test_main.py .. 
tests/test_serve.py ..  

---------- coverage: platform darwin, python 3.10.6-final-0 ----------
Name                  Stmts   Miss  Cover
-----------------------------------------
main/file.py              6      0   100%
serve/file.py             6      0   100%
tests/__init__.py         0      0   100%
tests/test_main.py        5      0   100%
tests/test_serve.py       5      0   100%
-----------------------------------------
TOTAL                    22      0   100%
```

<br><br>


### 2. `pytest --cov=main` 는 모든 테스트를 실행하고, main에 대해서만 Cover를 보여줍니다.
```sh
# 실행

pytest --cov=main
```
```sh
# 결과

collected 4 items

tests/test_main.py ..
tests/test_serve.py ..

---------- coverage: platform darwin, python 3.10.6-final-0 ----------
Name           Stmts   Miss  Cover
----------------------------------
main/file.py       6      0   100%
----------------------------------
TOTAL              6      0   100%

```

<br><br>


### 3. `pytest --cov=main tests/test_main.py` 는 test_main.py의 테스트만 실행하고, main에 대해서만 Cover를 보여줍니다.
```sh
# 실행

pytest --cov=main tests/test_main.py
```
```sh
# 결과

collected 2 items                          

tests/test_main.py ..

---------- coverage: platform darwin, python 3.10.6-final-0 ----------
Name           Stmts   Miss  Cover
----------------------------------
main/file.py       6      0   100%
----------------------------------
TOTAL              6      0   100%


```


<br><br>

## 참고

pytest-cov에 대해 더 자세한 내용을 알고 싶다면 [공식문서](https://pytest-cov.readthedocs.io/en/latest/)를 확인해주세요.

<br><br>
---
위의 예시와 공식문서를 참고하여 직접 명령어를 입력해보세요.<br>
당신의 프로젝트에 적용해보고 coverage를 확인해보세요.

