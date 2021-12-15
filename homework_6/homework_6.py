user = "Tim"
data1 = ["John", "Maria", "Antom", "Tim"]
data2 = ["John", "Maria", "Antom", "tIm"]
data = ["John", "Maria", "antom", "tim"]

if user not in data1:
    data1.append(user)

if user not in data2:
    data2.append(user)
elif user.lower() in data2:
    data.append(user)

found = False
for item in data:
    if item.lower() == user.lower():
        found = True
        break
if not found:
        data.append(user)
