import numpy as np
import pandas as pd
from emoji_translate.emoji_translate import Translator
import time
import spacy
import regex
import torchtext
import torch

def emojify(word):
    ignore_words = {'the', 'in', 'and', 'but', 'yet'}
    custom_emojis = {'a': '🅰️'}
    emo = Translator(exact_match_only=False, randomize=True)

    if word in ignore_words:
        return None
    else:
        emojified_word = emo.emojify(word)
        if emojified_word != word:
            return emojified_word
        elif word.lower() in custom_emojis.keys():
            return custom_emojis[word]
        else:
            most_similar = None
            glove = torchtext.vocab.GloVe(name="6B",  # trained on Wikipedia 2014 corpus
                                          dim=100)  # embedding size = 50

            vec = glove[word]
            dists = torch.norm(glove.vectors - vec, dim=1)
            lst = sorted(enumerate(dists.numpy()), key=lambda x: x[1])  # sort by distance
            for idx, difference in lst[1:10 + 1]:  # take the top n
                poss_emoji = emo.emojify(glove.itos[idx])
                if glove.itos[idx] != poss_emoji:
                    most_similar = poss_emoji
            return most_similar


def main():
    # # test = 'i love chicken. What the fuck is guacamole. avocado and avocados'
    # test = 'love love love love love'
    # output = emojify(test)
    # # print(output.split()[0])
    # # print(output.split()[0].encode('utf-8'))
    # print(output)
    test = 'handle'
    print(emojify(test))


if __name__ == "__main__":
    main()
