from textblob import TextBlob


def process(news, args):
    for new in news:
        blob = TextBlob(new['text'])
        for i in range(len(new['text_tokens'])):
            new['text_tokens'][i]['pos'] = blob.tags[i][1]

        blob = TextBlob(new['title'])
        for i in range(len(new['title_tokens'])):
            new['title_tokens'][i]['pos'] = blob.tags[i][1]

    return news
