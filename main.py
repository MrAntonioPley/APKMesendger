from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

questions = [
    {
        "question": "Как ты восстанавливаешь силы, когда чувствуешь сильную усталость?",
        "options": [("Звоню друзьям и вместе мы что-то придумаем", "E"),
                    ("Мне нужен покой: я читаю книги, смотрю кино", "I")]
    },
    {
        "question": "Какое описание тебе больше подходит?",
        "options": [("Я люблю жить моментом, здесь и сейчас...", "S"),
                    ("Я обожаю мечтать, придумывать что-то новое...", "N")]
    },
    {
        "question": "Когда мне нужно принять очень важное решение, то я:",
        "options": [("Стараюсь думать головой. В таких вопросах нужна логика", "T"),
                    ("Слушаю свое сердце, прислушиваюсь к эмоциям", "F")]
    },
    {
        "question": "Когда у меня что-то запланировано, я:",
        "options": [("Заранее продумываю детали, мне нужен четкий план", "J"),
                    ("Предпочитаю ориентироваться по ситуации", "P")]
    }
]

# Таблица совместимости (можно доработать)
compatibility = {
    "INTJ": ["ENFP", "ENTP"],
    "INTP": ["ENTJ", "ESTJ"],
    "ENTJ": ["INFP", "INTP"],
    "ENTP": ["INFJ", "INTJ"],
    "INFJ": ["ENFP", "ENTP"],
    "INFP": ["ENFJ", "ESFJ"],
    "ENFJ": ["INFP", "ISFP"],
    "ENFP": ["INFJ", "INTJ"],
    "ISTJ": ["ESFP", "ESTP"],
    "ISFJ": ["ESFP", "ESTP"],
    "ESTJ": ["ISFP", "ISTP"],
    "ESFJ": ["ISFP", "ISTP"],
    "ISTP": ["ESFJ", "ENFJ"],
    "ISFP": ["ESFJ", "ENFJ"],
    "ESTP": ["ISFJ", "ISTJ"],
    "ESFP": ["ISFJ", "ISTJ"]
}


class MBTITest(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.current_q = 0
        self.answers = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        self.question_label = Label(text="", font_size=20)
        self.add_widget(self.question_label)
        self.option_buttons = [Button(), Button()]
        for btn in self.option_buttons:
            btn.bind(on_press=self.on_answer)
            self.add_widget(btn)
        self.load_question()

    def load_question(self):
        if self.current_q < len(questions):
            q = questions[self.current_q]
            self.question_label.text = q["question"]
            for i, (text, _) in enumerate(q["options"]):
                self.option_buttons[i].text = text
        else:
            self.show_result()

    def on_answer(self, instance):
        selected_option = instance.text
        q = questions[self.current_q]
        for text, value in q["options"]:
            if text == selected_option:
                self.answers[value] += 1
        self.current_q += 1
        self.load_question()

    def show_result(self):
        # Формируем тип
        mbti = ""
        mbti += "E" if self.answers["E"] >= self.answers["I"] else "I"
        mbti += "S" if self.answers["S"] >= self.answers["N"] else "N"
        mbti += "T" if self.answers["T"] >= self.answers["F"] else "F"
        mbti += "J" if self.answers["J"] >= self.answers["P"] else "P"
        comp = compatibility.get(mbti, ["Неизвестно", "Неизвестно"])

        self.clear_widgets()
        self.add_widget(Label(text=f"Твой тип личности: {mbti}", font_size=24))
        self.add_widget(Label(text=f"Подходящие типы: {comp[0]}, {comp[1]}", font_size=20))


class MBTIApp(App):
    def build(self):
        return MBTITest()


if __name__ == "__main__":
    MBTIApp().run()
