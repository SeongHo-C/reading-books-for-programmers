n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

result = 0

"""
# 내 풀이 방법
for i in range(m):
  if i % k == 0 and i != 0: result += second
  else: result += first

# 단순하게 푸는 답안 예시
while True:
  for i in range(k):
    if m == 0: break
    result += first
    m -= 1
  
  if m == 0: break
  result += second
  m -= 1

이 문제는 M이 10,000 이하이므로 위 방식으로도 문제를 해결할 수 있지만, M의 크기가 100억 이상처럼 커진다면 시간 초과 판정을 받을 것이다.
아래 방식처럼 간단한 수학적 아이디어(반복되는 수열)를 이용해 더 효율적으로 문제를 해결할 수 있다.
"""  

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result += count * first
result += (m - count) * second

print(result)



