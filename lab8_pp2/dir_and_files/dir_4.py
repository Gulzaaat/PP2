f = "xaxa.txt"
cnt = 0
with open(f, "r") as file:
    for i in file:
        cnt += 1
print(cnt)