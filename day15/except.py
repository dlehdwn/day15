try: #try는 에러가 날 것 같은 구문을 적는 곳
   n = int(input("숫자 입력:"))
   result = 10 / n
   print(f"결과는 {result}")
except Exception:
    print("에러!!")
else:
    print("에러없다~~~")
finally:
    print("상관 없으니 보여줘라")

