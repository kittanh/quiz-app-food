# models.py
class Question:
    def __init__(self, title: str, text: str, position: int, image: str, possibleAnswers: list):
        self.title = title
        self.text = text
        self.position = position
        self.image = image
        self.possibleAnswers = possibleAnswers

