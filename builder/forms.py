from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import FileUpload
from crispy_forms.layout import Layout, Fieldset
from crispy_tailwind.layout import Button, Submit
from crispy_forms.helper import FormHelper

class ResumeUploadForm(forms.ModelForm):
    # form used on homepage for fetching file upload data
    class Meta:
        model = FileUpload
        fields = "__all__"