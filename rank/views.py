from rank.models import Rank, ScoreSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def rank_view(request, **kwargs):
    score_str = kwargs['score']
    score = int(score_str)
    rank = Rank(score=score)
    rank.save()

    behind = Rank.objects.filter(score__lt=score).count()
    total = Rank.objects.count()
    percetange = behind * 100.0 / total

    rank = "{0:.2f}".format(round(percetange, 2)) + "%"
    return JsonResponse({'rank': rank})
