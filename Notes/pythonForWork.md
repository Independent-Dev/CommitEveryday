# Python 정리

### \*변수
***
- **변수명 선언규칙**
  1. 영문자(대, 소문자 구분), 숫자, 언더바(\_)를 사용할 수 있다.
  2. 첫 자리에는 숫자를 사용할 수 없다.
  3. 파이썬 키워드는 변수명으로 사용할 수 없다.

- **변수 선언**: variable = value

- _변수에 저장할 수 있는 것_
  1. 내장 자료형: 숫자형, 문자열, 불리언, 리스트, 튜플, 셋, 딕트
  2. 객체

- **변수의 강제 삭제**
  - del(variable)로 강제 삭제 가능. 

- **언패킹**
  - a, b = [1, 2] -> a = 1, b = 2
  - b, a = a, b -> a = 2, b = 1, 치환을 이렇게 하면 매우 쉬움!!
  - 함수 반환형도 이런 방식으로 받을 수 있음 ex) for x, y in enumerate(list)

### \*조건문
***
- **if**
  - "if:" + 줄바꿈 이후 들여쓰기 
  - **수치 비교**: ==(같다), !=(다르다), <, >, >=, <=("=<"는 에러)
  - **문자열, 리스트 비교**: ==, != 이용.
  - **한 번에 여러 번 비교하기**: "and"나 "or", 그리고 괄호"()"를 이용하여 조건을 연결.  
  - **문자열, 리스트, 셋, 튜플, 딕트(키) 검색**: if target in object(문자열, 리스트, 셋, 튜플, 딕트)
- **else**
  - if가 아닌 경우. 
  - "else:" + 줄바꿈 이후 들여쓰기
- **elif**
  - if가 아닌 다른 조건, 또는 이전에 나오지 않은 다른 조건.
  - "elif:" + 줄바꿈 이후 들여쓰기
##### 파이썬에서는 서로 다른 자료형은 비교할 수 없다. SyntaxError를 일으키지는 않지만 기대한 결과를 얻기 위해서는 형변환 등의 조작이 필요함. 
- **True, False**
  - 파이썬 문법에서 False로 취급하는 것들
     1. None
     2. 0: 0, 0.0, 0.j
     3. 비어 있는 문자열, 리스트, 튜플, 셋

### \*반복문
***
- 반복문이 실행되는 블럭은 들여쓰기 필수.
#### for
- **for x in range(시작수(default=0), 끝수, 단위(default=1))**
  - for x in range(1, 10, 2): 1부터 2씩 추가하면서 10 이전까지(9까지) 숫자를 x라는 변수로 추출하라.
- **for x in list, tuple, set, dict** 등: in 뒤에 오는 데이터를 하나씩 x라는 변수로 추출하라.

#### while
- **선언**: "while 조건문:" + 줄바꿈 이후 들여쓰기 이후 작성, 조건을 탈출할 수 있는 요소를 블록 내에 포함. or 블록 내에 들어가면 무한루프 실행.
- ※파이썬에는 do while이 없는데 그 이유는 1)이건 while로 충분히 대체가 가능하고, do라는 예약어를 추가할 경우 호환성이 심각하게 손상될 수 있기 때문에.

#### break, continue, else
- **break**: 반복문 중단(이하 구문 실행x), 이후 벗어나기
- **continue**: 반복문 블록 내의 이하 구문 건너뛰기. 반복문을 벗어나지는 않는다.
- **else**: 반복문 이후 실행되는 구문. break로 반복문이 끝난 경우에는 실행하지 않는다. 

### \*함수
***
- **함수의 선언**: "def funcname(parameters(NN)):"+ 줄바꿈 이후 들여쓰기 이후 작성(+return dataOrVariable)
  - 선언시에 def funcname(parameter=1)과 같이 default 값을 줄 수 있음.
  - 매개 변수를 정확히 몇 개 받을지 모르는 경우에는 \*를 사용. 
    - ex) def funcname(a, b, \*variables) // funcname(a = 1, b = 2, 3, 4)(여기서 3, 4를 \*variables로 받음. print(\*variables)-> 3, 4. print(variables)->[3, 4])
      - \*는 리스트, 튜플, 셋, 딕트와 같은 자료형에서 데이터만 쏙 뽑아내는 것이라고 생각할 수 있을 것임. 
  - key:value 형식의 미정의 인수를 받고 싶은 경우에는 \*\*를 사용. 
    - ex) def funcname(a, b, \*\*args) // funcname(a = 1, b = 2, c = 3, d = 4)

