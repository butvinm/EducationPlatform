from typing import Callable

import context
import structures
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRoundFlatButton
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.textfield import MDTextField
from widgets.banner import Banner


class TestTitle(MDLabel):
    """Test title widget"""

    def __init__(self, title: str, **kwargs):
        """Set appearance

        Args:
            title (str): title of test block
        """

        super().__init__(**kwargs)

        self.adaptive_height = True
        self.text = title
        self.font_style = 'H6'


class QuestionText(MDLabel):
    """Widget with test question text"""

    def __init__(self, text: str, **kwargs):
        """Set appearance

        Args:
            text (str): question text
        """

        super().__init__(**kwargs)

        self.adaptive_height = True
        self.text = text


class CheckBoxItem(MDBoxLayout):
    """Widget with CheckBox and Label"""

    def __init__(self, group: int, value: str, *args, **kwargs):
        """Set appearance and widgets

        Args:
            group (int): group of checkboxes (CheckBoxInput id)
            value (str): consisted values, displayed at label
        """

        super().__init__(*args, **kwargs)

        self.size_hint_y = None
        self.height = dp(48)

        self.group = group
        self.value = value
        self.checkbox = None
        self._update_widgets()

    def _update_widgets(self):
        """Set children widgets"""

        self.checkbox = MDCheckbox(group=self.group)
        self.add_widget(self.checkbox)
        self.add_widget(MDLabel(text=self.value))

    @property
    def is_checked(self) -> bool:
        """Return state of checkbox

        Returns:
            bool: checkbox is selected
        """

        return self.checkbox.active == True


class CheckBoxInput(MDBoxLayout):
    """Input with several checkboxes. Value is label of selected checkbox"""

    def __init__(self, values: list[str], *args, **kwargs):
        """Set appearance and widgets

        Args:
            values (list[str]): values for checkboxes
        """

        super().__init__(*args, **kwargs)

        self.adaptive_height = True

        self.values = values
        self.checkboxes: list[CheckBoxItem] = []
        self._update_widgets()

    def _update_widgets(self):
        """Set children widgets"""

        for value in self.values:
            checkbox = CheckBoxItem(id(self), value)
            self.checkboxes.append(checkbox)
            self.add_widget(checkbox)

    @property
    def value(self) -> str:
        """Return value of active checkbox

        Returns:
            str: checkbox value
        """

        for checkbox in self.checkboxes:
            if checkbox.is_checked:
                return checkbox.value


class TextFieldInput(MDBoxLayout):
    """Input with text field"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.adaptive_height = True
        self.textfield: MDTextField = None
        self._update_widgets()

    def _update_widgets(self):
        """Set children widgets"""

        self.textfield = MDTextField(hint_text='Ваш ответ')
        self.add_widget(self.textfield)

    @property
    def value(self) -> str:
        """Return value of text field

        Returns:
            str: text
        """

        return self.textfield.text


class QuestionItem(MDBoxLayout):
    """Widget with one question text and input"""

    def __init__(self, question: structures.TestQuestion, *args, **kwargs):
        """Set appearance and widgets

        Args:
            question (TestQuestion): _description_
        """
        super().__init__(*args, **kwargs)

        self.padding = [0, dp(10)]
        self.orientation = 'vertical'
        self.adaptive_height = True

        self.question = question
        self._update_widgets()

    @property
    def result(self) -> int:
        """Check answer and return result points

        Returns:
            int: taken points
        """

        return self.input.value == self.question.answer

    def _update_widgets(self):
        """Set children widgets"""

        self.add_widget(QuestionText(self.question.question))
        if self.question.input:
            self.input = CheckBoxInput(self.question.input)
        else:
            self.input = TextFieldInput()

        self.add_widget(self.input)


class SubmitButton(MDFloatLayout):
    """Widget that contain button calling test validation method"""

    def __init__(self, action: Callable, *args, **kwargs):
        """Set appearance and widgets

        Args:
            action (Callable): method, called on submitting
        """

        super().__init__(*args, **kwargs)

        self.size_hint_y = None
        self.height = dp(48)

        self.action = action
        self._update_widgets()

    def _update_widgets(self):
        """Set children widgets"""

        button = MDRoundFlatButton(text='Проверить')
        button.on_press = self.action
        button.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
        self.add_widget(button)


class TestResult(MDBoxLayout):
    """Widget displayed when test complained"""

    def __init__(self, text: str, *args, **kwargs):
        """Set appearance

        Args:
            text (str): displayed text
        """

        super().__init__(*args, **kwargs)

        self.adaptive_height = True

        self.text = text
        self._update_widgets()
    
    def _update_widgets(self):
        """Set children widgets"""

        self.add_widget(MDLabel(text=self.text, adaptive_height=True))


class TestBlock(MDBoxLayout):
    """Widget for structure.TestBlock"""

    def __init__(self, block: structures.TestBlock, *args, **kwargs):
        """Build widget from block

        Args:
            block (structures.TestBlock): inherit structure
        """

        super().__init__(*args, **kwargs)

        self.orientation = 'vertical'
        self.adaptive_height = True
        self.padding = [dp(5)]
        self.line_color = context.COLOR_RGB

        self.block = block
        self.questions: list[QuestionItem] = []
        self._update_widgets()

    def _update_widgets(self):
        """Set children widgets"""

        self.add_widget(TestTitle(self.block.title))
        for question in self.block.questions:
            question = QuestionItem(question)
            self.questions.append(question)
            self.add_widget(question)

        self.add_widget(SubmitButton(self.validate_test))

    def validate_test(self, *args):
        """Check entered answers and show pop-up with result"""

        points = 0
        max_points = len(self.questions)
        for question in self.questions:
            points += question.result

        percentage = points / max_points * 100
        if percentage >= 90:
            mark = 5
        elif percentage >= 75:
            mark = 4
        elif percentage >= 50:
            mark = 3
        else:
            mark = 2

        text = (f'Вы набрали {points} из {max_points}\n'
                f'{percentage:.2f}% - ваша оценка - {mark}')
         

        if not self.block.repeatable:
            self.clear_widgets()
            self.add_widget(TestResult(text))
            self.disabled = True

        Banner(text).open()
