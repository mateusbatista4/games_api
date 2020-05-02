from .models import EsrbRating,Game,PlayerScore,Player
from .serializers import EsrbRatingSerializer,GameSerializer,PlayerScoreSerializer,PlayerSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import  reverse


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self,request,*args,**kwargs):
        return Response({
            'players': reverse(PlayerList.name,request=request),
            'esrb-rating': reverse(EsrbRatingList.name,request=request),
            'games':reverse(GameList.name,request=request),
            'scores': reverse(PlayerScoreList.name,request=request)
        })


class EsrbRatingList(generics.ListCreateAPIView):
    queryset = EsrbRating.objects.all()
    serializer_class = EsrbRatingSerializer
    name = 'esrbrating-list'


class EsrbRatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EsrbRating.objects.all()
    serializer_class = EsrbRatingSerializer
    name = 'esrbrating-detail'


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'


class PlayerScoreList(generics.ListCreateAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-list'


class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-detail'

#
#
# @api_view(['GET','POST'])
# def game_collection(request):
#     if request.method == 'GET': #return all objects in database
#         games = Game.objects.all()
#         games_serializer = GameSerializer(games, many=True)
#         return Response(games_serializer.data)
#
#     elif request.method == 'POST': #inserts a object in the database
#         game_serializer = GameSerializer(data=request.data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return Response(game_serializer.data, status=status.HTTP_201_CREATED)
#         return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','POST'])
# def game_detail(request, id):
#     try:
#         game = Game.objects.get(id=id)
#     except Game.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':    #returns a especific object from database
#         game_serializer = GameSerializer(game)
#         return Response(game_serializer.data)
#
#     elif request.method == 'PUT': #alterates a especific object from database
#         game_serializer = GameSerializer(game, data=request.data)
#         if game_serializer.is_valid():
#             game_serializer.save()
#             return Response(game_serializer.data)
#         return Response(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE': #deletes a especific object from database
#         game.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#
#
#