- **함수의 호출방법**
  - 반환값이 없는 경우: funcname((실행에 요구되는)parameters)
  - 반환값이 있는 경우: variable = funcname((실행에 요구되는)parameters)
  - 두 경우 모두 호출시에는 순서에 유의해서 매개변수를 써야 한다. 
  - "parameter=value(or variable)"와 같은 식으로 특정 값이 정확히 어떤 매개변수인지 써놓으면 순서는 틀려도 상관없다. 
- **이름 붙이는 요령**: do_something과 같이 함수의 기능을 뜻하는 영어 동사와 명사를 조합하여 함수명을 만들면 알기 쉽다. 
- **함수 내의 변수**
  - 함수 내에서 변수를 선언할 경우 그것은 지역변수로서 함수 블록 바깥에서 사용할 수 없다(이 경우 **NameError**).
  - 함수 내에서는 함수 밖의 변수를 참조할 수 있다. 그렇지만 그 변수에 조작을 가할 수는 없다(그런 경우 **UnboundLocalError**)
  - 함수 밖의 변수에 조작을 가하기 위해서는 "global variable"이라고 함수 내에서 선언한다. 단, 한 행을 띄우고 조작을 해야지 global과 함께 값을 할당해서는 안 된다.(**SyntaxError**)

#### lambda식
- **선언**: lambda sequence: sequence 내의 개별 데이터를 사용한 식(반환값)
  - ex)
  - a = [1, 5, 4, 6, 2, 3, 9]
  - a.sort(key = lambda a: a*-1) =>[9, 6, 5, 4, 3, 2, 1]


### \*class
***
- **클래스 정의**: "def className(superClass, 없으면 이 괄호 전체는 안 써도 됨.):"+ 줄바꿈 이후 들여쓰기 이후 작성
- **메소드**
  - 함수는 모듈 내에 위치하는 것. 클래스 내부에 위치하는 함수는 메소드라고 함. 
  - 모든 메소드는 'self'라는 초기 인자를 무조건 받음. 굳이 self일 필요는 없지만 관행적으로 쓰는 것. self에 대입하는 인수는 호출시에 지정할 필요가 없다. 
  - _self를 썼을 때의 이점: 295page_
- **초기화 메소드**
  - **정의**: "def \_\_init\_\_(self, parameters(NN)):"+ 줄바꿈 이후 들여쓰기 이후 작성(self.prop1 = parameter1 등등...)
  - 인스턴스를 생성할 때 실행됨
- **인스턴스 생성**: instance = Class()
- **인스턴스 이용**
  - 입력: 메소드와 속성은 인스턴스 네임스페이스에서 입력(메소드의 경우엔 함수 할당, 속성은 값)과 변경 가능. 
  - 호출 및 참조: object.method(), object.property()(이게 가능한 건 인스턴스 네임스페이스가 클래스 네임스페이스를 참조할 수 있기 때문임)
  - 인스턴스 네임스페이스에 없는(당연히 클래스 네임스페이스에도 없음) 값을 참조하려고 하면 AttribueError 발생
- **캠슐화**
  - 프로퍼티 앞에 \_ 하나 붙이기: 클래스 내부에서만 조작할 수 있음을 알리는 것
  - 프로퍼티 앞에 \_ 두 개 붙이기: 외부에서는 이 프로퍼티에 접근도 할 수 없음을 알리는 것
    - 그렇지만 이것도 object.\_classname\_\_propertyname을 하면 접근, 변경 가능.
  

### \*모듈
***
#### 내장 모듈
- **모듈의 사용**
  - import moduleName: moduleName.class() or moduleName.func()
  - import moduleName as mn: mn.class() or mn.func()
  - from moduleName as class(or func): class.func() or func() 등 
- **모듈 찾기**: http://docs.python.jp/3/

### 내장 자료형
***
#### 숫자형(정수, float)
- **표기법**
  - 16진법: 0x 연속해서 0~9, a~f
  - 8진법: 0o 연속해서 0~7
  - 2진법: 0b 연속해서 0or1 
