import PackPr.module1

texttransl = input("Введіть текст для перекладу: ")
target_language = input("Введіть код мови (мова на яку необхідно перекласти) : ")
print()
print("Переклад : ", PackPr.module1.TransLate(texttransl, "auto", target_language))

print(PackPr.module1.LangDetect(texttransl, "all"))

print(f"Назва мови на яку переклали {target_language}: ", PackPr.module1.CodeLang(target_language))

print("\nСписок мов у консолі:")
print(PackPr.module1.LanguageList("screen", texttransl))

print(PackPr.module1.LanguageList("file", texttransl))
