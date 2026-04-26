from django.shortcuts import render
from reccomendationengine.models import RecommendationDatabase
from django.contrib import messages
import random

# Create your views here.
def reccomendation_home(request):
    return render(
        request,
        "reccomendation_home.html",
        {
            "page_title": "Anime Recommendation Quiz | The Anime Radio",
            "page_description": "Answer a short anime quiz and get a personalized anime recommendation from The Anime Radio.",
        },
    )

def reccomendation_engine(request):
    return render(
        request,
        "recommendation_engine.html",
        {
            "page_title": "Start the Anime Recommendation Quiz | The Anime Radio",
            "page_description": "Find an anime to watch next by answering a few quick genre and experience questions.",
        },
    )


def _choice(request, name):
    value = request.GET.get(name)
    if value is None:
        messages.info(request, "Please choose an answer to continue.")
    return value


def _recommend(request, queryset):
    anime_data = list(queryset)
    if not anime_data:
        messages.info(request, "No recommendations match that path yet. Try another set of answers.")
        return render(request, "recommendation_engine.html")

    anime = random.choice(anime_data)
    sample_size = min(3, len(anime_data))
    anime_list = random.sample(anime_data, sample_size)
    return render(
        request,
        'anime_recc_template.html',
        {
            "anime": anime,
            "anime_list": anime_list,
            "page_title": f"{anime.name} Anime Recommendation | The Anime Radio",
            "page_description": anime.summary[:155],
        },
    )
 
def recc1(request):
    # receviing the response of instant or question
    val1 = _choice(request, 'answer1')
    if val1 is None:
        return reccomendation_engine(request)
    if val1 == "1":
        #moved to next part of the quiz (aer you new to anime )
        return render(request, "recommendation_engine_questions.html")
    else: #instantly reccomendation 
        return _recommend(request, RecommendationDatabase.objects.filter(Year2010=True))
        
def recc2(request):
    #receiving the answer to are you new to anime
    val1 = _choice(request, 'answer2')
    if val1 is None:
        return render(request, "recommendation_engine_questions.html")
    if val1 == "1":
        #moved to next part of the quiz ( mainstream or not)
        return render(request, "recommendation_engine_questions2.html")
    else: 
        #code to code learding to page when he says he is old
        return render(request, 'recommendation_engine_questions3.html')

def recc3(request):
    # receiving the answer of have you seen mainstream
    val1 = _choice(request, 'answer3')
    if val1 is None:
        return render(request, "recommendation_engine_questions2.html")
    if val1 == "0":
        #moved to next part not seen then anime shown
        return _recommend(request, RecommendationDatabase.objects.filter(genre="mainstream"))
    else: 
        #code if they have not seen leading to next page
        return render(request, 'recommendation_engine_questions3.html')

def recc4(request):
    # receiving the answer to before or after 2010
    val1 = _choice(request, 'answer4')
    if val1 is None:
        return render(request, 'recommendation_engine_questions3.html')
    if val1 == "1": #Before 2020
        return render(request, "recc_genre_before_2020.html")
    else: #After 2020 
        #genre will be showed after 2020
        return render(request, 'recc_genre_after_2020.html')

def genre_before_2010(request):
    #received the answer on genre 
    genre = _choice(request, 'answer_before_genre')
    if genre is None:
        return render(request, "recc_genre_before_2020.html")

    # 1- SLICE OF LIFE
    # 2- Dark and Fantasy
    # 3- ISIKAI
    # 4- SPORTS
    # 5- Comedy 
    # 6- Shonin 

    if  genre =="1": #will have further subcateogries
        return render(request, 'slice_of_life_before_2010.html')
    
    elif genre =="2": #No Sub categories

        return _recommend(request, RecommendationDatabase.objects.filter(genre="darkfan", Year2010=True))

    elif genre =="3": # Wil have further subcateogies
        return render(request, 'isekai.html', {"age":'isekai_before_2010'})
    elif genre =="4": # Sports No Further Categories

        return _recommend(request, RecommendationDatabase.objects.filter(genre="sports", Year2010=True))

    elif genre =="5": # Comedy No Further Categories

        return _recommend(request, RecommendationDatabase.objects.filter(genre="comedy", Year2010=True))
    
    elif genre =="6": # Will have further subcateogires
        return render(request, 'shonin.html', {"age":'shonin_before_2010'})
    else: # PLEASE VOTE PAGE
        messages.info(request, "Please choose a genre.")
        return render(request, "recc_genre_before_2020.html")
   

