
from .models import Game, EsrbRating, Player, PlayerScore
from rest_framework import serializers
from rest_framework import generics




class EsrbRatingSerializer(serializers.HyperlinkedModelSerializer):

    games = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='games-detail'
    )

    class Meta:
        model = EsrbRating
        fields = ('url', 'id', 'description', 'games')


class GameSerializer(serializers.HyperlinkedModelSerializer):
    esrb_rating = serializers.SlugRelatedField(
        queryset=EsrbRating.objects.all(),
        slug_field='description'
    )

    class Meta:
        model = Game
        fields = '__all__'


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = GameSerializer()

    class Meta:
        model = PlayerScore
        fields = '__all__'


class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    scores = ScoreSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(
        choices=Player.GENDER_CHOICES
    )
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True
    )

    class Meta:
        model = Player
        fields = '__all__'


class PlayerScoreSerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.SlugRelatedField(
        queryset=Player.objects.all(),
        slug_field='name'
    )
    game = serializers.SlugRelatedField(
        queryset=Game.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = PlayerScore
        fields = '__all__'
