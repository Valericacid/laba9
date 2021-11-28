def sort_sentence(sentence):
    sentence = sentence.lower()
    sentence = sentence.split(' ')
    sentence = sorted(sentence, key=len)
    sentence = " ".join(sentence)
    sentence = sentence.capitalize()

    return sentence


if __name__ == "__main__":
    sentence = "Keep calm and carry on"
    print(sort_sentence(sentence))
