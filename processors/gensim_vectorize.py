from gensim.models import FastText


def process(news, args):
    try:
        model = FastText.load(args)
    except:
        model = FastText.load("models/araneum_none_fasttextcbow_300_5_2018/araneum_none_fasttextcbow_300_5_2018.model")

    for new in news:
        for i, word in enumerate(new['text_tokens']):
            new['text_tokens'][i]['vec'] = model.wv[word]

        for i, word in enumerate(new['title_tokens']):
            new['title_tokens'][i]['vec'] = model.wv[word]
    return news
