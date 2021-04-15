from django.db import models

# Create your models here.
class CardUsedata(models.Model):
    use_seq = models.AutoField(db_column='USE_SEQ', primary_key=True)  # Field name made lowercase.
    use_date = models.CharField(db_column='USE_DATE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    use_loc = models.CharField(db_column='USE_LOC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    use_ctg = models.CharField(db_column='USE_CTG', max_length=30, blank=True, null=True)  # Field name made lowercase.
    use_ctg_detail = models.CharField(db_column='USE_CTG_DETAIL', max_length=30, blank=True, null=True)  # Field name made lowercase.
    use_age = models.CharField(db_column='USE_AGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    use_pay = models.IntegerField(db_column='USE_PAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'card_usedata'

