'''
we want to build a translator app that 
takes in text and translate to japanese 

1 read from the file you want to translate 
2 use a translater package to translate into japanese 
3 output the results written to a file 

'''
from translate import Translator


with open('text_to_translate.txt') as file:
    with open('translated_text.txt', mode='w', encoding='utf-8') as output_file:
        translator = Translator(to_lang='ja')
        translation = translator.translate(file.read())
        output_file.write(translation)
