#oefening 2 met dank aan TIM :D
import queue

q = queue.LifoQueue(4)
q.put({'g1': 5, 'g2': 10})
q.put({'g1': 15, 'g2': 20})
q.put({'g1': 4, 'g2': 4})
q.put({'g1': 7, 'g2': 8})

lijst = []

for i in range(q.maxsize):
    som = 0
    for (key,value) in q.get().items():
        print(f'Getal {key} is {value}')
        som += value
    input_som = int(input('Wat is de som: '))
    if som == input_som:
        lijst.append(f'Vraag {i+1}: juist')
    else:
        lijst.append(f'Vraag {i+1}: fout')
    print('-------------------')

print('')

for item in lijst:
    print(item)
