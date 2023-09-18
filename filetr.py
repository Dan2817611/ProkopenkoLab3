from googletrans import Translator
import os
import re

def WordCount(text):
    words = text.split()
    sentences_count = re.split(r'[.!?]', text)
    words_count = len(words)
    sentences_count = len(sentences_count) - 1
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
    config_file = ConfigRead('config.txt')

    if config_file is None:
        print("Конфігураційний файл не знайдено.")
        return

    input_filename = config_file.get('Назва файлу з текстом')
    output_mode = config_file.get('Куди вивести результат')
    max_characters = int(config_file.get('Кількість символів'))
    max_words = int(config_file.get('Кількість слів'))
    max_sentences = int(config_file.get('Кількість речень'))
    target_language = config_file.get('Назва або код мови перекладання')

    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            text = input_file.read()

        text_length = len(text)
        words_count, sentences_count = WordCount(text)

        print("Назва файлу :", input_filename)
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
            output_filename = f"file_translate_text.txt"
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(translated_text)
            print("Ok \n Заданий текст перекладено та збережен у file_translate_text.txt")
        elif output_mode == 'екран':
            print("Мова перекладу:", target_language)
            print(translated_text)
        else:
            print("Невірно вказаний режим виводу")

    except FileNotFoundError:
        print("Файл з текстом не знайдено.")
    except Exception as e:
        print("Помилка:", str(e))

if __name__ == "__main__":
    TextTransl()