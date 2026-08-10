from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

class BlueScreen(Screen):
    def __init__(self, **kwargs):
        super(BlueScreen, self).__init__(**kwargs)
        
        # رسم یک مستطیل آبی رنگ در پس‌زمینه
        with self.canvas.before:
            # رنگ آبی در قالب RGBA (قرمز=0، سبز=0، آبی=0.8، شفافیت=1)
            Color(0.1, 0.4, 0.8, 1) 
            self.rect = Rectangle(size=self.size, pos=self.pos)
            
        # هماهنگ کردن اندازه پس‌زمینه با تغییر اندازه صفحه
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class MyApp(App):
    def build(self):
        # ساخت مدیریت صفحات و اضافه کردن صفحه آبی
        sm = ScreenManager()
        sm.add_widget(BlueScreen(name='blue_screen'))
        return sm

if __name__ == '__main__':
    # در ویندوز برای تست رنگ، سایز پنجره را شبیه به گوشی می‌کنیم
    Window.size = (360, 640)
    MyApp().run()
