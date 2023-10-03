import random

meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
my_words = ["herkesin önünde düşmek", "yatağına kaçırmak",]

my_word = ["dans eden süngerbob", "komik kediler"]

if word in meme_dict.keys():
    print(random.choice(my_words))
else:
    print(random.choice(my_word))
