from translate import Translator
import os

try:
    with open(os.path.join(os.getcwd(),'Input Output (i.o)', 'test.txt'), mode='r') as my_file:
        text = (my_file.read())
        translator = Translator(to_lang='ja')
        translation = translator.translate(text)
        with open(os.path.join(os.getcwd(),'Input Output (i.o)', 'translated_jap.txt'), mode='w') as my_file2:
            my_file2.write(translation)

except FileNotFoundError as e:
    print('check your file path silly!')



