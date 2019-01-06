import sys, pickle, xlrd, importlib


def parse_args(argv):
    file_name = None
    processor_classes = []
    for arg in argv[1:]:
        if arg.startswith("fname="):
            file_name = arg.split("fname=")[1]
        if arg.startswith("--"):
            processor_args = None
            if "=" in arg:
                processor_class, processor_args = arg[2:].split("=")
            else:
                processor_class = arg[2:]
            processor_classes.append((processor_class, processor_args))
    return file_name, processor_classes


def read_xlsx(file_name):
    news = []
    xl_workbook = xlrd.open_workbook(file_name)
    sheet_names = xl_workbook.sheet_names()
    xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
    for rownum in range(0, xl_sheet.nrows):
        news.append({
            "title": xl_sheet.cell_value(rownum, 3),
            "text": xl_sheet.cell_value(rownum, 4),
            "text_sentences": xl_sheet.cell_value(rownum, 4).split("."), #TODO smarter sentence separation?
            "text_tokens": [
                                {
                                    "id": 0, #TODO ID (used for dependency parsing)
                                    "token": token,
                                    "normal_form": "",
                                    "pos": "",
                                    "ner": "",
                                    "sentiment": "",
                                    "dependency": [] #[(ID, TYPE)]
                                    #...
                                } for token in  xl_sheet.cell_value(rownum, 4).split(" ") #TODO smarter tokenization
                            ],
            "n_grams": [], #TODO ngrams
            "authenticity": 0, #TODO
            "objectivity": 0,
            "social_impact": 0,
            "potential_resonance": 0,
            "sentiment": 0,
            "manipulative": 0,
            "politisized": 0,
            "kazakhstani": 0,
            "topic1": "",
            "topic2": "",
            "topic3": "",
        })
    return news


def main(argv):
    file_name, processor_classes = parse_args(argv)
    news = read_xlsx(file_name)
    for processor in processor_classes:
        i = importlib.import_module(processor[0])
        news = i.process(news, processor[1])

    pickle.dump(news, open(file_name.split('.')[0] + "_processed(" + str(processor_classes) + ").pickled", "wb"))


if __name__ == "__main__":
    main(sys.argv)