- **표기법 변환**
  - **16, 8, 2진수로 변환**: hex(num), oct(num), bin(num)
  - **16, 8, 2진수를 10진수로**: int('num', 16(or 8 or 2))
- **비트 연산
  - x | y: x와 y를 2진수로 변환했을 때 각 자리수에 대하여 둘 중 하나라도 1이라면 1을 표기. ex)12(1100)|9(1001) = 13(1101)
  - x & y: 각 자리수에 대하여 둘 중 다 1이라면 1을 표기. ex)12&9 = 8(1000)
  - x ^ y: 각 자리수가 동일하면 0, 다르면 1을 표기. ex)12^9 = 5(0101)

#### 문자열
- **정의 방법**: "~"(큰 따옴표), '~'(작은 따옴표), """~\n"""(삼중 쌍따옴표, 줄바꿈을 포함하는 문자열 정의 가능)
- **문자열의 연결**
  - 1)(변수=)문자열+문자열, 2)변수+문자열 3)+=변수 또는 문자열(복합연산자 이용방식)
  - 다른 데이터 유형을 덧셈(또는 +=) 한 경우에는 TypeError가 발생함. 이걸 막기 위해서는 int(str_var), str(int_var)이 필요함. 
- **문자열 메소드**
  - **str.split(target)**: str을 target을 기준으로 분할, 반환형은 리스트
  - **"target".join(List)**: 주어진 리스트 List에 target을 연결한 문자열을 반환. 
  - **str.replace(target, goal)**: str에서 target에 해당하는 부분을 전부 goal로 변환. 반환형은 문자열.
- **이스케이프 문자**
  - \n: , \r: 줄 바꿈, \t: 수평 탭, \f: 새로운 페이지, \': 단일 인용 , \": 이중 인용 , \\: 백슬래시 , \x61: 16비트 호환 8비트 문자 , \u3042: 16비트 16진수 호환하는 유니코드 문자(16진수 부분에는 "0x" 불필요), \0: null문자
- **raw 문자열**: string = r"\t\n\f"-> "\\t\\n\\f", 이렇게 str 앞에 r을 쓰면 string을 참조했을 때 raw로 나오게끔 백슬레시를 하나 더 추가해준다. 
- **문자열 메소드**
  - S.**find**(target, 시작 인덱스(NN), 종료 인덱스(NN)): S에서 target을 찾기
  - S.**index**(target, Sindex(NN), Findex(default=end, NN)): 숫자 1개를 쓰면 그것은 시작 인덱스. 
  - S.endwith(target, Sindex(NN), Findex(default=end, NN))
  - S.startwith(target, Sindex(NN), Findex(default=end, NN))
  - S.**strip**(target): target을 S의 앞에서부터 target이 안 나오는 곳까지, 그리고 뒤에서부터 target이 안 나오는 곳까지 삭제. 다른 문자열 사이에 있는 것은 삭제 안 함. "aamamaa".strip("a") ->"mam"
  - S.upper(), S.lower(): S의 모든 문자를 대문자와 소문자로 바꾸기. 
  - S.**ljust**(폭(숫자), target(str, NN)): 폭만큼의 공간에서 S를 왼쪽에 밀어놓고 나머지를 target으로 채워넣기. 없으면 공백. 
  - S.rjust(폭(숫자), target(str, NN)): 위와 같은데 S를 오른쪽에 밀어놓기.
  - revered(S)
  - S.encode(way, 오류처리방법(NN, strict, replace, ignore)): S를 way로 인코딩해서 바이트 형식으로 return.
  - Byte.decode(way, 오류처리방법(NN, strict, replace, ignore)): Byte를 way로 해석해서 문자열 형식으로 return.

-  **.format()**
  -  이 메소드의 반환형은 전부 str.
  - "{}str{}".format("v", "a"): 포멧에 들어있는 매개변수를 {}안에 순서에 맞게 삽입->"vstra"
  - "{1}str{0}".format("v", "a"): {} 안에 숫자를 입력하므로써 삽입 위치 지정 가능 -> "astrv"
  - "{a1}str{v1}".format(v1="v", a1="a"): 매개변수를 key=value 형식으로 집어넣으면 {key}로 value를 추출 할 수 있다.->"vstra"
  - "{0[a1]}str{0[v1]}".format(dictionary): 매개변수로 딕트형 데이터를 전달하면 {0[key]}로 value를 추출 할 수 있다.->"vstra"(dictionary = {v1: "v", a1: "a"})
  - 그외: 이것 외에도 밀림과 표기형식을 지정할 수 있음. 
