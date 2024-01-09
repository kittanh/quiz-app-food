# serialization.py
def question_to_dict(question):
    return {
        "title": question.title,
        "text": question.text,
        "position": question.position,
        "image": question.image,
        "possibleAnswers": question.possibleAnswers
    }

def dict_to_question(data):
    return Question(
        title=data["title"],
        text=data["text"],
        position=data["position"],
        image=data["image"],
        possibleAnswers=data["possibleAnswers"]
    )
