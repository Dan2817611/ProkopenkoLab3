import PackPr.module2

texttransl = input("Введіть текст для перекладу: ")
target_language = input("Введіть код мови (мова на яку необхідно перекласти) : ")

print("Переклад : ",PackPr.module2.TransLate(texttransl, "auto", target_language))

print(PackPr.module2.LangDetect(texttransl, "all"))

print(f"\nНазва мови на яку переклали {target_language}: " ,PackPr.module2.CodeLang(target_language))

print("\nСписок мов у консолі:")
print(PackPr.module2.LanguageList("screen", texttransl))

print(PackPr.module2.LanguageList("file", texttransl))
