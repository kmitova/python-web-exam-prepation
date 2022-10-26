from django.shortcuts import render, redirect

from examprep3.library.forms import ProfileCreateForm, BookCreateForm, BookEditForm, ProfileEditForm, ProfileDeleteForm

from examprep3.library.models import Profile, Book


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def add_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'hide_nav_links': True,
    }

    return render(
        request,
        'home-no-profile.html',
        context,
    )

def index(request):
    profile = get_profile()
    if profile is None:
        return add_profile(request)

    context = {
        'books': Book.objects.all(),
        'profile': profile,
    }

    return render(
        request,
        'home-with-profile.html',
        context,

    )


def add_book(request):
    if request.method == 'GET':
        form = BookCreateForm()
    else:
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': get_profile()
    }

    return render(request, 'add-book.html', context)


def edit_book(request, pk):
        book = Book.objects.filter(pk=pk).get()
        if request.method == 'GET':
            form = BookEditForm(instance=book)
        else:
            form = BookEditForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect('index')

        context = {
            'form': form,
            'book': book,
            'profile': get_profile()
        }

        return render(request, 'edit-book.html', context)


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()
    return redirect('index')


def details_book(request, pk):
    book = Book.objects.filter(pk=pk).get()

    context = {
        'book': book,
        'profile': get_profile()
    }

    return render(request, 'book-details.html', context)


def profile_page(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == "GET":
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')

    context = {
        'form': form,
        'profile': profile,

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
        'profile': profile
    }

    return render(
        request,
        'delete-profile.html',
        context,
    )

