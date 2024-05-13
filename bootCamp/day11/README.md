## 리스트 컴프리헨션(list comprehension)
리스트 컴프리헨션은 Python에서 리스트를 생성하기 위한 간결하고 효율적인 방법입니다. 
구체적으로, 이 구문은 모든 카드 모양(suits)과 숫자(ranks)의 조합을 순회하며, 각 조합으로 카드를 생성하여 리스트에 추가합니다. 
여기서 각 카드는 모양과 숫자를 결합한 문자열로 표현됩니다(f"{suit} {rank}").

```py
# cards 리스트를 생성합니다.
cards = [f"{suit} {rank}" for suit in suits for rank in ranks]
```

1. 외부 루프: 먼저, for suit in suits 구문으로 모든 카드 모양(suits)을 순회합니다. 이는 스페이드(♠️), 하트(♥️), 다이아몬드(♦️), 클로버(♣️) 각각에 대해 내부 루프를 실행하게 합니다.
2. 내부 루프: 그 다음, for rank in ranks 구문으로 모든 카드 숫자(ranks)를 순회합니다. 이는 A부터 K까지 각 숫자에 대해 실행됩니다.
3. 리스트에 추가: 외부 루프와 내부 루프의 현재 요소(suit와 rank)를 결합하여 새로운 문자열을 생성합니다. 이 문자열은 형식화된 문자열 리터럴(f-string, f"{suit} {rank}")을 사용하여 만들어지며, 카드 모양과 숫자를 공백으로 구분한 형태로 표현됩니다.
4. 리스트 생성: 위에서 생성된 문자열들은 cards 리스트에 순차적으로 추가됩니다. 최종적으로, 이 리스트 컴프리헨션은 모든 가능한 카드의 조합을 포함하는 리스트를 생성합니다.

결과적으로, 이 구문은 각 모양에 대해 모든 숫자의 카드를 생성하고, 이를 하나의 리스트로 결합합니다. 이렇게 하여, 52장의 전체 카드 덱을 나타내는 cards 리스트가 만들어집니다.

## 리스트에 요소 추가하기
### 1. `append()` 메서드 사용하기
`append(element)` 메서드는 리스트의 끝에 새로운 요소를 추가합니다. 예를 들어, `cards` 리스트에 "♠️ A" 카드를 추가하고 싶다면 다음과 같이 할 수 있습니다:

```python
cards.append("♠️ A")
```

### 2. `insert()` 메서드 사용하기
`insert(index, element)` 메서드를 사용하면 지정된 인덱스에 요소를 삽입할 수 있습니다. 예를 들어, 인덱스 0의 위치에 "♠️ A" 카드를 삽입하려면 다음과 같이 할 수 있습니다:

```python
cards.insert(0, "♠️ A")
```

### 3. `extend()` 메서드 사용하기
만약 여러 개의 요소를 리스트에 추가하고 싶다면, `extend(iterable)` 메서드를 사용할 수 있습니다. 이 메서드는 인자로 받은 반복 가능한 객체(예: 다른 리스트)의 모든 요소를 리스트의 끝에 추가합니다. 예를 들어, 두 개의 카드를 `cards` 리스트에 추가하고 싶다면 다음과 같이 할 수 있습니다:

```python
cards.extend(["♠️ A", "♦️ 10"])
```

### 4. 슬라이싱을 이용한 삽입
슬라이싱과 할당을 이용하여 리스트의 특정 위치에 여러 요소를 삽입할 수도 있습니다. 예를 들어, 인덱스 1의 위치에 여러 카드를 삽입하고 싶다면:

```python
cards[1:1] = ["♠️ A", "♦️ 10"]
```

## 리스트에 특정 요소 제거하기

### remove() 메서드
리스트에서 첫 번째로 나타나는 지정된 값을 삭제한다.
```py
cards.remove("♠️ A")
```

### pop() 메서드
지정된 인덱스에 있는 요소를 삭제하고, 삭제된 요소를 반환한다.
```py
removed_card = cards.pop(0)
```

### del 키워드
특정 인덱스의 요소를 직접 삭제하고 싶다면, 슬라이싱과 할당을 사용하여 해당 요소를 삭제할 수 있다.
```py
# 인덱스 0에 있는 요소를 삭제한다.
del cards[0]
# 인덱스 0부터 3까지의 요소를 삭제한다.
del cards[0:4]
```

### 값으로 인덱스 찾아 삭제하기
index() 메서드를 사용하여 특정 값의 인덱스를 찾은 후, pop() 메서드를 사용하여 해당 인덱스의 요소를 삭제할 수 있다.
```py
card_to_remove = "♠️ A"
index_to_remove = cards.index(card_to_remove)
removed_card = cards.pop(index_to_remove)
```

## 전역 변수(global variable) 사용하기
전역 변수는 프로그램 전체에서 사용할 수 있는 변수로, 함수 내부에서도 접근할 수 있습니다.
전역 변수를 사용하려면 변수를 함수 내부에서 global 키워드로 선언해야 합니다.
```py
# 전역 변수를 선언한다.
global_var = 10

def my_function():
    # 함수 내부에서 전역 변수를 사용한다.
    global global_var
    print(global_var)
