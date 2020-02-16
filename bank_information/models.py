from django.db import models


class Banks(models.Model):
    id = models.BigIntegerField(blank=False, primary_key=True)
    name = models.CharField(max_length=49)

    class Meta:
        db_table = 'banks'
        indexes = [
            models.Index(fields=['id'], name='banks_id_pkey'),
        ]


class Branches(models.Model):
    bank = models.ForeignKey(Banks, on_delete=models.CASCADE)
    ifsc = models.CharField(max_length=11, primary_key=True)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    class Meta:
        db_table = 'branches'
        indexes = [
            models.Index(fields=['ifsc'], name='branches_ifsc_pkey'),
        ]


class BankBranches(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank = models.ForeignKey(Branches, on_delete=models.DO_NOTHING)
    bank_name = models.CharField(max_length=49)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    class Meta:
        managed = False
        db_table = 'bank_branches'
