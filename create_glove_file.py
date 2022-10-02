import torchtext

if __name__ == "__main__":
    glove = torchtext.vocab.GloVe(name="6B",  # trained on Wikipedia 2014 corpus
                                  dim=100)  # embedding size = 50