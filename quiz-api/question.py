# models.py
class Question:
    def __init__(self, title: str, text: str, position: int, image: str, possibleAnswers: list):
        self.title = title
        self.text = text
        self.position = position
        self.image = image
        self.possibleAnswers = possibleAnswers

    def to_dict(self):
        return {
            "title": self.title,
            "text": self.text,
            "position": self.position,
            "image": self.image,
            "possibleAnswers": self.possibleAnswers
        }