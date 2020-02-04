# 알기 쉬운 파이썬 4판2

### Chap5 파이썬과 함수형 프로그래밍
***
#### 1.함수형 프로그래밍이란
- 정의: 쉽게 말하면 객체지향형 프로그래밍과는 달리 모든 것을 함수로 표현하려는 방법. 객체에 그에 적합한 조작을 가하여 결과를 얻어내는 것이 아니라, (어떤 객체든 간에 특정한) 입력에 대하여 원하는 출력을 뽑아내는 함수를 작성하는 것. 
  - "객체 지향적...252page"
- 이점: 함수형 스타일을 이용하면...
- lambda식: lambda parameters: func() // 여기서 parameters에는 list, tuple, set, dict 전부 다 들어갈 수 있음. 그 자료형을 처리할 수 있게 func()을 써주기만 하면 됨. 

**★헷갈리기 쉬운 것!!: list는 reverse(), str은 reversed(str), 여기서 reversed(str)은 완성된 문자열을 반환하는 게 아니라 뒤집힌 출력을 만들어 낼 수 있는 reverse object를 반환함.**

**★리스트를 문자열로 만드는 2방법**
  1.str(list) ->'[list]'
  2."".join(list) ->'list'
  
_map()과 filter()_

#### 2.Comprehension
- list comprehension 예시 // set도 비슷함. 
  - str_speeds = "38 42 30 40 a1 39"
  - speeds = [int(s) for s in  str_speeds.split() if s.isdigit()]
  - print(speeds)-> [38, 42, 30, 40, 39]

- dictionary comprehension: {key:value for 반복 변수 in sequence if(NN)}

#### 3-1.지연평가(lazy evaluation): Iterator
##### 참조: https://wikidocs.net/22800, http://pythonstudy.xyz/python/article/23-Iterator%EC%99%80-Generator
- 지연평가: 평가를 늦추고 필요할 때 값을 계산해주는 것
- iterator: 지연평가 객체, generator: 특정한 방식(yield 키워드를 사용하는)으로 생성한 iterator
- iterator 사용의 이점: 특정 주소에 있는 데이터를 컴퓨터가 RAM에 올려놓으면 메모리에 부담이 큼. 그래서 iterator는 lazy하게 요청받으면 해당 데이터만을 RAM에 올려놓음. so 메모리 사용량 측면에서 많은 이득이 있고, 이 이득은 데이터의 크기에 비례함.
- iterator 객체를 만드는 방법:
  1. for문의 시퀀스로 내장 자료구조를 이용할 때 파이썬이 자동으로 변환
  2. 내장함수인 iter_object = iter(seq)를 사용. 다음 요소를 얻으려면 next(iter_object)를 이용.
  3. 생성자 표현식 이용: iter_object = (x\*\*2 for x in range(1, 10)), 사용 방법은 위와 동일

#### 3-2.지연평가: Generator
- iterator와의 차이: _(이건 확실하지 않음, 나중에 여쭤보기!) iterator가 아직 완벽하게 evaluate되지는 않았지만 (리스트, 셋 등으로) 형태가 규정되기는 한 sequence를 다룬다면, generator가 다루는 것은 함수에 의해 나온 개별 출력 자체. yield 키워드를 통해 함수에 대한 출력값의 조작 권한을 다른 함수 또는 메소드 등에 위임.
- Generator example:
  - def factorial(x=1, y=1):
    - while True:
      - x+=1
      - y*=x
      - yield y
  - i = factorial()
  - for x in range(10):
    - print(next(i))
***
_소수를 반환하는 generator는 직접 만들어보기_

#### 4.고차함수(higher-order-functions)와 데코레이터
- 고차함수: 함수를 매개변수로 받는 함수, 또는 반환값으로 함수를 돌려주는 함수.
- 데코레이터: 고차함수를 이용할 때 고차함수의 매개변수 자리에 특정 함수(func())를 대입하는 것이 아니라 함수 위에 "@고차함수명"을 표시해주고, func()을 실행하므로써 고차함수를 이용하는 것과 동일한 결과를 가져올 수 있다. 
_268~273 이해하는 데 어려움은 없음. 다만 익숙해져야 할 뿐. 계속 써보자!! 집에 가서 실습해보기._

### Chap6 클래스와 객체지향 개발
***

#### 클래스
- ★클래스를 만들 때 아무런 처리도 하지 않을 때에는 **pass**라고 적기. 
- **★클래스를 만든 이후에 속성(property)를 몇 개라도 자유롭게 정의하고 정의된 것을 사용할 수 있지만, 정의되지 않은 속성을 사용하려고 하면 문제가 생김**
  - i = MyClass()
  - i.value = 5 #MyClass()가 value를 가지고 있지 않더라도 이건 가능. 
  - print(i.value)#이것도 가능! 그렇지만 윗 줄과 순서를 바꾸는 것은 허용x.
- 클래스 내에서 규정된 메소드들은 무조건 제1인수로 self를 받아야함
- 캡슐화: java에서 public, protected, private과 같은 식으로 명시하는 것보다는 미약. 그렇지만 존재하긴 함.
  - 속성명이나 메소드 앞에 _ 한 개: 속성 변경 불가
  - _ 두 개(\_\_): 속성 접근 불가




