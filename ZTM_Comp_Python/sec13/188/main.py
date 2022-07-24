from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open("./test.txt", mode="r") as f1:
        text = f1.read()
        translated = translator.translate(text)
        with open("./test-ja.txt", mode="w") as f2:
            f2.write(translated)
except FileNotFoundError as err:
    print("ERROR: file not found error")
except IOError as err:
    print("ERROR: IO error")
