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
        return f'Drink Size: {self.size}.'

class Drinks(models.Model):
    name = models.CharField(max_length=15)
    size = models.ForeignKey(Sizes, default=1, on_delete=models.SET_DEFAULT)
    price = models.FloatField()
    def __str__(self):
        return f"Drink Name: {self.name}. Price: {self.price}. Size: {self.size}"

