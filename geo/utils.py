import math

# 피타고라스 정리: 빗변 c의 길이 계산 (c = sqrt(a**2 + b**2))
def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

# 원의 넓이 계산 (area = pi * r * 2)
def circle(r):
    area = math.pi * r * 2
    return area
