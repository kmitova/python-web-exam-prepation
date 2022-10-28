from django import forms

from examprep5.recipes_app.models import Recipe


class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'time': 'Time (Minutes)'
        }



class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'time': 'Time (Minutes)'
        }


class RecipeDeleteForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            # field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disabled'] = 'disabled'