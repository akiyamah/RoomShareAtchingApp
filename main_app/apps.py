'''
ここにはappの設定を記述することでその内容をconfigフォルダのsettings.pyで読み込めるようにし、
結果的にプロジェクト全体に、該当するappの機能を反映しています。
'''

# main_app/apps.py
from django.apps import AppConfig

class MainAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_app'
    
    def ready(self):
        import main_app.signals
