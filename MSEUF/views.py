from multiprocessing import context
from django.shortcuts import render

def Mission(request):
    context = {
        'head': 'Mission',
        'Mission': "The University is a private non-stock non-profit non-sectarian educational foundation with a three-fold function - instruction, research, and community service - offering \
        responsive and alternative programs supportive of national development and standards of global excellence."

     }
    return render(request, 'MVG.html', context)

def Vision(request):
    context = {
    'head': 'Vision',
        'Vision': "In 2030, the Manuel S. Enverga University Foundation is a globally competitive university with high concentrations of talent, \
        excellent teaching environment, rigorous program quality, sufficient resources, and a culture of collaboration."

    }
    return render(request, 'MVG.html', context)

def Goal(request):
    context = {
         'head' : 'Goal',
        'Goal': "MSEUF shall produce graduates who have research-based knowledge, leadership and management skills, and professionalism."

    }
    return render(request, 'MVG.html', context)



