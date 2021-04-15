from django.db import models

#원격DB용
# class Store(models.Model):
    # num = models.AutoField(primary_key=True)
    # id = models.CharField(max_length=45)
    # password = models.CharField(max_length=45)
    # name = models.CharField(max_length=45)
    # category = models.CharField(max_length=45)
    # location = models.CharField(max_length=100)
    # regdate = models.DateTimeField()
    #
    # class Meta:
        # managed = False
        # db_table = 'store'

#개인DB용
class Store(models.Model):
    store_seq = models.AutoField(db_column='STORE_SEQ', primary_key=True)  # Field name made lowercase.
    store_id = models.CharField(db_column='STORE_ID', max_length=20)  # Field name made lowercase.
    store_pwd = models.CharField(db_column='STORE_PWD', max_length=20)  # Field name made lowercase.
    store_name = models.CharField(db_column='STORE_NAME', max_length=50)  # Field name made lowercase.
    store_ctg = models.CharField(db_column='STORE_CTG', max_length=20)  # Field name made lowercase.
    store_loc = models.CharField(db_column='STORE_LOC', max_length=100)  # Field name made lowercase.
    store_tel = models.CharField(db_column='STORE_TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='REGDATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store'