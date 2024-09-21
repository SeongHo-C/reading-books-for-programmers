n, k = map(int, input().split())

count = 0

"""
# 내 풀이 방법
while n != 1:
  if n % k: n -= 1
  else: n /= k

  count += 1

# 단순하게 푸는 답안 예시
while n >= k:
  while n % k != 0:
    n -= 1
    count += 1

  n //= k
  count += 1

while n > 1:
  n -= 1
  count += 1
    
문제에서는 N의 범위가 10만 이하이므로, 이처럼 일일이 1씩 빼도 문제를 해결할 수 있다. 
하지만 N이 100억 이상의 큰 수가 되는 경우를 가정했을 때에도 빠르게 동작하려면, N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 소스코드를 작성할 수 있다.
"""

while True:
  # (N == K로 나누어떨어지는 수)가 될 때까지 1씩 빼기
  target = (n // k) * k
  count += n - target
  n = target
  # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k: break
  # K로 나누기
  count += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
count += (n - 1)
print(count)