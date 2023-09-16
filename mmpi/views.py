from django.shortcuts import render, get_object_or_404
from django.views import View
from uuid import uuid1
from .models import *
import json


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
            results = get_object_or_404(ResultsData, id=pk)
            main_scales = results.main_scales
            additional_scales = results.additional_scales
        except:
            return render(request, 'mmpi/results.html', context={'error': True})
        else:
            return render(request, 'mmpi/results.html',
                          context={'values': list(main_scales.values()), 'keys': list(main_scales.keys()),
                                   'add_scales': additional_scales.items(), 'uuid': pk, 'clearLS': 'true'})

    def post(self, request, pk):

        def raw_score_calculation(datas):
            results = {}
            for data in datas:
                results |= {data.scale: 0}
                for i in range(1, 567):
                    if (i in data.yes and request.POST[f'answer{i}'] == 'yes') or (
                            i in data.no and request.POST[f'answer{i}'] == 'no'):
                        results[data.scale] += 1
            return results

        def t_score_calculation(results):
            for key in results.keys():
                scale = AverageData.objects.get(scale=key)
                if request.session['sex'] == 'male':
                    results[key] = round(50 + 10 * (results[key] - scale.m_male) / scale.sigma_male, 1)
                else:
                    results[key] = round(50 + 10 * (results[key] - scale.m_female) / scale.sigma_female, 1)

        main_scales = raw_score_calculation(AverageData.objects.filter(id__lte=14))
        additional_scales = raw_score_calculation(AverageData.objects.filter(id__gt=14))

        main_scales['9'] += main_scales['K'] * 0.2
        main_scales['4'] += main_scales['K'] * 0.4
        main_scales['1'] += main_scales['K'] * 0.5
        main_scales['7'] += main_scales['K'] * 1
        main_scales['8'] += main_scales['K'] * 1

        if request.session['sex'] == 'male':
            main_scales.pop('5(Ж)')
            additional_scales.pop('Ригидность (женская)')
            additional_scales.pop('Стабильность профиля (женская)')
        elif request.session['sex'] == 'female':
            main_scales.pop('5(М)')
            additional_scales.pop('Ригидность (мужская)')
            additional_scales.pop('Стабильность профиля (мужская)')

        t_score_calculation(main_scales)
        t_score_calculation(additional_scales)

        ResultsData(id=pk, main_scales=main_scales, additional_scales=additional_scales).save()

        return render(request, 'mmpi/results.html',
                      context={'values': list(main_scales.values()), 'keys': list(main_scales.keys()),
                               'add_scales': additional_scales.items(), 'uuid': pk, 'clearLS': 'true'})
