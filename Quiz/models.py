from django.db import models

# Create your models here.
class Quiz(models.Model):
    no=models.IntegerField()
    qns=models.TextField()
    ans=models.CharField(max_length=50)

    def __str__(self):
        return self.qns



class Quiz1(models.Model):
    n1 = models.IntegerField()
    qns1=models.TextField()
    ans1=models.CharField(max_length=50)


    def __str__(self):
        return self.qns1

class Quiz2(models.Model):
    n2 = models.IntegerField()
    qns2=models.TextField()
    ans2=models.CharField(max_length=50)


    def __str__(self):
        return self.qns2

class Quiz3(models.Model):
    n3 = models.IntegerField()
    qns3=models.TextField()
    ans3=models.CharField(max_length=50)


    def __str__(self):
        return self.qns3

class Quiz4(models.Model):
    n4 = models.IntegerField()
    qns4=models.TextField()
    ans4=models.CharField(max_length=50)


    def __str__(self):
        return self.qns4

class Quiz5(models.Model):
    n5 = models.IntegerField()
    qns5=models.TextField()
    ans5=models.CharField(max_length=50)


    def __str__(self):
        return self.qns5

class Quiz6(models.Model):
    n6= models.IntegerField()
    qns6=models.TextField()
    ans6=models.CharField(max_length=50)


    def __str__(self):
        return self.qns6
class Quiz7(models.Model):
    n7 = models.IntegerField()
    qns7=models.TextField()
    ans7=models.CharField(max_length=50)


    def __str__(self):
        return self.qns7
class Quiz8(models.Model):
    n8 = models.IntegerField()
    qns8=models.TextField()
    ans8=models.CharField(max_length=50)


    def __str__(self):
        return self.qns8
class Quiz9(models.Model):
    n9 = models.IntegerField()
    qns9=models.TextField()
    ans9=models.CharField(max_length=50)


    def __str__(self):
        return self.qns9

class Quiz10(models.Model):
    n10= models.IntegerField()
    qns10=models.TextField()
    ans10=models.CharField(max_length=50)


    def __str__(self):
        return self.qns10





