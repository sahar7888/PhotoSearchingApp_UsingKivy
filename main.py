
""" Ref: Intermediate to Advanced Python with 10 OOP Projects-Udemy
"""


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def get_image_link(self):
        # Get user query from textinput
        query = self.manager.current_screen.ids.user_query.text
        print(query)
        # Get wikipedia page and the first image link
        page = wikipedia.page(query,auto_suggest=False)
        image_link = page.images[0]
        print(image_link)
        return image_link


    def download_image(self):
        # Download the image
        headers = {

            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"

        }
        req = requests.get(self.get_image_link(),headers=headers)
        img_path = 'Files/photo.jpg'
        with open(img_path, 'wb') as file:
            file.write(req.content)

        return img_path
    def set_image(self):
        # set the image in the image widget
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
