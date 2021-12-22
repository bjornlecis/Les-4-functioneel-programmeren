import queue

getallen = queue.Queue(5)
getallen.put(5)
getallen.put(9)
getallen.put(3)
getallen.put(4)
getallen.put(7)
lijst_juiste_getallen = []
aantal_juiste_antwoorden = 0

for i in range(getallen.maxsize):
    getal = getallen.get()
    print("hoeveel is het dubbel van: ",getal)
    antwoord_gebruiker = int(input())
    if antwoord_gebruiker == getal*2:
        lijst_juiste_getallen.append(getal)
        aantal_juiste_antwoorden = aantal_juiste_antwoorden+1

print(lijst_juiste_getallen)
print("je hebt ",aantal_juiste_antwoorden," juist beantwoord")
