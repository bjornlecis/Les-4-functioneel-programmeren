#oefening 3
import queue

q = queue.Queue(4)
q.put({"cat": "kat"})
q.put({"dog": "hond"})
q.put({"horse": "paard"})
q.put({"donkey": "ezel"})

lijst = []

for i in range(q.maxsize):
    for (key,value) in q.get().items():
        print(f'Welke dier is {key} in het Nederlands')
        antwoord_gebruiker = input().lower()

        if antwoord_gebruiker == value:
            lijst.append(f'Vraag {i+1}: juist')
        else:
            lijst.append(f'Vraag {i+1}: fout')
        print('-------------------')

print('')

for item in lijst:
    print(item)
