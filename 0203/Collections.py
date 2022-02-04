from collections import Counter

portfolio = [
    ('김백산', 100, 220.1),
    ('태백산', 70, 70.1),
    ('소백산', 10, 490.1),
    ('대백산', 60, 490.1),
    ('전백산', 20, 490.1),
    ('GOOG', 50, 490.1),
]

total_shares = Counter()

# 데이터 순회
for name, shares, price in portfolio:
    total_shares[name] += 1

print(total_shares)