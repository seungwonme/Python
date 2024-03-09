# python

## `venv`와 `pip`를 이용한 가상환경 설정

프로젝트의 종속성을 격리시켜 충돌방지

```bash
python -m venv venv
```

## 가상환경 활성화

```bash
source venv/activate
```

## 필요한 패키지 설치

```bash
pip install your-package

# 만약 requirements.txt가 있다면
pip install -r requirements.txt
```

## `requirements.txt` 생성

```bash
pip freeze > requirements.txt
```

## 가상환경 비활성화

```bash
deactivate
```
