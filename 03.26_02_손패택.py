'''
2024년3월26일
202195057 손패택
'''
num1 = int (input("첫번째 수 입력 : "))
num2 = int (input("두번째 수 입력 : "))

if num1 == num2 :
    print(f"첫번재 수 {num1}과 두번째 수 {num2}는 같다.")
elif num1 > num2 :
    print(f"첫번째 수 {num1}가 두번째 수 {num2}는 크다.")
else :
    print("num1<num2")