pytest --cov 는 전체폴더와 전체 테스트에 대한 cov
pytest --cov=app 은 app폴더에 대한 cov(특정 폴더만 확인할 수 있음, 테스트는 전체 돌아감)
pytest --cov=app tests/ 는 tests폴더안에 있는 테스트를 확인함(테스트를 분류해서 돌릴 수 있음)
pytest tests/ 는 해당폴더에 있는 테스트 코드만 실행
즉, 앞에는 cov 확인 폴더 뒤에는 테스트 돌릴 경로 라고 이해하면 됨

