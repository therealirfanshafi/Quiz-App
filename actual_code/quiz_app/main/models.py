from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=20)
    category_1 = models.CharField(max_length=20)
    category_2 = models.CharField(max_length=20)
    category_3 = models.CharField(max_length=20, null=True, blank=True)
    category_4 = models.CharField(max_length=20, null=True, blank=True)


def get_image_name(instance, filename):
    return f"images/{instance.id} {filename}"



class Question(models.Model):
    question_text = models.TextField(blank=True, null=True)
    question_image = models.ImageField(upload_to=get_image_name, blank=True, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)

    def clean(self):
        if not (self.category in (self.game.category_1, self.game.category_2, self.game.category_3, self.game.category_4)) :
            raise ValidationError(
                _('The category must be a category within the game')
            )
        
        super().clean()


        