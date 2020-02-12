from io import StringIO

f = StringIO()
f.write("a"*100)
f.seek(0)
print(f.read())
f.close()
f1 = StringIO("""- 일종의 파일을 흉내내는 객체. 
문자열 데이터를 파일로 저장한 다음 여러가지 처리를 하게 되는데, 
그 파일이 다시 쓰이지 않을 때 유용함. 
처리 과정에서 동적으로 파일의 확장자나 내용이 바뀌는 데이터(파일)에서도 유용할 거라고 생각함. 
""")
print(f1.getvalue())
f1.close()
