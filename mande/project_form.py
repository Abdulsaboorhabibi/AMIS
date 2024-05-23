from django import forms
from . import models

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ('title', 'sector', 'donor', 'location', 'end_date', 'idp', 'idp_returnee',
        'refugee', 'host', 'kochi', 'male', 'female', 'childern', 'childern_age_from', 'childern_age_end',
        'plw', 'pwd', 'overall_Status', 'remarks')

        widgets = {
            'title': forms.TextInput(attrs={'class':"bg-gray-50 text-md font-semibold border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "}),
            'sector': forms.Select(attrs={'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "}),
            'donor': forms.Select(attrs={'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "}),
            'location': forms.Select(attrs={'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "}),
            'end_date': forms.DateTimeInput(attrs={'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 "}),
            'idp': forms.CheckboxInput(attrs={'class':"w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 "}),
            'idp_returnee': forms.CheckboxInput(attrs={'class':"w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 "}),
            'refugee': forms.CheckboxInput(attrs={'class':"w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 "}),
            'host': forms.CheckboxInput(attrs={'class':"w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 "}),
            'kochi': forms.CheckboxInput(attrs={'class':"w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 "}),
            'male': forms.CheckboxInput(attrs={'class':"w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 "}),
            'female': forms.CheckboxInput(attrs={'class':"w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 "}),
            'plw': forms.CheckboxInput(attrs={'class':"w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 "}),
            'pwd': forms.CheckboxInput(attrs={'class':"w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 "}),
            'childern': forms.CheckboxInput(attrs={'class':"w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 "}),
            'childern_age_from': forms.NumberInput(attrs={'class':"bg-gray-50 text-md font-semibold border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"}),
            'childern_age_end': forms.NumberInput(attrs={'class':"bg-gray-50 text-md font-semibold border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"}),
            'overall_Status': forms.Select(attrs={'class':"bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"}),
            'remarks': forms.Textarea(attrs={'class':"block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 "}),
        }