- **f문자열(fstring)**
  - 포메팅을 쉽게 하는 방법, 마찬가지로 리턴값은 str.
  - S = "AAA"인 상태에서 f"str{S}"을 하면 리턴값은 "strAAA"이 된다. 

#### 리스트(list)
- **특징**: 순서 있음, 인덱스 접근 가능, 변경 가능, 중복 가능
- **리스트 정의**
  - variable = [1, 2, 3, "문자", ["LI", "ST"], ("TU", "PLE"), {"S", "ET"}]
- **리스트 요소 추출**: LIST[INDEX]
- **리스트 슬라이싱**: LIST[시작요소 인덱스: 끝요소 인덱스+1(불포함):단위(NN)]
  - li = [1, 2, 3, 4, 5]
  - li[:] -> [1, 2, 3, 4, 5]
  - li[1:1] = []
  - li[1:3] = [2, 3]
  - li[1:0] = []
  - li[2:4] = ['Three', 'four', 'five'] -> li = [1, 2, 'Three', 'four', 'five', 5]
- **리스트 연결**: (변수=)리스트+리스트, 2)변수+리스트 3)+=변수 또는 리스트(복합연산자 이용방식)
- **2차원 배열**: [["li", "st1"], ["li", "st2"]]
- **리스트 메소드**
  - max(list): list의 최대값
  - min(list): list의 최솟값
  - len(list): list의 길이, 요소 수
  - list.sort(reverse(NN)): list의 요소를 오름차순으로 정렬, 반환값은 없음, list 자체를 정렬하는 것, reverse=True이면 내림차순 정렬. 
    - sorted_list = sorted(list, reverse(NN)): sorted()는 정렬된 리스트를 반환함. 
  - list.sort(key=func(괄호 안 붙임! 매개변수는 당연히 list이므로), reverse(NN)): func에 의해 조정된 list를 오름차순으로. reverse=True이면 내림차순으로. 
    - ex: 만약 minus_def()가 리스트의 모든 항목에 -1을 곱하는 함수라 치면 list.sort(key=minus_def)를 하면 내림차순 값이 나오게 됨.
    - sorted_list = sorted(list, key=func reverse(NN)): sorted()는 정렬된 리스트를 반환함. 
  - del list[index]: 리스트의 인덱스 항목을 삭제.
  - del list[:]: 슬라이싱 된 항목을 삭제. 이 경우에는 전부. 
  - list.pop(index(default = -1)): 해당 인덱스를 반환하고 리스트에서는 삭제.
  - list.remove(item): 리스트에서 가장 앞에 있는 해당 item을 삭제, 반환값x.
  - list.append(item): 리스트의 맨 뒤에 해당 item을 추가.
  - list.extends(sequence): sequence를 하나하나 분리해서 각 요소를 list에 append()
  - list.insert(index, item), 해당 index에 item을 삽입. index가 크기보다 더 크면 맨 뒤, 마이너스로 변환했을 때 리스트에 있는 인덱스보다 더 작으면 맨 앞에 삽입.  

- **리스트 컴프리핸션**
  - 함수형 프로그래밍을 이용하여 리스트를 생산하는 기법.
  - List = [func(variable)(or variable) for variable in data (if 조건문)]
    - ex) 0~9까지의 리스트 생성: [x for x in range(10)]
  - zip() 함수를 활용
    - [[x, y] for x, y in zip(seq1, seq2)]

  1. 셋 컴프리핸션: {func(variable)(or variable) for variable in data (if 조건문)}
  2. 딕트 컴프리핸션: {var1:var2 for var1, var2 in data (if 조건문)}
  - **튜플 컴프리핸션 같은 건 없다. 중괄호를 소괄호로 바꾸면 그와 같은 데이터를 지연평가로 생산하는 iterator가 된다.** 


