from django.shortcuts import render, redirect

from examprep4.notesapp.forms import ProfileCreateForm, NoteCreateForm, NoteEditForm, NoteDeleteForm, ProfileDeleteForm
from examprep4.notesapp.models import Note, Profile


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
        'notes': Note.objects.all(),
        'profile': profile,
    }

    return render(
        request,
        'home-with-profile.html',
        context,

    )


def add_note(request):
    if request.method == 'GET':
        form = NoteCreateForm()
    else:
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': get_profile()
    }

    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = NoteEditForm(instance=note)
    else:
        form = NoteEditForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note,
        'profile': get_profile()
    }

    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = NoteDeleteForm(instance=note)
    else:
        form = NoteDeleteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'note': note,
        'profile': get_profile()
    }

    return render(request, 'note-delete.html', context)

def details_note(request, pk):
    note = Note.objects.filter(pk=pk).get()

    context = {
        'note': note,
        'profile': get_profile()
    }

    return render(request, 'note-details.html', context)

# def delete_note(request, pk):
#     note = Note.objects.filter(pk=pk).get()
#     note.delete()
#     return redirect('index')


def profile_page(request):
    notes_count = Note.objects.count()
    profile = get_profile()
    context = {
        'profile': profile,
        'notes_count': notes_count
    }
    return render(request, 'profile.html', context)

def delete_profile(request):
    profile = get_profile()
    notes = Note.objects.all()
    profile.delete()
    notes.delete()
    return redirect('index')