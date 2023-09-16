from django.contrib import admin
from .models import *


class MaleQuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    search_fields = ['id', 'text']


class FemaleQuestionAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    search_fields = ['id', 'text']


class AverageDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'scale', 'yes', 'no', 'm_male', 'sigma_male', 'm_female', 'sigma_female']


class ResultsDataAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(MaleQuestion, MaleQuestionAdmin)
admin.site.register(FemaleQuestion, FemaleQuestionAdmin)
admin.site.register(AverageData, AverageDataAdmin)
admin.site.register(ResultsData, ResultsDataAdmin)
