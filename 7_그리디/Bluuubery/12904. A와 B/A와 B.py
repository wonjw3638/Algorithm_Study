# 220904 12904 A와 B

# 정답코드

# S: 시작 문자열, T: 목표 문자열
S = input()
T = input()

# cnt: 문자열을 바꿀 횟수
cnt = len(T) - len(S)
# idx: 지금까지 문자열을 바꾼 횟수
idx = 0

# T에서 S로 역순으로 진행해가며 S가 나올 수 있는지 검증한다.
while True:
    idx += 1
    # T의 마지막 문자가 A면 직전 시행은 무조건 'A 추가'이므로 역으로 A를 빼준다.
    if T[-1] == 'A':
        T = T[0:-1]
    # T의 마지막 문자가 A면 직전 시행은 무조건 '문자열 뒤집고 B를 추가'이므로 역순으로 B를 빼주고 문자열을 뒤집는다..
    else:
        T = T[0:-1]
        T = T[::-1]
    
    # 문자열을 횟수만큼 다 바꿨으면 종료
    if idx == cnt:
        break
    

# 바꿀 수 있으면 1, 없으면 0 출력
if S == T:
    print(1)
else: 
    print(0)
