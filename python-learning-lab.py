names = ["Alice", "Bob", "Charlie"]
scores = [85,92,78]

zipped = zip(names,scores)

for name, score in zipped:
    print(f"{name}: {score}")