#### 튜플(tuple)
- **특징**: 순서 있음, 인덱스 접근 가능, 변경 불가, 중복 가능
- **튜플 정의**: Tuple = (value1, value2)
- **튜플의 추출, 슬라이싱, 그리고 연결**: 리스트와 동일
- **튜플 메소드**
  - max(tuple): tuple의 최대값
  - min(tuple): tuple의 최솟값
  - len(tuple): tuple의 길이, 요소 수

#### 딕트(dict)
- **특징**: key:value 형식, 인덱스 접근 불가, 변경 가능, 키 중복 불가(키에 변경가능 자료형 사용 불가)
- **딕트 정의**
  - Dict = {}
  - Dict = {key1:value1, key2:value2}
  - Dict = dict({key1:value1, key2:value2})
  - Dict = dict([[key1, value1], [key2, value2]])
  - Dict = dict(key1=value1, key2=value2)
- **키의 검색**: if x in Dict와 같이 in 키워드를 이용하여.
- **딕트 요소 추출**: Dict[key]
  - **존재하지 않는 key를 이용해 dict를 참조하려고 하면 keyError가 발생함. 그러므로 이것은 보다 세심하게 처리할 필요가 있음. 이 경우에는 3가지 방법**
    1. if문을 이용하여 키가 없는 경우에 처리할 프로세스를 정해놓을 수 있음.
    2. get(key, default(NN-not necessary))를 이용하여 key가 없는 경우에는 default값을 반환하도록 할 수 있음. default가 없으면 None을 반환함. 
    3. setdefault(key, default(NN))를 이용하여 key값에 아무것도 없다면 default를 key의 value로 세팅하고 그것을 반환함. get이 key가 없는 경우에 에러를 대신할 값을 반환한다면(그래서 일종의 있는 것처럼 보이게 한다면), setdefault는 요청을 받은 시점에 값을 실제로 세팅한다는 점에서 차이가 있음. 
- **Dict[key] = value**: key가 없으면 Dict의 key에 value값을 입력, 있으면 key의 값을 value로 변경.
- **딕트 메소드**
  - del Dict[key]: Dict에서 해당 key를 가진 요소를 삭제. 
  - Dict1.update(Dict2): Dict1에 Dict2의 내용을 추가. 키가 없으면 키를 추가하고, 키가 있으면 키를 갱신.
  - 그외: D.keys(), D.values(), D.items() 


#### 셋(set)
- **특징**: 인덱스 접근 불가, 변경 가능, 중복 불가(변경가능 자료형 사용 불가, 정의 시 중복 때에는 자동으로 중복이 제거됨)
- **셋 정의**: Set = {value1, value2, value3}
- **셋 연산 및 메소드**
- 셋은 집합연산을 지원한다. 
- 합집합: Set1|Set2, Set1.union(Set2)
- 차집합: Set1-Set2, Set1.difference(Set2)
- 교집합: Set1&Set2, Set1.intersection(Set2)
- 대상차집합(합집합-교집합): Set1^Set2, Set1.symmetric_difference(S2)
- Set1.add(item): item을 셋에 추가.
- Set1.remove(item): item을 셋에서 제거.

_개념과 이론보다는 사용방법을 중심으로 정리하자. 모든 것을 하기 보다는 핵심적인 것만_

### 파일 입출력
***
- **open()**: +를 붙이면 읽고 쓰기 둘 다 가능, 모드를 사용하면 파일을 열 당시에 read/write() 시작 위치를 조정 가능. 
  1. w+: 파일이 없다면 새로 만들고, 있다면 내용을 싹 다 지우고 처음.
  2. r+: 내용 처음.
  3. a+: 내용 마지막. 
- **seek(num, whence(default=0, NN))**: num을 통해서 읽고 쓰는 위치 조정 가능.
  - for문에서 파일 객체에 in을 건 다음 변수(i)를 print(i, end = " ")로 출력하면, 한 줄씩 파일의 내용을 출력할 수 있음. 
- **f.close()**: file 객체 f 닫기.  
- **readline(읽어들일 바이트(NN))**: 바이트를 지정하면 1줄에서 읽어들일만큼만. 그렇지 않으면 파일을 1줄씩 읽어들이는 메소드,  
- **readlines(읽어들일 바이트(NN))**:  
- **writelines()**: 


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
  