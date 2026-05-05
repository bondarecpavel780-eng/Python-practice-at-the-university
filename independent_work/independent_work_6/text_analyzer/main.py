"""Точка входу — обробка командного рядка та запуск аналізу."""

import argparse
import os

from parser import tokenize, split_sentences
from analysis import (
    count_words, count_words_len, count_unique_words,
    count_titlecase_words, count_digits, alternation_count
)
from output import print_table, export_to_json, export_to_csv


class TextAnalyzer:
    def __init__(self, text: str):
        self.text = text
        self.tokens = tokenize(text)
        self.sentences = split_sentences(text)

    def get_main_stats(self, target_word_len: int = 3) -> dict:
        return {
            "Кількість слів": count_words(self.tokens),
            f"Слів довжини {target_word_len}": count_words_len(self.tokens, target_word_len),
            "Унікальних слів": count_unique_words(self.tokens),
            "Починаються з великої": count_titlecase_words(self.tokens),
            "Чисел": count_digits(self.tokens),
            "Кількість знакозмін": alternation_count(self.tokens)
        }

    def get_sentence_analytics(self) -> dict:
        analytics = {}
        for i, sentence in enumerate(self.sentences, 1):
            sent_tokens = tokenize(sentence)
            analytics[f"Речення {i}"] = {
                "Кількість слів": count_words(sent_tokens),
                "Кількість чисел": count_digits(sent_tokens)
            }
        return analytics


def main():
    parser = argparse.ArgumentParser(description="Текстовий аналізатор")
    parser.add_argument("text", nargs="?", default="", help="Текст для аналізу")
    parser.add_argument("-f", "--file", help="Шлях до текстового файлу")
    parser.add_argument("-o", "--output", help="Зберегти результат (.json або .csv)")

    args = parser.parse_args()

    if args.file:
        if not os.path.exists(args.file):
            print(f"Помилка: Файл {args.file} не знайдено.")
            return
        with open(args.file, 'r', encoding='utf-8') as f:
            text = f.read()
    elif args.text:
        text = args.text
    else:
        print("Передайте текст як аргумент або використайте прапорець -f.")
        return

    analyzer = TextAnalyzer(text)
    stats = analyzer.get_main_stats()
    sentence_stats = analyzer.get_sentence_analytics()

    print_table(stats)

    print("\n--- Аналітика по реченнях ---")
    for key, data in sentence_stats.items():
        print(f"{key}: {data['Кількість слів']} слів, {data['Кількість чисел']} чисел.")

    if args.output:
        if args.output.endswith('.json'):
            export_to_json({"stats": stats, "sentences": sentence_stats}, args.output)
        elif args.output.endswith('.csv'):
            export_to_csv(stats, args.output)


if __name__ == "__main__":
    main()