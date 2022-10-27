from django import forms

from examprep4.notesapp.models import Profile, Note


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={'placeholder': 'First Name'}
        #     ),
        #     'last_name': forms.TextInput(
        #         attrs={'placeholder': 'Last Name'}
        #     ),
        #     'image_url': forms.URLInput(
        #         attrs={'placeholder': 'URL'}
        #     ),
        #
        # }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass

class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            Note.objects \
                .all() \
                .delete()
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class NoteBaseForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={'placeholder': 'Title'}
        #     ),
        #     'description': forms.Textarea(
        #         attrs={'placeholder': 'Description'}
        #     ),
        #     'image': forms.URLInput(
        #         attrs={'placeholder': 'Image'}
        #     ),
        #     'type': forms.TextInput(
        #         attrs={'placeholder': 'Fiction, Novel, Crime...'}
        #     ),
        #
        # }


class NoteCreateForm(NoteBaseForm):
    pass


class NoteEditForm(NoteBaseForm):
    pass


class NoteDeleteForm(NoteBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'