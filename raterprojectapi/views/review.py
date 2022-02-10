from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.serializers import ModelSerializer
from raterprojectapi.models.game import Game
from raterprojectapi.models.gamer import Gamer
from raterprojectapi.models.review import Review


class ReviewView(ViewSet):
    def list(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def create(self, request):
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data['game'])

        review = Review.objects.create(
            review=request.data['review'],
            gamer=gamer,
            game=game
        )
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        review=Review.objects.get(pk=pk)
        review.review = request.data['review']
        review.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        review = Review.get(pk=pk)
        review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        depth = 1
