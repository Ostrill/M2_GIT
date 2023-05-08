from pymystem3 import Mystem

with open('text.txt', 'r') as file:
    text = file.read()

ms = Mystem()
analysis = ms.analyze(text)

for token in analysis:
    word = token.get('analysis')
    if not word:
        continue
    for data in word:
        if isinstance(data, dict):
            gr = data.get('gr')
            if gr:
                print(gr)
                break
