# from janome.tokenizer import Tokenizer
# t = Tokenizer()
# for token in t.tokenize('すもももももももものうち'):
#     print(token)

from janome.tokenizer import Tokenizer
t = Tokenizer()
malist = t.tokenize("庭には二羽鶏がいます")
for n in malist:
    print(n)