from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(decimal_places=3,max_digits=11)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    fromAccount = models.ForeignKey(Account, on_delete=models.CASCADE)
    toAccount = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='%(class)s_requests_to_account')
    amount = models.DecimalField(decimal_places=3,max_digits=11)
    sentAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "From: " + self.fromAccount + " To: " + self.toAccount

class Balance(models.Model):
    amount = models.DecimalField(decimal_places=3,max_digits=11)
    balance = models.DecimalField(decimal_places=3,max_digits=11)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner + ' $' + self.amount
