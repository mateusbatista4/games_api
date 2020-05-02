from django.db import models

#
class EsrbRating(models.Model):
    description = models.CharField(max_length=200)

    class Meta:
        ordering = ('description',)

    def __str__(self):
        return self.description




class Game(models.Model):
    created_timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200,default='')
    release_date = models.DateTimeField()
    esrb_rating = models.ForeignKey(
        EsrbRating,
        related_name = 'games',
        on_delete=models.CASCADE
    )
    played_once = models.BooleanField(default=False)
    played_times = models.IntegerField(default=0)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=200,default='')

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE,'Male'),
        (FEMALE,'Female')
    )
    created = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(
        max_length= 50,
        choices =GENDER_CHOICES,
        default= MALE
    ),

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class PlayerScore(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name= 'scores'
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE
    )
    score = models.IntegerField()
    score_date = models.DateTimeField()

    class Meta:
        ordering = ('-score',)

    def __str__(self):
        return self.game.name +' - ' +self.player.name+ ' score'