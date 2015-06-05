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
    ahead = Rank.objects.filter(score__gt=score).count()
    total = Rank.objects.count()

    percetange = behind * 100.0 / total
    rank = "{0:.2f}".format(round(percetange, 2)) + "%"

    """
    Though score less the new score, but since there is no score
    greater than the new score, so the new score beat everyone
    """
    if ahead == 0:
        rank = "100%"


    return JsonResponse({'rank': rank})

@api_view(['GET'])
def score_view(request, **kwargs):
    ranks = Rank.objects.order_by('-score')

    score_list = []

    for r in ranks:
        score_list.append(r.score)

    return JsonResponse({'scores': score_list})
