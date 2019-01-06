import random


def process(news, args):
    for new in news:
        for token in new['text_tokens']:
            token['ner'] = ["NOUN", "VERB", "ADJ"][random.randrange(0, 3)]
    return news