def genre_after_2010(request):
    #received the answer on genre 
    genre = _choice(request, 'answer_after_genre')
    if genre is None:
        return render(request, "recc_genre_after_2020.html")

    # 1- SLICE OF LIFE
    # 2- Dark and Fantasy
    # 3- ISIKAI
    # 4- SPORTS
    # 5- Comedy 
    # 6- Shonin

    if  genre == "1": #will have further subcateogries
         return render(request, 'slice_of_life_after_2010.html')

    elif genre == "2": #No Sub categories
        return _recommend(request, RecommendationDatabase.objects.filter(genre="darkfan"))

    elif genre == "3": # Wil have further subcateogies
        return render(request, 'isekai.html', {"age":'isekai_after_2010'})
    elif genre == "4": # Sports
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sports"))
    elif genre == "5": # Comedy
        return _recommend(request, RecommendationDatabase.objects.filter(genre="comedy"))
    elif genre == "6": # Will have further subcateogires
        return render(request, 'shonin.html', {"age":'shonin_after_2010'})
    else: #Please Vote page
        messages.info(request, "Please choose a genre.")
        return render(request, "recc_genre_after_2020.html")



def sliceoflife_before_2010(request):
    # 1. Tears Jerking 
    # 2. Underrated
    # 3. Classis comedy
    # 4. Adult
    # 5. Radio's Best
    # 6. Must Watch 
    genre_sol = _choice(request, 'answer_sol_genre')
    if genre_sol is None:
        return render(request, 'slice_of_life_before_2010.html')

    if genre_sol == "1":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="tear", Year2010=True))
    
    elif genre_sol == "2":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="underrated", Year2010=True))
    
    elif genre_sol == "3":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="comedy", Year2010=True))

    elif genre_sol == "4":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="adult", Year2010=True))

    elif genre_sol == "5":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="radio", Year2010=True))

    elif genre_sol == "6":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="mustwatch", Year2010=True))
    else:
        messages.info(request, "Please choose a slice-of-life category.")
        return render(request, 'slice_of_life_before_2010.html')

def sliceoflife_after_2010(request):
    # 1. Tears Jerking 
    # 2. Underrated
    # 3. Classis comedy
    # 4. Adult
    # 5. Radio's Best
    # 6. Must Watch 
    genre_sol = _choice(request, 'answer_sol_genre')
    if genre_sol is None:
        return render(request, 'slice_of_life_after_2010.html')

    
    if genre_sol == "1":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="tear"))
    
    elif genre_sol == "2":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="underrated"))
    
    elif genre_sol == "3":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="comedy"))

    elif genre_sol == "4":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="adult"))

    elif genre_sol == "5":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="radio"))

    elif genre_sol == "6":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="mustwatch"))
    else:
        messages.info(request, "Please choose a slice-of-life category.")
        return render(request, 'slice_of_life_after_2010.html')

def isekai_before_2010(request):
    # 1- Underrated
    # 2- Main Stream
    isi_genre = _choice(request, "answer_isekai_genre")
    if isi_genre is None:
        return render(request, 'isekai.html', {"age": 'isekai_before_2010'})

    if isi_genre  == "1":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="isekai", sub_genre="underrated", Year2010=True))
    else:
        return _recommend(request, RecommendationDatabase.objects.filter(genre="isekai", sub_genre="mainstream", Year2010=True))

def isekai_after_2010(request):
    # 1- Underrated
    # 2- Main Stream
    isi_genre = _choice(request, "answer_isekai_genre")
    if isi_genre is None:
        return render(request, 'isekai.html', {"age": 'isekai_after_2010'})

    if isi_genre  == "1":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="isekai", sub_genre="underrated"))
    else:
        return _recommend(request, RecommendationDatabase.objects.filter(genre="isekai", sub_genre="mainstream"))


def shonin_after_2010(request):
# 1- NEWGEN
# 2- MainStream
# 3- Others
    shonin_genre = _choice(request, 'answer_shonin_genre')
    if shonin_genre is None:
        return render(request, 'shonin.html', {"age": 'shonin_after_2010'})

    if shonin_genre == "1":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="shonin", sub_genre="newgen", Year2010=True))
    elif shonin_genre == "2":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="shonin", sub_genre="mainstream"))
    else:
        return _recommend(request, RecommendationDatabase.objects.filter(genre="shonin", sub_genre="other",  Year2010=True))



def shonin_before_2010(request):
    shonin_genre = _choice(request, 'answer_shonin_genre')
    if shonin_genre is None:
        return render(request, 'shonin.html', {"age": 'shonin_before_2010'})

    
    if shonin_genre == "1":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="shonin", sub_genre="newgen"))
    elif shonin_genre == "2":
        return _recommend(request, RecommendationDatabase.objects.filter(genre="shonin", sub_genre="mainstream"))
    else:
        return _recommend(request, RecommendationDatabase.objects.filter(genre="shonin", sub_genre="other"))
   
