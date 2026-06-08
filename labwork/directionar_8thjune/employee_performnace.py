performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# 1. Employees scoring above 80
print("Employees Scoring Above 80:")
for emp in performance:
    if performance[emp] > 80:
        print(emp)

# 2. Count employees needing improvement
count = 0
for emp in performance:
    if performance[emp] < 60:
        count += 1

print("Employees Needing Improvement:", count)

# 3. Find top performer
top = max(performance, key=performance.get)
print("Top Performer:", top, performance[top])

# 4. Calculate average score
total = sum(performance.values())
average = total / len(performance)

print("Average Score:", average)

# 5. Create separate lists
excellent = []
good = []
average_list = []
poor = []

for emp in performance:
    score = performance[emp]

    if score >= 90:
        excellent.append(emp)
    elif score >= 75:
        good.append(emp)
    elif score >= 60:
        average_list.append(emp)
    else:
        poor.append(emp)

print("Excellent:", excellent)
print("Good:", good)
print("Average:", average_list)
print("Poor:", poor)
