from django import forms
from recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = 'category', 'title', 'image', 'short_description', 'content'
        labels = {
            'category': 'Category',
            'title': 'Title',
            'image': 'Image',
            'short_description': 'Short Description',
            'content': 'Description',
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'select select-bordered w-full max-w-xs'}),
            'title': forms.TextInput(attrs={
                'class': 'peer h-full shadow-lg w-full rounded-[7px] border bg-transparent px-3 py-2.5 pr-20 font-sans text-sm font-normal text-orange-500 outline outline-0 placeholder-shown:border focus:border-2 focus:border-orange-500 focus:outline-0'}),
            'image': forms.FileInput(attrs={
                'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'}),
            'short_description': forms.TextInput(attrs={
                'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs[
            'oninput'] = 'titlePreview(this)'
        self.fields['title'].widget.attrs[
            'required'] = ''

        self.fields['image'].widget.attrs[
            'required'] = ''

        self.fields['short_description'].widget.attrs[
            'oninput'] = 'descPreview(this)'
        self.fields['short_description'].widget.attrs[
            'required'] = ''

