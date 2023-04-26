'''
DjangoのSignal（シグナル）とは、アプリケーションの実行中に起こるイベントで、特定の処理をおこなえる機能。
'''

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile, UserPurpose, UserDesiredCohabitee, UserRoomLayout, UserRent
from matching_app.models import RoommatePreference

@receiver(post_save, sender=User)
def create_related_objects(sender, instance, created, **kwargs):
    # Userモデル作成(ユーザー登録)後にこの関数は自動で実行されUser.userに関連するオブジェクトを作成する。
    print('create_related_objects 起動')
    if created:
        # main_app.modelsに定義したuser関連obj
        UserProfile.objects.create(user=instance)
        UserPurpose.objects.create(user=instance)
        UserDesiredCohabitee.objects.create(user=instance)
        UserRoomLayout.objects.create(user=instance)
        UserRent.objects.create(user=instance)
        
        
        # matching_app.modelsに定義したuser関連obj
        RoommatePreference.objects.create(user=instance)



from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Prefecture

PREFECTURE_DATA = [
    '北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県', '茨城県', '栃木県', '群馬県',
    '埼玉県', '千葉県', '東京都', '神奈川県', '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', 
    '岐阜県', '静岡県', '愛知県', '三重県', '滋賀県', '京都府', '大阪府', '兵庫県','奈良県', '和歌山県', 
    '鳥取県', '島根県', '岡山県', '広島県', '山口県', '徳島県', '香川県', '愛媛県', '高知県', '福岡県', 
    '佐賀県', '長崎県','熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県',
]
# post_migrateシグナルをリッスンして、create_prefectures関数を実行します。
@receiver(post_migrate, sender=Prefecture)
def create_prefectures(sender, **kwargs):
# create_prefectures関数では、Prefectureモデルに初期データが存在しない場合に、都道府県データを追加します。
    if Prefecture.objects.exists():
        print('prefecture is ')
        return
    print('prefecture is not, create name ')
    for name in PREFECTURE_DATA:
        Prefecture.objects.create(name=name)
