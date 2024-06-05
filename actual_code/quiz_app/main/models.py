from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=20, unique=True)
    category_1 = models.CharField(max_length=20)
    category_2 = models.CharField(max_length=20)
    category_3 = models.CharField(max_length=20, null=True, blank=True)
    category_4 = models.CharField(max_length=20, null=True, blank=True)
    number_of_questions_per_category = models.IntegerField(default=5, validators=[MaxValueValidator(5, 'There can be a maximum of 5 questions per category')])


    def __str__(self):
        return self.name


def get_image_name(instance, filename):
    return f"images/{instance.game} {instance} {filename}"



class Question(models.Model):
    question_text = models.TextField(blank=True, null=True, default='Some question')
    question_image = models.ImageField(upload_to=get_image_name, blank=True, null=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    points = models.IntegerField()
    category = models.CharField(max_length=20)
    answer = models.CharField(max_length=50, default='Some Answer')

    def clean(self):
        if not (self.category in (self.game.category_1, self.game.category_2, self.game.category_3, self.game.category_4)) :
            raise ValidationError(
                _('The category must be a category within the game')
            )
        
        if not (self.question_text or self.question_image):
            raise ValidationError(
                _('The text or image must be present')
            )

        super().clean()

    def delete(self, *args, **kwargs):
        self.question_image.delete()
        super(Question, self).delete(*args, **kwargs)

    
    def __str__(self):
        return f"{self.category} for {self.points} in {self.game.name}"


        