# Python 정리4

## 표준 라이브러리

### 데이터 구조
***
#### collections.OrderedDict
- **from collections import OrderedDict**
- 딕셔너리는 추가 순서와 관계없이 요소가 표시되지만 OrderedDict는 추가하는 순서에 맞춰서 내부에 저장됨.
- 3.6 버전부터는 딕셔너리의 저장방식이 OrderedDict와 동일하게 됨. _그럼 3.6 이후부터는 OrderedDict를 왜 써야하나...

#### collections.defaultDict
- **from collections import defaultdict**
- **객체 생성**: object = defaultdict(내장자료형), 여기엔 list외에도 tuple, set 등이 들어갈 수 있음. 
- 객체 생성 시에 인수로 전달한 자료형에 맞게 key와 value를 세팅하면 됨.
  - ex)
  - from collections import defaultdict
  - dd = defaultdict(list)
  - dd["a"].append(1)

#### bisect
- 이 모듈은 모든 리스트의 요소를 항상 정렬된 상태를 유지하고 있게끔 도와주는 함수들을 제공한다. 
- **import bisect**
- **bisect.insort_left(a, x)**: 정렬된 리스트 a에 요소 x를 정렬되어 있는 상태로 삽입함. x와 같은 요소가 있는 경우에는 같은 요소의 앞에 요소를 추가함. **insort_right**는 뒤에.
- **bisect.bisect_left(a, x)**: 정렬된 상태에 x를 추가한다고 할 때, a에서 x의 위치. 같은 요소가 있다면 그 요소들 가운데 가장 앞의 인덱스를 반환함. **bisect_right**는 반대. 

### 일시(날짜와 시간)
***
- **time**: 날짜와 시간을 취급하기 위한 기초적인 모듈. 에폭이라고 불리는 특별한 초 수를 기본으로 하여 처리함. 
- **datetime**: 이 모듈을 사용하면, time 모듈에서는 1970년 이전과 2036년 이후의 미래에 대한 시간을 사용할 수 있음. 특별한 이유가 없는 이상 이 모듈을 사용한다고 함.  
#### datetime




