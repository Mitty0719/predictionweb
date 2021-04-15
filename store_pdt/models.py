from django.db import models
from store.models import Store
# Create your models here.
class StorePdt(models.Model):
    pdt_seq = models.AutoField(db_column='PDT_SEQ', primary_key=True)  # Field name made lowercase.
    pdt_name = models.CharField(db_column='PDT_NAME', max_length=20)  # Field name made lowercase.
    pdt_disc = models.CharField(db_column='PDT_DISC', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pdt_cnt = models.IntegerField(db_column='PDT_CNT')  # Field name made lowercase.
    pdt_price = models.IntegerField(db_column='PDT_PRICE')  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='REGDATE', blank=True, null=True)  # Field name made lowercase.
    store_seq = models.ForeignKey(Store, models.DO_NOTHING, db_column='STORE_SEQ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store_pdt'