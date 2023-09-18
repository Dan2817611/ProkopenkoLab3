import os
import re
from googletrans import Translator

def WordCount(text):
    words = text.split()
    sentences = re.split(r'[.!?]', text)
    words_count = len(words)
    sentences_count = len(sentences) - 1
    return words_count, sentences_count


def ConfigRead(config_filename):
    config = {}
    try:
        with open(config_filename, 'r', encoding='utf-8') as config_file:
            for line in config_file:
                key, value = line.strip().split(':')
                config[key.strip()] = value.strip()
        return config
    except FileNotFoundError:
        return None

def TextTransl():
    config = ConfigRead('config.txt')

    if config is None:
        print("Помилка: конфігураційний файл не знайдено.")
        return

    input_filename = config.get('Назва файлу з текстом')
    output_mode = config.get('Куди вивести результат')
    max_characters = int(config.get('Кількість символів'))
    max_words = int(config.get('Кількість слів'))
    max_sentences = int(config.get('Кількість речень'))
    target_language = config.get('Назва або код мови, на яку необхідно перекласти текст')

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            text = input_file.read()

        text_length = len(text)
        words_count, sentences_count = WordCount(text)

        print("Назва файлу:", input_filename)
        print("Розмір файлу:", os.path.getsize(input_filename), "байт")
        print("Кількість символів:", text_length)
        print("Кількість слів:", words_count)
        print("Кількість речень:", sentences_count)
        print("Мова тексту:", target_language)

        if text_length > max_characters or words_count > max_words or sentences_count > max_sentences:
            print("Досягнуто максимальну кількість символів, слів або речень.")
            return

        translator = Translator()
        translated_text = translator.translate(text, dest=target_language).text

        if output_mode == 'file_text.txt':
            output_filename = f"translate_{input_filename}_{target_language}.txt"
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(translated_text)
            print("Ok \n Заданий текст перекладено")
        elif output_mode == 'екран':
            print("Мова перекладу:", target_language)
            print(translated_text)
        else:
            print("Помилка: невірно вказаний режим виводу")

    except FileNotFoundError:
        print("Помилка: файл з текстом не знайдено.")
    except Exception as e:
        print("Помилка:", str(e))

if __name__ == "__main__":
    TextTransl()