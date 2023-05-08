from pymystem3 import Mystem
import re


def extract_and_check_part(gr):
    part_of_speech = re.split(r'\W+', gr)[0]
    if part_of_speech in counts.keys():
        return part_of_speech
    else:
        return None


with open('text.txt', 'r') as file:
    text = file.read()

ms = Mystem()
analysis = ms.analyze(text)

counts = {'A': 0, 'ADV': 0, 'V': 0}

for token in analysis:
    word = token.get('analysis')
    if not word:
        continue
    for data in word:
        if isinstance(data, dict):
            gr = data.get('gr')
            if gr:
                checked_part = extract_and_check_part(gr)
                if checked_part:
                    counts[checked_part] += 1
                break

label_to_russian = {'A': 'Прилагательных', 'ADV': 'Наречий', 'V': 'Глаголов'}
for part, count in counts.items():
    print(f'{label_to_russian[part]}: {count}')