from django.shortcuts import render
from reccomendationengine.models import RecommendationDatabase
import random

# Create your views here.
def reccomendation_home(request):
    return render(request, "reccomendation_home.html")

def reccomendation_engine(request):
    return render(request, "recommendation_engine.html")
 
def recc1(request):
    # receviing the response of instant or question
    val1= request.GET['answer1']
    if val1 == "1":
        #moved to next part of the quiz (aer you new to anime )
        return render(request, "recommendation_engine_questions.html")
    else: #instantly reccomendation 
        anime_data =list( RecommendationDatabase.objects.filter(Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
        
def recc2(request):
    #receiving the answer to are you new to anime
    val1= request.GET['answer2']
    if val1 == "1":
        #moved to next part of the quiz ( mainstream or not)
        return render(request, "recommendation_engine_questions2.html")
    else: 
        #code to code learding to page when he says he is old
        return render(request, 'recommendation_engine_questions3.html')

def recc3(request):
    # receiving the answer of have you seen mainstream
    val1= request.GET['answer3']
    if val1 == "0":
        #moved to next part not seen then anime shown
        return render(request, "anime_recc_template.html")
    else: 
        #code if they have not seen leading to next page
        return render(request, 'recommendation_engine_questions3.html')

def recc4(request):
    # receiving the answer to before or after 2010
    val1= request.GET['answer4']
    if val1 == "1": #Before 2020
        return render(request, "recc_genre_before_2020.html")
    else: #After 2020 
        #genre will be showed after 2020
        return render(request, 'recc_genre_after_2020.html')

def genre_before_2010(request):
    #received the answer on genre 
    genre = request.GET['answer_before_genre']

    # 1- SLICE OF LIFE
    # 2- Dark and Fantasy
    # 3- ISIKAI
    # 4- SPORTS
    # 5- Comedy 
    # 6- Shonin 

    if  genre =="1": #will have further subcateogries
        return render(request, 'slice_of_life_before_2010.html')
    
    elif genre =="2": #No Sub categories

        anime_data =list( RecommendationDatabase.objects.filter(genre="darkfan", Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        print(anime_data)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})

    elif genre =="3": # Wil have further subcateogies
        return render(request, 'isekai.html', {"age":'isekai_before_2010'})
    elif genre =="4": # Sports No Further Categories

        anime_data =list( RecommendationDatabase.objects.filter(genre="sports", Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})

    elif genre =="5": # Comedy No Further Categories

        anime_data =list( RecommendationDatabase.objects.filter(genre="comedy", Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    
    elif genre =="6": # Will have further subcateogires
        return render(request, 'shonin.html', {"age":'shonin_before_2010'})
    else: # PLEASE VOTE PAGE
        pass
   

def genre_after_2010(request):
    #received the answer on genre 
    genre = request.GET['answer_after_genre']

    # 1- SLICE OF LIFE
    # 2- Dark and Fantasy
    # 3- ISIKAI
    # 4- SPORTS
    # 5- Comedy 
    # 6- Shonin

    if  genre == "1": #will have further subcateogries
         return render(request, 'slice_of_life_after_2010.html')

    elif genre == "2": #No Sub categories
        anime_data =list( RecommendationDatabase.objects.filter(genre="darkfan"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})

    elif genre == "3": # Wil have further subcateogies
        return render(request, 'isekai.html', {"age":'isekai_after_2010'})
    elif genre == "4": # Sports
        anime_data =list( RecommendationDatabase.objects.filter(genre="sports"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    elif genre == "5": # Comedy
        anime_data =list( RecommendationDatabase.objects.filter(genre="comedy"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    elif genre == "6": # Will have further subcateogires
        return render(request, 'shonin.html', {"age":'shonin_after_2010'})
    else: #Please Vote page
        pass    



def sliceoflife_before_2010(request):
    # 1. Tears Jerking 
    # 2. Underrated
    # 3. Classis comedy
    # 4. Adult
    # 5. Radio's Best
    # 6. Must Watch 
    genre_sol = request.GET['answer_sol_genre']

    if genre_sol == "1":
        anime_data =list( RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="tear", Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    
    elif genre_sol == "2":
        anime_data =list( RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="underrated", Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    
    elif genre_sol == "3":
        anime_data =list( RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="comedy", Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})

    elif genre_sol == "4":
        anime_data =list( RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="adult", Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})

    elif genre_sol == "5":
        anime_data =list( RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="radio", Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})

    elif genre_sol == "6":
        anime_data =list( RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="mustwatch", Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    else:
        pass #add you have not selected any answer please select one

def sliceoflife_after_2010(request):
    # 1. Tears Jerking 
    # 2. Underrated
    # 3. Classis comedy
    # 4. Adult
    # 5. Radio's Best
    # 6. Must Watch 
    genre_sol = request.GET['answer_sol_genre']

    
    if genre_sol == "1":
        anime_data =list( RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="tear"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    
    elif genre_sol == "2":
        anime_data =list( RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="underrated"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    
    elif genre_sol == "3":
        anime_data =list( RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="comedy"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})

    elif genre_sol == "4":
        anime_data =list( RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="adult"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})

    elif genre_sol == "5":
        anime_data =list( RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="radio"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})

    elif genre_sol == "6":
        anime_data =list( RecommendationDatabase.objects.filter(genre="sliceoflife", sub_genre="mustwatch"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    else:
        pass #add you have not selected any answer please select one

def isekai_before_2010(request):
    # 1- Underrated
    # 2- Main Stream
    isi_genre = request.GET["answer_isekai_genre"]

    if isi_genre  == "1":
        anime_data =list( RecommendationDatabase.objects.filter(genre="isekai", sub_genre="underrated", Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    else:
        anime_data =list( RecommendationDatabase.objects.filter(genre="isekai", sub_genre="mainstream", Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})

def isekai_after_2010(request):
    # 1- Underrated
    # 2- Main Stream
    isi_genre = request.GET["answer_isekai_genre"]

    if isi_genre  == "1":
        anime_data =list( RecommendationDatabase.objects.filter(genre="isekai", sub_genre="underrated"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    else:
        anime_data =list( RecommendationDatabase.objects.filter(genre="isekai", sub_genre="mainstream"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})


def shonin_after_2010(request):
# 1- NEWGEN
# 2- MainStream
# 3- Others
    shonin_genre = request.GET['answer_shonin_genre']

    if shonin_genre == "1":
        anime_data =list( RecommendationDatabase.objects.filter(genre="shonin", sub_genre="newgen", Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    elif shonin_genre == "2":
        anime_data =list( RecommendationDatabase.objects.filter(genre="shonin", sub_genre="mainstream")
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    else:
        anime_data =list( RecommendationDatabase.objects.filter(genre="shonin", sub_genre="other",  Year2010=True))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})



def shonin_before_2010(request):
    shonin_genre = request.GET['answer_shonin_genre']

    
    if shonin_genre == "1":
        anime_data =list( RecommendationDatabase.objects.filter(genre="shonin", sub_genre="newgen"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    elif shonin_genre == "2":
        anime_data =list( RecommendationDatabase.objects.filter(genre="shonin", sub_genre="mainstream"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
    else:
        anime_data =list( RecommendationDatabase.objects.filter(genre="shonin", sub_genre="other"))
        anime = random.choice(anime_data)
        anime_list = random.sample(anime_data, 3)
        return render(request, 'anime_recc_template.html', {"anime":anime, "anime_list":anime_list})
   
