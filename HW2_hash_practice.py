import matplotlib.pyplot as m

D = {}

with open("hw2_data.txt", "r") as txt:
    for x in txt:
        word = x.strip()
        if word:
            if word in D:
                D[word] += 1
            else:
                D[word] = 1

print("不重複英文字的數量：", len(D))
print("\n每個字的出現次數：")
for word, count in D.items():
    print(f"{word}: {count}")

def a(items):
    return items[1]
I = list(D.items())
sorted_items = sorted(I, key=a, reverse=True)
labels = []
values = []
for word, count in sorted_items:
    labels.append(word)
    values.append(count)

m.figure(figsize=(10, 6))
m.bar(labels, values)
m.xlabel("Word")
m.ylabel("frequency")
m.tight_layout()
m.show()
