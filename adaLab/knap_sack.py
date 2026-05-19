n, W = map(int, input().split())

items = []

for _ in range(n):
    value, weight = map(int, input().split())
    items.append((value, weight))

total_value = 0.0

for value, weight in items:

    # if whole item can fit
    if W >= weight:
        total_value += value
        W -= weight

    else:
        # take fraction
        fraction = W / weight
        total_value += value * fraction
        break

print(f"{total_value:.2f}")