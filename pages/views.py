from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from pages.models import List2018, Votes, List2019, List2020
from django.db.models import F
from django.contrib import messages


# Create your views here.
def home(request):
    return render(
        request,
        'index.html',
        {
            "page_title": "The Anime Radio | Anime Recommendations, Lists, and Polls",
            "page_description": "Discover anime with recommendation quizzes, ranked seasonal lists, and community polls from The Anime Radio.",
        },
    )


def _handle_vote(request, model, queryset, template_name, context_name):
    if request.method != "POST":
        return render(request, template_name, {context_name: queryset})

    if not request.user.is_authenticated:
        messages.info(request, "Login or register to vote.")
        return render(request, template_name, {context_name: queryset})

    up_vote = request.POST.get('up_votes')
    down_vote = request.POST.get('down_votes')
    anime_name = up_vote or down_vote

    if not anime_name:
        messages.info(request, "Please choose an anime before voting.")
        return render(request, template_name, {context_name: queryset})

    anime = get_object_or_404(model, name=anime_name)

    if Votes.objects.filter(user_id=request.user.id, anime_id=anime.anime_id).exists():
        messages.info(request, "You have already voted for this anime.")
        return render(request, template_name, {context_name: queryset})

    Votes.objects.create(anime_id=anime.anime_id, user_id=request.user.id)

    if up_vote:
        model.objects.filter(pk=anime.pk).update(up_votes=F("up_votes") + 1)
        messages.info(request, f"You upvoted {anime_name}.")
    else:
        model.objects.filter(pk=anime.pk).update(down_votes=F("down_votes") + 1)
        messages.info(request, f"You downvoted {anime_name}.")

    return render(request, template_name, {context_name: queryset})

#LIST PAGE 2018
def list2018(request):
    list1 = List2018.objects.all().order_by("-up_votes", "name")
    return _handle_vote(request, List2018, list1, 'list2018.html', 'list_2018')


def list2019(request):
    list1 = List2019.objects.all().order_by("-up_votes", "name")
    return _handle_vote(request, List2019, list1, 'list2019.html', 'list_2019')


def summer2020(request):
    list1 = List2020.objects.filter(season="summer").order_by("-up_votes", "name")
    return _handle_vote(request, List2020, list1, 'summer2020.html', 'summer2020')

def winter2020(request):
    list1 = List2020.objects.filter(season="winter").order_by("-up_votes", "name")
    return _handle_vote(request, List2020, list1, 'winter2020.html', 'winter2020')



def spring2020(request):
    list1 = List2020.objects.filter(season="spring").order_by("-up_votes", "name")
    return _handle_vote(request, List2020, list1, 'spring2020.html', 'spring2020')
        
def sitemap(request):
    return render(request, 'sitemap.xml', content_type="application/xml")


def robots_txt(request):
    return render(request, 'robots.txt', content_type="text/plain")
