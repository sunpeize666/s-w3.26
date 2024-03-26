'''
컴퓨터학부202195057 손패택
 
'''
score = int(input("점수 입력 : "))
num = int(input("점수를 입력하세요:"))
if 100>=num >=90:
    print("{}은 A학점.".format(num))
elif 90>num >=80:
    print("{}은 B학점.".format(num))
elif 80>num >=70:
    print("{}은 C학점.".format(num))
elif 70>num >=60:
    print("{}은 D학점.".format(num))
elif 0<=num <60:
    print("{}은 F학점.".format(num))
else :
    print("없는 점수")
