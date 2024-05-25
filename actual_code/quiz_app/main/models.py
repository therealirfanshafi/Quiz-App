from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=20)
    category_1 = models.CharField(max_length=20)
    category_2 = models.CharField(max_length=20)
    category_3 = models.CharField(max_length=20, null=True, blank=True)
    category_4 = models.CharField(max_length=20, null=True, blank=True)

class Question(models.Model):
    question_text = models.TextField()
    question_image = models.BinaryField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    
    def get_categories(self):
        possible_categories = {self.game.category_1: self.game.category_1, self.game.category_2: self.game.category_2}

        if self.game.category_3:
            possible_categories[self.game.category_3] = self.game.category_3

        if self.game.category_4:
            possible_categories[self.game.category_3] = self.game.category_4

        return possible_categories
    
    category = models.CharField(max_length=20, choices=get_categories)


        
