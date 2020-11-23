from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Entry(models.Model):
    """Something about the topic."""
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.text}..."

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model.""" 
        return self.text

class Sizes(models.Model):
    size = models.CharField(max_length=100)
    def __str__(self):
        return self.size

class Drinks(models.Model):
    name = models.CharField(max_length=15)
    size = models.ForeignKey(Sizes, default=1, on_delete=models.CASCADE)
    price = models.FloatField()
    def __str__(self):
        return f"Drink Name: {self.name}. Price: {self.price}. Size: {self.size}"

class Person(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    favourite_drink = models.ForeignKey(Drinks, default=1, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Test(models.Model):
    text = models.CharField(max_length=350)
    number = models.IntegerField()
    def __str__(self):
        return self.text
class Test2(models.Model):
    text = models.ForeignKey(Test, on_delete=models.CASCADE)
    number = models.IntegerField()
    def __str__(self):
        return self.text


