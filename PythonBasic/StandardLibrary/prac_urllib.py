from urllib import request
import os

if __name__ =="__main__":
    url = input('url을 입력하세요: ')
    temp = url.split("/")[-1]
    filename = "./"+temp.split(".")[1]+".html"
    request.urlretrieve(url, filename)
    #입력한 url을 "www.바로 뒤 문자열+html"형식의 파일로 저장.
    print("파일 생성 확인1")
    print(os.listdir(os.getcwd()))

    #다른 버젼
    req = request.Request(url)
    #reqeust 객체 req를 반환. "<class 'urllib.request.Request'>"
    object_response = request.urlopen(req)
    #urlopen은 request 객체를 이용해 HTTPResponse 객체를 생성
    # 이 객체는 read()를 포함하여 여러 메소드를 가지고 있음.
    sourcebyte = request.urlopen(req).read()
    #이때 리턴값은 byte형식.
    decoded = sourcebyte.decode()
    #때문에 이것을 html파일로 만들기 위해서는 디코딩이 필요.
    f = open("./"+temp.split(".")[1]+"1.html", "w")
    f.write(decoded)
    f.close()
    print("파일 생성 확인2")
    print(os.listdir(os.getcwd()))
    print("HTTPResponse 객체 메소드들: ")
    print("geturl(): ", object_response.geturl())
    print("info(): ", object_response.info())
    #그외 readline(), readlines() 등을 사용할 수 있고 이것의 사용 방법은 file객체 이용과 동일. 다만 반환값이 byte형식.

    print("--------데이터 POST---------")
    from urllib import parse
    print("about parse.urlencode: 딕셔너리 또는 시퀀스로부터 URL 인코드된 쿼리를 만듦. urlopen() 등을 이용하여 웹 서비스에 데이터를 송신하고"
          "데이터를 송신하고 싶을 때 편리함.")
    postdic = {'name': 'someone', 'email': 'foo@bar.com'}
    print("변환 전: ", postdic)
    postdata = parse.urlencode(postdic)
    print("변환 후: ", postdata)
    #urlopen()은 postdata도 매개변수로 받을 수 있음.
    #그외 이것과 비슷한 함수로는 quote(), quote_plus(), unquote(), unquote_plus() 등이 있음.


