def total(initial=5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count
print total(10, 1, 2, 3, vegetables=50, fruits=100)

# 앞에 별 기호가 달린 매개 변수, 예를 들어 *param 과 같이 매개 변수를 지정해 주면
# 함수에 넘겨진 모든 위치 기반 인수들이 'param' 이라는 이름의 튜플로 묶여서 넘어온다.
# 또 이와 비슷하게 앞에 별 두 개가 달린 매개 변수, 예를 들어 **param 과 같이 매개 변수를 지정해 주면
# 함수에 넘겨진 모든 키워드 인수들이 'param' 이라는 이름의 사전으로 묶여서 넘어옵니다.
# 핵심은 튜플과 사전 이라는 개념 

