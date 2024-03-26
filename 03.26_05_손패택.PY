'''
202195057 손패택
2024년3월26일
'''
score = int(input("점수 입력 :"))
if 0 <= score <=100:
    if score >= 90 :
       print("A")
    elif   score >= 80 :
        print("B")
    elif   score >= 70 :
        print("C")
    elif   score >= 60 :
        print("D")
    else:
        print("F")
else :
    print("잘뭇된 점수입니다.")