from django.db import models

# Create your models here.
class WordList(models.Model):
    word_seq = models.AutoField(db_column='WORD_SEQ', primary_key=True)  # Field name made lowercase.
    keyword = models.CharField(db_column='KEYWORD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    word_year = models.CharField(db_column='WORD_YEAR', max_length=4, blank=True, null=True)  # Field name made lowercase.
    word_mon = models.CharField(db_column='WORD_MON', max_length=2, blank=True, null=True)  # Field name made lowercase.
    word_word = models.CharField(db_column='WORD_WORD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    word_cnt = models.IntegerField(db_column='WORD_CNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'word_list'