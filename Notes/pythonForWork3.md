# Python 정리3

## 목차: 이터레이터, 고차함수와 데코레이터, 예외 처리

### 이터레이터
***
#### 3-1.지연평가(lazy evaluation): Iterator
##### 참조: https://wikidocs.net/22800, http://pythonstudy.xyz/python/article/23-Iterator%EC%99%80-Generator
- 지연평가(lazy evaluation): 평가를 늦추고 필요할 때 값을 계산해주는 것
- iterator: 지연평가 객체, generator: 특정한 방식(yield 키워드를 사용하는)으로 생성한 iterator
- iterator 사용의 이점: 특정 주소에 있는 데이터를 컴퓨터가 RAM에 올려놓으면 메모리에 부담이 큼. 그래서 iterator는 lazy하게 요청받으면 해당 데이터만을 RAM에 올려놓음. so 메모리 사용량 측면에서 많은 이득이 있고, 이 이득은 데이터의 크기에 비례함.
- iterator 객체를 만드는 방법:
  1. for문의 시퀀스로 내장 자료구조를 이용할 때 파이썬이 자동으로 변환
  2. 내장함수인 iter_object = iter(seq)를 사용. 다음 요소를 얻으려면 next(iter_object)를 이용.
  3. 생성자 표현식(generator expression) 이용: iter_object = (x\*\*2 for x in range(1, 10)), 사용 방법은 위와 동일

#### 3-2.지연평가: Generator
- generator expression은 내부적으로 yield 키워드를 사용하여 지연평가를 수행함.
- generator expression 외에 함수를 만들 때 yield를 씀으로써 generator를 만들어서 사용할 수 있음. 
  - ex):
    - def factorial(x=1, y=1):
      - while True:
        - x+=1
        - y*=x
        - yield y
    - i = factorial()
    - for x in range(10):
      - print(next(i))
***
- **enumerate(sequence)**
  - sequence에 인덱스를 붙여서 (index, value) 형태(튜플)로 반환하는 함수. 

### 고차함수와 데코레이터
***
- **고차함수란**? 함수를 전달해서 처리하는 함수, 또는 반환값으로 함수를 돌려주는 함수
  - ex1)
  - def execute(func, arg):
    - return func(arg)
  - print(execute(int, "100") ->100을 반환. 
  - ex2)
  - def logger(func):
    - def inner(\*args):
      - print("인수", args)
      - return func(args)
    - return inner()
  - newfunc = logger(sum)
  - print(newfunc(1, 2)) -> inner()의 결과가 출력됨.

- **데코레이터란**? 고차함수를 이용할 때 함수를 고차함수에 대입하지 않고 이용하는 방식.
  - ex)
  - @logger
  - def accumerate(\*args):
    - return sum(args) 
  - print(accumerate(1, 2)) ->위와 동일한 결과가 출력됨. 

### 예외 처리
***
-에러(error)는 stackoverflow나 메모리 부족처럼 발생하면 복구할 수 없는 심각한 오류이고, 예외는 발생하더라도 수습할 수 있는 비교적 
#### 처리 방법
- **예외처리 기본 구문**: "try:" 줄바꿈 후 들여쓰기+"예외를 포착하는 블록"+ "except:" 줄바꿈 후 들여쓰기+"예외가 발생하였을 때 처리하는 블록"
  - "except 예외클래스명:"과 같이 포착할 예외, 또는 예상되는 예외를 규정할 수도 있음. 
  - except 예외 클래스명 as 변수명: print(변수명)을 해서 예외에 대한 보다 상세한 정보 얻을 수 있음.
  - else 블록: 예외가 발생하지 않은 경우의 처리를 기술하고 싶을 때 이용. except가 break라 쳤을 때 for문의 else와 동일한 역할.
  - finally: 예외가 발생해도 발생하지 않아도 실행할 블록
  - 이상의 try, except, else, finally는 서로 어떤 블록의 내부에 들어가지 않고 독립적인 블록임. 
  - ex)
  - try:
  - except:
  - else:
  - finally:

- **with** command as variable: command에서 얻어진 객체가 variable에 들어감. command에서 에러가 나면 블록으로 진입x, with에서는 예외처리를 하는 것보다 블록 처리로 간결하게 기술할 수 있음. 
  - ex)
  - with open(filename) as f:
    - for line in f:
      - print(line)
***
- **raise**: 자신이 만든 클래스 등에서 오류가 발생한 것을 외부에 전달하고 싶을 수 있는데 그럴 때 사용함. ex)raise ValueError("Some Message")와 같은 식으로 사용함. raise구문이 실행되면 except블록으로 넘어가서 데이터의 처리가 이루어짐. 
- **traceback 모듈**: except블록에서 traceback 모듈을 사용하면 정보를 가져와 표시하거나 문자열로 가지고 올 수 있음._나중에 raise와 더불어 써보기_

#### 자주 발생하는 예외
- **NameError**: 정의되지 않은 변수 등을 참조할 때 발생하는 에러.
- **AttributeError**: 객체에 정의되지 않은 속성을 참조하려 하거나 정의되지 않은 메소드를 이용하려 할 때 발생하는 에러. 
- **KeyError**: 존재하지 않는 키로 딕셔너리의 요소를 참조하려 할 때 또는 존재하지 않는 셋의 요소에 접근하려고 할 때(Set.remove(item) 등) 발생하는 에러.
- 그외: SyntaxError, IndexError, ImportError, TypeError, ZeroDivisionError