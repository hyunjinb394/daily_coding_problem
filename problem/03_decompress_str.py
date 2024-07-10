# 0. 문제 정보
# 문자열 압축 해제
# 시간 제한: 1초
# 엘리스 토끼는 문자열을 직접 압축 해제하려고 합니다.

# 압축되지 않은 문자열 S가 주어졌을 때, 이 문자열 중 어떤 부분 문자열은 K(Q)와 같이 압축할 수 있습니다. 
# 이것은 Q라는 문자열이 K 번 반복된다는 뜻입니다. K는 한 자릿수의 정수이고, Q는 0자리 이상의 문자열입니다.

# 예를 들면, 53(8)은 다음과 같이 압축을 해제할 수 있습니다.

# 53(8) = 5 + 3(8) = 5 + 888 = 5888

# 압축된 문자열이 주어졌을 때, 이 문자열을 다시 압축을 푸는 프로그램을 작성하세요.

# 지시사항
# 입력
# 첫째 줄에 압축된 문자열 S를 입력합니다.
# S의 길이는 최대 50입니다.
# 문자열은 (, ), 숫자로만 구성되어 있습니다.


# 1. 문제 이해
# () 앞의 숫자 만큼 문자열의 길이가 추가되고
# ()가 닫힐때 stack으로 마지막에 넣어준 값들 부터 계산해 나가야함
# 즉, 가장 안쪽의 () 부터 풀어나가야한다는 뜻
# 시간초과가 자꾸 떠서 문자열을 생성하지 않고 문자열 길이만 계산하는 로직으로 수정

# 2. 문제 풀이
import sys
input = sys.stdin.readline

def decompress_length(s):
    stack = []
    # 압축 해제된 문자열 길이
    current_length = 0
    # 문자열의 인덱스
    i = 0
    
    while i < len(s):
        # 현재 인덱스의 문자가 숫자라면
        if s[i].isdigit():
            # 정수로 변환
            num = int(s[i])
            # 다음 문자가 ( 일때
            if i + 1 < len(s) and s[i + 1] == '(':
                stack.append(current_length)
                # ( 앞의 추가되는 길이의 숫자
                stack.append(num)
                current_length = 0
                # ( 건너 뛰기 위한 인덱스 +1
                i += 1 
            # ()로 감싸진 문자가 아닌 숫자면 길이 +1
            else:
                current_length += 1
        elif s[i] == '(':
            pass 
        elif s[i] == ')':
            # num으로 스택에 추가한 repeat_count 꺼내기
            repeat_count = stack.pop()
            previous_length = stack.pop()
            current_length = previous_length + repeat_count * current_length
        else:
            current_length += 1
        # 다음 문자로 이동
        i += 1
    
    return current_length

S = input().strip()
result = decompress_length(S)

print(result)


# 3. 다른 풀이

string = input()

stack = []
# depth 리스트로 문자열을 저장
depth_result = [0] * 50
depth = 0

for ch in string:
    if ch != ")":
        if ch == "(":
            depth += 1
            depth_result[depth] = 0
        stack += [ch]
    # 문자가 ) 이면
    else:
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == "(":
                num = depth_result[depth]
                for j in stack[i + 1 :]:
                    num += 1
                depth -= 1
                depth_result[depth] += num * int(stack[i - 1])
                del stack[i - 1 :]

                break

print(depth_result[0] + len(stack))

# 이 정도의 풀이를 해내려면 depth_result가 필요하다는 판단과
# 문제 흐름을 압축해서 그림으로 그릴 수 있어야한다.
