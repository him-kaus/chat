from django.db import models

class User1(models.Model):
    name1 = models.CharField(max_length=40, null=True, blank=True)
    phno = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True,blank=True)
    password = models.CharField(max_length=500, null=True, blank=True)

    def isExists(self):
        if User1.objects.filter(email = self.email):
            return True

        return False

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return User1.objects.get(email=email)
        except:
            return False



