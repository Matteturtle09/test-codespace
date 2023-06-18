from deep_translator import GoogleTranslator

f = open("testo.txt", 'r')
fw = open("testo2.txt", 'w')

translated = GoogleTranslator(source='auto', target=input('Lingua Destinazione:')).translate(f.read()) 
print(translated + '')
fw.write(translated)
fw.close()