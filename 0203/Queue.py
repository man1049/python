import queue

li = ["김백산", "태백산", "소백산"]

# 큐를 생성해서 데이터를 추가
# back = queue.Queue()
# back = queue.PriorityQueue()  # 우선순위 큐
back = queue.LifoQueue()  # 스택
for x in li:
    back.put(x)

print(back.get(0))
print(back.get(0))
print(back.get(0))
