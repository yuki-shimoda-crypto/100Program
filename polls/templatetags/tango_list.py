from django import template
import collections
from janome.tokenizer import Tokenizer
from googletrans import Translator
register = template.Library()

@register.simple_tag

def  tango_n(s):
    translator = Translator()
    t = Tokenizer()

    v = [token.surface for token in t.tokenize(s)
         if token.part_of_speech.startswith('名詞')]
    c = collections.Counter(v)
    print(c.most_common())
    order = [i[0] for i in c.most_common()]
    print(order)
    ls = []
    
    for english in order:
        m = translator.translate(english)
        ls.append(str(m.text))
     
    return(ls)
        
    dict_from_list = dict(zip(order, ls))
    print(dict_from_list)
    
    