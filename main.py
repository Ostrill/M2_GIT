from pymystem3 import Mystem
import re


def extract_and_check_part(gr, required_parts):
    part_of_speech = re.split(r'\W+', gr)[0]
    if part_of_speech in required_parts:
        return part_of_speech
    else:
        return None


def open_text_file():
    with open('text.txt', 'r') as file:
        text = file.read()
    return text


def analyze(text):
    ms = Mystem()
    return ms.analyze(text)


def count_parts(analysis):
    counts = {'A': 0, 'ADV': 0, 'V': 0}
    for token in analysis:
        word = token.get('analysis')
        if not word:
            continue
        for data in word:
            if isinstance(data, dict):
                gr = data.get('gr')
                if gr:
                    checked_part = extract_and_check_part(gr, counts.keys())
                    if checked_part:
                        counts[checked_part] += 1
                    break
    return counts


def print_result(result):
    label_to_russian = {'A': 'Прилагательных',
                        'ADV': 'Наречий',
                        'V': 'Глаголов'}
    for part, count in result.items():
        print(f'{label_to_russian.get(part)}: {count}')


if __name__ == '__main__':
    text_from_file = open_text_file()
    text_analysis = analyze(text_from_file)
    part_counts = count_parts(text_analysis)
    print_result(part_counts)
