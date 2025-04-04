from django import forms
from .models import ModelAuto

class ModelAutoForm(forms.ModelForm):
    class Meta:
        model = ModelAuto
        fields = ('marka', 'naimenovanie', 'kuzov', 'izobrazhenie', 'photoosobennosti', 'photo1', 'photo2', 'photo3', 'clirens', 'kolesa', 'toplivo', 'korobkaperedach', 'privod', 'osobennosti', 'price', 'opisanie', 'shirina', 'visota', 'dlina', 'stepensjatiya', 'mochnost', 'obembaka')
        labels = {'marka': 'Марка', 'naimenovanie':'Наименование', 'kuzov':'Кузов', 'izobrazhenie':'Изображение', 'photoosobennosti' : 'Фото особенности', 'photo1'  : 'Фото-Лента 1', 'photo2' : 'Фото-Лента 2', 'photo3' : 'Фото-Лента 3', 'clirens' : 'Клиренс', 'kolesa' : 'Колеса', 'toplivo' : 'Тип топлива', 'korobkaperedach' : 'Тип коробки передач', 'privod' : 'Тип привода', 'osobennosti' : 'Особенности', 'price' : 'Стоимость', 'opisanie' : 'Описание', 'shirina' : 'Ширина', 'visota' : 'Высота', 'dlina' : 'Длина', 'stepensjatiya' : 'Степень сжатия', 'mochnost' : 'Мощность двигателя', 'obembaka' : 'Объем топливного бака'}
        widgets = {'marka': forms.Select(attrs={'class': 'form-select'}),
                    'naimenovanie': forms.TextInput(attrs={'class': 'form-control', 'rows':1, 'cols':1}),
                    'kuzov': forms.Select(attrs={'class': 'form-select'}),
                    'izobrazhenie': forms.FileInput(attrs={'class': 'form-control'}),
                    'photoosobennosti': forms.FileInput(attrs={'class': 'form-control'}),
                    'photo1': forms.FileInput(attrs={'class': 'form-control'}),
                    'photo2': forms.FileInput(attrs={'class': 'form-control'}),
                    'photo3': forms.FileInput(attrs={'class': 'form-control'}),
                    'clirens': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols':1}),
                    'kolesa': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols':1}),
                    'toplivo': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols':1}),
                    'korobkaperedach': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols':1}),
                    'privod': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols':1}),
                    'osobennosti': forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'cols':1}),
                    'price': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols':1}),
                    'opisanie': forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'cols':1}),
                    'shirina': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols':1}),
                    'visota': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols':1}),
                    'dlina': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols':1}),
                    'stepensjatiya': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols':1}),
                    'mochnost': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols':1}),
                    'obembaka': forms.Textarea(attrs={'class': 'form-control', 'rows':1, 'cols':1}),}