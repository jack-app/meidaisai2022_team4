from django.db import models
# ユーザー認証
from django.contrib.auth.models import User

# ユーザーアカウントのモデルクラス
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 追加フィールド
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username