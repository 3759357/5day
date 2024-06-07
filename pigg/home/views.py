from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def main_feed(request):
    return render(
        request,
        'home/main_feed.html'
    )


def history(request):
    return render(
        request,
        'home/history.html'
    )

def story(request):
    return render(
        request,
        'home/story.html'
    )

def style(request):
    return render(
        request,
        'home/style.html'
    )

def menu(request):
    return render(
        request,
        'home/menu.html'
    )

def restaurant(request):
    return render(
        request,
        'home/restaurant.html'
    )

def franchise_story(request):
    return render(
        request,
        'home/story.html'
    )

def franchise(request):
    return render(
        request,
        'home/franchise.html'
    )

def review(request):
    return render(
        request,
        'home/review.html'
    )

