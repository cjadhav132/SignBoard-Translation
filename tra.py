from googletrans import Translator
from googletrans import LANGUAGES
trans = Translator()
#var=""
class var:
    def __init__(self, vab,lan):
        self.vab = vab
        self.lan = lan
    def trann(vab ,lan):
        t = trans.translate(vab,dest= lan)
        #print(f'destination: {LANGUAGES[t.dest]}')
        #print
        text = (t.text).split()
        print(text)
        s=' '.join(text)
        print(s)
        return (s)


'''
for lang in LANGUAGES:
    #    az+=1
    print(f'{lang} - {LANGUAGES[lang]}')

var2=var.trann('আপনি কেমন আছেন','fr')
print(var2)
p=(list(LANGUAGES.values()))
print(p)
q=(list(LANGUAGES.keys()))
print(q)

print((type(p)))
az=0
print(az)
#'''