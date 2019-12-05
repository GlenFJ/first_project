import translate

translator=Translator(to_lang='es')
try:
    with open('C:/Users/GLENFRAN/test.txt', mode='r') as my_file:
        text=my_file.read()
        translation=translator.translate(text)
        with open('./test-ja.txt',mode='w') as my_file2:
            my_file2.write(translation)
        print(translation)
except FileNotFoundError as e:
    print('enter the right file path')
