from googletrans import Translator, LANGUAGES
import os



def TransLate(text: str, scr: str, dest: str) -> str:
    translator = Translator()
    translation = translator.translate(text, src=scr, dest=dest)
    return translation.text


def LangDetect(text: str, set: str) -> str:
    translator = Translator()
    detection = translator.detect(text)

    if set == "lang":
        return detection.lang
    elif set == "confidence":
        return str(detection.confidence)
    else:
        return f"Language: {detection.lang}, Confidence: {detection.confidence}"


def CodeLang(lang: str) -> str:
    translator = Translator()
    try:
        lang_code = translator.translate(lang, src='en').src
        return lang_code
    except:
        return "Error: Language code not found."


def LanguageList(out: str, text: str = None) -> str:
    translator = Translator()
    output = ""

    if text is not None:
        output += f"N Language ISO-639 code Text\n"
        output += "-" * 56 + "\n"
        for idx, (code, lang) in enumerate(LANGUAGES.items(), start=1):
            translation = translator.translate(text, dest=code).text
            output += f"{idx:<2} {lang:<12} {code:<15} {translation}\n"
    else:
        output += f"N Language ISO-639 code\n"
        output += "-" * 28 + "\n"
        for idx, (code, lang) in enumerate(LANGUAGES.items(), start=1):
            output += f"{idx:<2} {lang:<12} {code}\n"

    if out == "file":
        with open("language_list.txt", "w", encoding='utf-8') as file:
            file.write(output)
        return f"Ok: Table written to {os.getcwd()}\\language_list.txt"
    else:
        print(output)
        return "Ok"


