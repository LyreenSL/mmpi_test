from django.shortcuts import render, get_object_or_404
from django.views import View
from uuid import uuid1
from .models import *


class MaleTest(View):
    def get(self, request):
        request.session['sex'] = 'male'
        return render(request, 'mmpi/test.html', {'questions': MaleQuestion.objects.all(), 'uuid': uuid1()})


class FemaleTest(View):
    def get(self, request):
        request.session['sex'] = 'female'
        return render(request, 'mmpi/test.html', {'questions': FemaleQuestion.objects.all(), 'uuid': uuid1()})


class Results(View):

    def get(self, request, pk):
        try:
            results = get_object_or_404(ResultsData, id=pk).results
        except:
            return render(request, 'mmpi/results.html', context={'error': 'yes'})
        else:
            return render(request, 'mmpi/results.html',
                          context={'keys': list(results.keys()), 'values': list(results.values())})

    def post(self, request, pk):
        results = {'L': 0, 'F': 0, 'K': 0, '1': 0, '2': 0, '3': 0, '4': 0,
                   '5(M)' if request.session['sex'] == 'male' else '5(F)': 0,
                   '6': 0, '7': 0, '8': 0, '9': 0, '0': 0}

        def calculate_raw_scores(key):
            scale = AverageData.objects.get(scale=key)
            yes = list(map(int, scale.yes.split(', ')))
            no = list(map(int, scale.no.split(', ')))

            for i in range(1, 567):
                if (i in yes and request.POST[f'answer{i}'] == 'yes') or (
                        i in no and request.POST[f'answer{i}'] == 'no'):
                    results[key] += 1

        def calculate_correction():
            results['9'] += results['K'] * 0.2
            results['4'] += results['K'] * 0.4
            results['1'] += results['K'] * 0.5
            results['7'] += results['K'] * 1
            results['8'] += results['K'] * 1

        def calculate_t_scores(key):
            scale = AverageData.objects.get(scale=key)
            if request.session['sex'] == 'male':
                results[key] = round(50 + 10 * (results[key] - scale.m_male) / scale.sigma_male, 1)
            else:
                results[key] = round(50 + 10 * (results[key] - scale.m_female) / scale.sigma_female, 1)

        for key in results.keys():
            calculate_raw_scores(key)

        calculate_correction()

        for key in results.keys():
            calculate_t_scores(key)

        ResultsData(id=pk, results=results).save()

        return render(request, 'mmpi/results.html',
                      context={'keys': list(results.keys()), 'values': list(results.values())})
