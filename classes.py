class BasicWord:
    """Класс содержащий в себе исходное слово и набор допустимых подслов"""
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return f"Из слова '{self.word}' можно составить слова: {', '.join(self.subwords)}"


    def is_correct(self, user_word):
        return user_word in self.subwords


    def number_subwords(self):
        return len(self.subwords)

class Player:
    """Класс содержащий в себе имя игрока и набор написаных им слов"""
    def __init__(self, name):
        self.name = name
        self.words = []


    def __repr__(self):
        return f"{self.name} использовал слова: {', '.join(self.words)}"


    def number_word(self):
        return len(self.words)


    def append_word(self, user_word):
        self.words.append(user_word)


    def is_repeat(self, user_word):
        return user_word in self.words