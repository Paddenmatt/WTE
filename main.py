from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import random

Builder.load_string("""
    
<StartScreen>:
    name: 'start'
    MDLabel:
        text: 'What 2 Eat'
        theme_text_color: 'Custom'
        text_color: (1, 1, 1, 1)
        halign: 'center'
   
    MDRectangleFlatButton:
        text: 'Lets Eat!'
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0.65, 0, 1)
        pos_hint: {'center_x':0.5,'center_y':0.3}
        on_press: 
            root.manager.current = 'option1'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: "I Don't Know!"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0.45, 0, 1)
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: 
            app.idk_rand()
            root.manager.current = 'decision'
            root.manager.transition.direction = "left"

<Option1Screen>:
    name: 'option1'
    Image:
        source: "images/dining.jpg"
        pos_hint: {'center_x':0.3,'center_y':0.65}
        allow_stretch: True
        keep_ratio: False
        size_hint_y: None
        height: dp(200)
        size_hint_x: None
        width: dp(120)
    Image:
        source: "images/cooking.jpg"
        pos_hint: {'center_x':0.7,'center_y':0.65}
        allow_stretch: True
        keep_ratio: False
        size_hint_y: None
        height: dp(200)
        size_hint_x: None
        width: dp(120)
        
    MDRectangleFlatButton:
        text: 'Dining Out'
        pos_hint: {'center_x':0.3,'center_y':0.31}
        on_press: 
            app.dining_press()
            root.manager.current = 'option2'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Cook at Home'
        pos_hint: {'center_x':0.7,'center_y':0.31}
        on_press: 
            app.cooking_press()
            root.manager.current = 'option2'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: "Choose For Me"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: 
            app.opt1_rand()
            root.manager.current = 'option2'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Start Over'
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: 
            root.manager.current = 'start'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
    MDRectangleFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.3,'center_y':0.1}
        on_press: 
            root.manager.current = 'start'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)

<Option2Screen>:
    name: 'option2'
    Image:
        source: "images/sweet.jpg"
        pos_hint: {'center_x':0.3,'center_y':0.65}
        allow_stretch: True
        keep_ratio: False
        size_hint_y: None
        height: dp(200)
        size_hint_x: None
        width: dp(120)
    Image:
        source: "images/salty.jpg"
        pos_hint: {'center_x':0.7,'center_y':0.65}
        allow_stretch: True
        keep_ratio: False
        size_hint_y: None
        height: dp(200)
        size_hint_x: None
        width: dp(120)
        
    MDRectangleFlatButton:
        text: 'Sweet'
        pos_hint: {'center_x':0.3,'center_y':0.31}
        on_press: 
            app.sweet_press()
            root.manager.current = 'option3'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Salty'
        pos_hint: {'center_x':0.7,'center_y':0.31}
        on_press: 
            app.salty_press()
            root.manager.current = 'option3'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: "Choose For Me"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: 
            app.opt2_rand()
            root.manager.current = 'option3'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Start Over'
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: 
            root.manager.current = 'start'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
    MDRectangleFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.3,'center_y':0.1}
        on_press: 
            root.manager.current = 'option1'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
            
<Option3Screen>:
    name: 'option3'
    Image:
        source: "images/healthy.jpg"
        pos_hint: {'center_x':0.3,'center_y':0.65}
        allow_stretch: True
        keep_ratio: False
        size_hint_y: None
        height: dp(200)
        size_hint_x: None
        width: dp(120)
    Image:
        source: "images/unhealthy.jpg"
        pos_hint: {'center_x':0.7,'center_y':0.65}
        allow_stretch: True
        keep_ratio: False
        size_hint_y: None
        height: dp(200)
        size_hint_x: None
        width: dp(120)
        
    MDRectangleFlatButton:
        text: 'Healthy'
        pos_hint: {'center_x':0.3,'center_y':0.31}
        on_press: 
            app.healthy_press()
            root.manager.current = 'option4'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Casual'
        pos_hint: {'center_x':0.7,'center_y':0.31}
        on_press: 
            app.casual_press()
            root.manager.current = 'option4'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: "Choose For Me"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: 
            app.opt3_rand()
            root.manager.current = 'option4'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Start Over'
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: 
            root.manager.current = 'option2'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
    MDRectangleFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.3,'center_y':0.1}
        on_press: 
            root.manager.current = 'option2'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
            
<Option4Screen>:
    name: 'option4'
    Image:
        source: "images/light.jpg"
        pos_hint: {'center_x':0.3,'center_y':0.65}
        allow_stretch: True
        keep_ratio: False
        size_hint_y: None
        height: dp(200)
        size_hint_x: None
        width: dp(120)
    Image:
        source: "images/full.jpg"
        pos_hint: {'center_x':0.7,'center_y':0.65}
        allow_stretch: True
        keep_ratio: False
        size_hint_y: None
        height: dp(200)
        size_hint_x: None
        width: dp(120)
        
    MDRectangleFlatButton:
        text: 'Light'
        pos_hint: {'center_x':0.3,'center_y':0.31}
        on_press: 
            app.light_press()
            root.manager.current = 'option5'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Heavy'
        pos_hint: {'center_x':0.7,'center_y':0.31}
        on_press: 
            app.heavy_press()
            root.manager.current = 'option5'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: "Choose For Me"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: 
            app.opt4_rand()
            root.manager.current = 'option5'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Start Over'
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: 
            root.manager.current = 'start'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
    MDRectangleFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.3,'center_y':0.1}
        on_press: 
            root.manager.current = 'option3'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
            
<Option5Screen>:
    name: 'option5'
    MDRectangleFlatButton:
        text: 'Left Option'
        pos_hint: {'center_x':0.3,'center_y':0.3}
        on_press: 
            root.manager.current = 'decision'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Right Option'
        pos_hint: {'center_x':0.7,'center_y':0.3}
        on_press: 
            root.manager.current = 'decision'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: "Choose For Me"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: 
            root.manager.current = 'decision'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Start Over'
        pos_hint: {'center_x':0.7,'center_y':0.1}
        on_press: 
            root.manager.current = 'start'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
    MDRectangleFlatButton:
        text: 'Go Back'
        pos_hint: {'center_x':0.3,'center_y':0.1}
        on_press: 
            root.manager.current = 'option4'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
            
<DecisionScreen>:
    name: 'decision'
    MDLabel:
        text: "Here's what we think you will like:"
        theme_text_color: 'Custom'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        text_color: (1, 1, 1, 1)
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Start Over'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: 
            app.user_answers()
            root.manager.current = 'start'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)

""")


