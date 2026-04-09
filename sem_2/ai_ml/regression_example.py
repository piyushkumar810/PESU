# Data (list of dictionaries)
data = [
    {"height": 151, "weight": 63},
    {"height": 174, "weight": 81},
    {"height": 138, "weight": 56},
    {"height": 186, "weight": 91},
    {"height": 128, "weight": 47},
    {"height": 136, "weight": 57},
    {"height": 179, "weight": 76},
    {"height": 163, "weight": 72},
    {"height": 152, "weight": 62},
    {"height": 131, "weight": 48}
]

# Initialize sums
n = len(data)
sum_x = sum_y = sum_xy = sum_x2 = sum_y2 = 0

# Loop through data
for d in data:
    x = d["height"]
    y = d["weight"]
    
    sum_x += x
    sum_y += y
    sum_xy += x * y
    sum_x2 += x ** 2
    sum_y2 += y ** 2

# Apply formula
numerator = n * sum_xy - (sum_x * sum_y)
denominator = ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2)) ** 0.5

r = numerator / denominator

# Output
print("Correlation coefficient (r):", round(r, 4))