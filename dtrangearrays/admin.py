from django import forms
from django.contrib import admin
from django.contrib.postgres.forms import SimpleArrayField, DateTimeRangeField
from .models import DateTimeRangeArray


class DateTimeRangeArrayForm(forms.ModelForm):

    durations = SimpleArrayField(
        DateTimeRangeField(
        ),
    )


    class Meta:
        model = DateTimeRangeArray
        fields = '__all__'


class DateTimeRangeArrayAdmin(admin.ModelAdmin):
    form = DateTimeRangeArrayForm


admin.site.register(DateTimeRangeArray, DateTimeRangeArrayAdmin)