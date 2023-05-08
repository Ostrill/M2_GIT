from pymystem3 import Mystem
import re


def extract_and_check_part(gr):
    required_parts = {'A', 'ADV', 'V'}
    part_of_speech = re.split(r'\W+', gr)[0]
    if part_of_speech in required_parts:
        return part_of_speech
    else:
        return None


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
