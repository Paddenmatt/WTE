from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image, AsyncImage

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
            root.manager.current = 'diningOption'
            root.manager.transition.direction = "left"

<DiningOptionScreen>:
    name: 'diningOption'
    MDRectangleFlatButton:
        text: 'Dining Out'
        pos_hint: {'center_x':0.3,'center_y':0.5}
        on_press: 
            root.manager.current = 'option1'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Cook at Home'
        pos_hint: {'center_x':0.7,'center_y':0.5}
        on_press: 
            root.manager.current = 'cooking'
            root.manager.transition.direction = "left"
            
<CookingScreen>:
    name: 'cooking'
    MDLabel:
        text: 'Recipes'
        theme_text_color: 'Custom'
        text_color: (1, 1, 1, 1)
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Start Over'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: 
            root.manager.current = 'start'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)

<Option1Screen>:
    name: 'option1'
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
            root.manager.current = 'option2'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Salty'
        pos_hint: {'center_x':0.7,'center_y':0.31}
        on_press: 
            root.manager.current = 'option2'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: "I Don't Know"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: 
            root.manager.current = 'option2'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Start Over'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: 
            root.manager.current = 'start'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
            
<Option2Screen>:
    name: 'option2'
    MDRectangleFlatButton:
        text: 'Left Option'
        pos_hint: {'center_x':0.3,'center_y':0.3}
        on_press: 
            root.manager.current = 'option3'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Right Option'
        pos_hint: {'center_x':0.7,'center_y':0.3}
        on_press: 
            root.manager.current = 'option3'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: "I Don't Know"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: 
            root.manager.current = 'option3'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Start Over'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: 
            root.manager.current = 'start'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
            
<Option3Screen>:
    name: 'option3'
    MDRectangleFlatButton:
        text: 'Left Option'
        pos_hint: {'center_x':0.3,'center_y':0.3}
        on_press: 
            root.manager.current = 'option4'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Right Option'
        pos_hint: {'center_x':0.7,'center_y':0.3}
        on_press: 
            root.manager.current = 'option4'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: "I Don't Know"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: 
            root.manager.current = 'option4'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Start Over'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: 
            root.manager.current = 'start'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
            
<Option4Screen>:
    name: 'option4'
    MDRectangleFlatButton:
        text: 'Left Option'
        pos_hint: {'center_x':0.3,'center_y':0.3}
        on_press: 
            root.manager.current = 'option5'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Right Option'
        pos_hint: {'center_x':0.7,'center_y':0.3}
        on_press: 
            root.manager.current = 'option5'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: "I Don't Know"
        pos_hint: {'center_x':0.5,'center_y':0.2}
        on_press: 
            root.manager.current = 'option5'
            root.manager.transition.direction = "left"
    MDRectangleFlatButton:
        text: 'Start Over'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: 
            root.manager.current = 'start'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)
            
<Option5Screen>:
    name: 'option5'
    MDRectangleFlatButton:
        text: 'Left Option'
        pos_hint: {'center_x':0.3,'center_y':0.3}
    MDRectangleFlatButton:
        text: 'Right Option'
        pos_hint: {'center_x':0.7,'center_y':0.3}
    MDRectangleFlatButton:
        text: "I Don't Know"
        pos_hint: {'center_x':0.5,'center_y':0.2}
    MDRectangleFlatButton:
        text: 'Start Over'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: 
            root.manager.current = 'start'
            root.manager.transition.direction = "right"
        text_color: (1, 1, 1, 1)
        md_bg_color: (1, 0, 0, 1)

""")


class StartScreen(Screen):
    pass


class DiningOptionScreen(Screen):
    pass


class CookingScreen(Screen):
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






class What2EatApp(MDApp):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(StartScreen(name='start'))
        sm.add_widget(DiningOptionScreen(name='diningOption'))
        sm.add_widget(CookingScreen(name='cooking'))
        sm.add_widget(Option1Screen(name='option1'))
        sm.add_widget(Option2Screen(name='option2'))
        sm.add_widget(Option3Screen(name='option3'))
        sm.add_widget(Option4Screen(name='option4'))
        sm.add_widget(Option5Screen(name='option5'))

        self.theme_cls.theme_style = "Dark"
        
        return sm


What2EatApp().run()
