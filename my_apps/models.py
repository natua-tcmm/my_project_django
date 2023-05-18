from django.db import models

# Create your models here.

# DB構造を変化させたくなったら
# ・モデルを変更する (models.py の中の)
# ・これらの変更のためのマイグレーションを作成するために python manage.py makemigrations を実行します。
# ・データベースにこれらの変更を適用するために python manage.py migrate を実行します。
# https://docs.djangoproject.com/ja/4.2/intro/tutorial02/

class SongData(models.Model):

    # 曲名など
    song_name = models.CharField(max_length=100)
    song_name_reading = models.CharField(max_length=100)
    song_auther = models.CharField(max_length=100)

    # カテゴリ
    song_catname = models.CharField(max_length=20)

    song_bpm = models.IntegerField()
    song_release = models.DateField()

    # レベル
    expert_const = models.DecimalField(max_digits=4,decimal_places=1)
    expert_notes = models.IntegerField()

    master_const = models.DecimalField(max_digits=4,decimal_places=1)
    master_notes = models.IntegerField()

    ultima_const = models.DecimalField(max_digits=4,decimal_places=1)
    ultima_notes = models.IntegerField()

    # 定数の未確定さ
    is_const_unknown = models.BooleanField()