class StartScreen(Screen):
    pass


class Option1Screen(Screen):
    pass


class Option2Screen(Screen):
    pass


class Option3Screen(Screen):
    pass


class Option4Screen(Screen):
    pass


class Option5Screen(Screen):
    pass


class DecisionScreen(Screen):
    pass


class User:
    default = "undecided"
    question1 = default
    question2 = default
    question3 = default
    question4 = default
    question5 = default


user1 = User()


class What2EatApp(MDApp):

    # Functions for Option1Screen
    def dining_press(self):  # If Dining Out is selected, set question 1 to "dining"
        user1.question1 = "dining out"

    def cooking_press(self):  # If Cooking at Home is selected, set question 1 to "cooking"
        user1.question1 = "cook at home"

    def opt1_rand(self):  # If Choose For Me is selected, randomly set question 1 value
        num = random.randint(0, 1)
        if num == 0:
            user1.question1 = "dining out"
        else:
            user1.question1 = "cook at home"

    # Functions for Option2Screen
    def sweet_press(self):  # If Sweet is selected, set question 2 to "sweet"
        user1.question2 = "sweet"

    def salty_press(self):  # If Salty is selected, set question 2 to "salty"
        user1.question2 = "salty"

    def opt2_rand(self):  # If Choose For Me is selected, randomly set question 2 value
        num = random.randint(0, 1)
        if num == 0:
            user1.question2 = "sweet"
        else:
            user1.question2 = "salty"

    # Functions for Option3Screen
    def healthy_press(self):  # If Healthy is selected, set question 3 to "healthy"
        user1.question3 = "healthy"

    def casual_press(self):  # If Casual is selected, set question 3 to "casual"
        user1.question3 = "casual"

    def opt3_rand(self):  # If Choose For Me is selected, randomly set question 3 value
        num = random.randint(0, 1)
        if num == 0:
            user1.question3 = "healthy"
        else:
            user1.question3 = "casual"

    # Functions for Option4Screen
    def light_press(self):  # If Light is selected, set question 4 to "light"
        user1.question4 = "light"

    def heavy_press(self):  # If Heavy is selected, set question4 to "heavy"
        user1.question4 = "heavy"

    def opt4_rand(self):  # If Choose For Me is selected, randomly set question 4 value
        num = random.randint(0, 1)
        if num == 0:
            user1.question4 = "light"
        else:
            user1.question4 = "heavy"

    def idk_rand(self):
        num = random.randint(0, 1)
        if num == 0:
            user1.question1 = "dining out"
        else:
            user1.question1 = "cook at home"
        num = random.randint(0, 1)
        if num == 0:
            user1.question2 = "sweet"
        else:
            user1.question2 = "salty"
        num = random.randint(0, 1)
        if num == 0:
            user1.question3 = "healthy"
        else:
            user1.question3 = "casual"
        num = random.randint(0, 1)
        if num == 0:
            user1.question4 = "light"
        else:
            user1.question4 = "heavy"

    # Functions
    def user_answers(self):
        print(user1.question1 + ", ",
              user1.question2 + ", ",
              user1.question3 + ", ",
              user1.question4 + ", ",
              user1.question5)


    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(Option1Screen(name='option1'))
        sm.add_widget(Option2Screen(name='option2'))
        sm.add_widget(Option3Screen(name='option3'))
        sm.add_widget(Option4Screen(name='option4'))
        sm.add_widget(Option5Screen(name='option5'))
        sm.add_widget(DecisionScreen(name='decision'))

        self.theme_cls.theme_style = "Dark"

        return sm


What2EatApp().run()
