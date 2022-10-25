from django.shortcuts import render, redirect

from examprep2.gamesplay.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from examprep2.gamesplay.models import Profile, Game


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True

    context = {
        'has_profile': has_profile
    }
    return render(request, 'home-page.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form
    }

    return render(request, 'create-profile.html', context)


def dashboard(request):
    games = Game.objects.all()
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    context = {
        'games': games,
        'has_profile': has_profile
    }

    return render(request, 'dashboard.html', context)



def create_game(request):
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'create-game.html', context)

def details_game(request, pk):
    game = Game.objects.filter(pk=pk).get()

    context = {
        'game': game
    }

    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameCreateForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game
    }

    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game
    }

    return render(request, 'delete-game.html', context)


def details_profile(request):
    games_count = Game.objects.count()
    profile = get_profile()
    rating = 0
    if games_count > 0:
        games = Game.objects.all()
        for game in games:
            rating += game.rating
        rating = rating / games_count


    context = {
        'profile': profile,
        'games_count': games_count,
        'rating': rating,
    }

    return render(request, 'details-profile.html', context)

def edit_profile(request):
    profile = get_profile()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,

    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'delete-profile.html',
        context,
    )