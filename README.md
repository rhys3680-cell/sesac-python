# 새싹 파이썬 기초 과정

새싹(SeSAC) 파이썬 기초 과정에서 학습한 내용과 미션 문제 풀이를 모아둔 저장소입니다.

## 개발 환경

- **Python**: 3.13
- **패키지 관리**: [uv](https://github.com/astral-sh/uv)
- **개발 도구**: ipython

## 시작하기

### 의존성 설치

```powershell
uv sync
```

### 실행 방법

```powershell
# 메인 스크립트 실행
uv run python main.py

# 개별 미션 문제 실행
uv run python mission_problem_2.py
```

## 프로젝트 구조

```
sesac-python/
├── main.py                    # 진입점
├── mission_problem_*.py       # 미션 문제 풀이
├── class_test.py              # 클래스 실습
├── test*.py                   # 연습 코드
├── pyproject.toml             # 프로젝트 설정
└── .python-version            # Python 버전 명시
```

## 미션 문제 목록

| 파일 | 주제 |
| --- | --- |
| [mission_problem_2.py](mission_problem_2.py) | 조건문 — 수하물 요금 계산 / 홀짝 판별 등 |
| [mission_problem_3.py](mission_problem_3.py) | 입력 처리와 조건식 — 홀짝 판별 |
| [mission_problem_4.py](mission_problem_4.py) | 두 정수 중 큰 값 출력 |
| [mission_problem_5.py](mission_problem_5.py) | 1~10 합계 (반복문 vs 공식) |
| [mission_problem_6.py](mission_problem_6.py) | 재귀 — 팩토리얼 |
| [mission_problem_7.py](mission_problem_7.py) | 반복문 — 구구단 |
| [mission_problem_8.py](mission_problem_8.py) | 반복문 — 3의 배수 합 |
| [mission_problem_9.py](mission_problem_9.py) | 숫자 맞추기 게임 (random) |
| [mission_problem_10.py](mission_problem_10.py) | 리스트 활용 — 강아지 이름 관리 |
| [mission_problem_11.py](mission_problem_11.py) | 친구 리스트 관리 메뉴 |
| [mission_problem_12.py](mission_problem_12.py) | 리스트와 함수 — 성적 평균 계산 |
| [mission_problem_13.py](mission_problem_13.py) | 클래스 — Circle (원 클래스) |
| [mission_problem_14.py](mission_problem_14.py) | 클래스 — BankAccount (은행 계좌) |
| [mission_problem_15.py](mission_problem_15.py) | 클래스 — Cat (캡슐화) |
| [mission_problem_16.py](mission_problem_16.py) | 클래스 — Box (직육면체) |

## 기타 실습 파일

- [class_test.py](class_test.py) — 클래스 연산자 오버로딩 (`__eq__`, `__str__`) 실습
- [test.py](test.py), [test2.py](test2.py), [test3.py](test3.py) — 수업 중 작성한 연습 코드