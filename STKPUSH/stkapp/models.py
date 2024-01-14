from django.db import models

# Create your models here.
class MpesaResponse(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_reference = models.CharField(max_length=50)
    transaction_desc = models.CharField(max_length=255)
    callback_url = models.URLField()
    response = models.TextField()

    def __str__(self):
        return f"{self.phone_number} - {self.amount}"
