from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _


# model for a game (i.e a round being played such as the finals)
class Game(models.Model):
    name = models.CharField(max_length=20, unique=True)  # e.g Quater Finals

    # the four categories in a game, at least 2 are required 
    category_1 = models.CharField(max_length=20) 
    category_2 = models.CharField(max_length=20)
    category_3 = models.CharField(max_length=20, null=True, blank=True)
    category_4 = models.CharField(max_length=20, null=True, blank=True)

    number_of_questions_per_category = models.IntegerField(default=5, validators=[MaxValueValidator(5, 'There can be a maximum of 5 questions per category')])


    def __str__(self):
        return self.name


# method to determine the name of an image being stores to prevent any name collisions 
def get_image_name(instance, filename):
    return f"images/{instance.game} {instance} {filename}"


# a question in a game 
class Question(models.Model):

    # the question may be in the form of a taext or image or both 
    question_text = models.TextField(blank=True, null=True, default='Some question')
    question_image = models.ImageField(upload_to=get_image_name, blank=True, null=True)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)  # links the question to a game 

    points = models.IntegerField()  # score awarded when the question is answered correctly or a subtracted when answered incorrectly
    category = models.CharField(max_length=20)  # e.g Statistics 
    answer = models.CharField(max_length=50, default='Some Answer')  # the correct answer to the question

    def clean(self):

        # validation to ensure that the category of the question is available in the category of the game 
        if not (self.category in (self.game.category_1, self.game.category_2, self.game.category_3, self.game.category_4)) :
            raise ValidationError(
                _('The category must be a category within the game')
            )
        
        # validation to ensure that either text or an image is entered for a question 
        if not (self.question_text or self.question_image):  
            raise ValidationError(
                _('The text or image must be present')
            )

        super().clean()

    # ensures that the image stored in the media directory is also deleted when a question is deleted
    def delete(self, *args, **kwargs):
        self.question_image.delete()
        super(Question, self).delete(*args, **kwargs)

    
    def __str__(self):
        return f"{self.category} for {self.points} in {self.game.name}"


        