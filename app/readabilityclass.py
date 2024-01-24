import re


class ReadabilityAnalyzer:
    def __init__(self, text):
        self.text = text

    def count_letters(self):
        letters_amount = len(re.sub(r"[^a-zA-Z]", "", self.text))
        return letters_amount

    def count_words(self):
        words_amount = self.text.count(" ") + 1
        return words_amount

    def count_sentences(self):
        sentences_amount = len(re.findall(r"[.!?]", self.text))
        return sentences_amount

    def count_readability(self):
        letters = self.count_letters()
        words = self.count_words()
        sentences = self.count_sentences()
        L = (letters / words) * 100
        S = (sentences / words) * 100
        readability = round(0.0588 * L - 0.296 * S - 15.8)
        return readability

    def show_analysis(self):
        index = self.count_readability()
        if index < 1:
            print("Before Grade 1")
        elif index > 16:
            print("Grade 16+")
        else:
            print(f"Grade {index}")


if __name__ == "__main__":
    text = input("Type text for analysis: ")
    analyzer = ReadabilityAnalyzer(text)
    analyzer.show_analysis()

