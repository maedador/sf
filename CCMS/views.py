from multiprocessing import context
from django.shortcuts import render

def Mission(request):
    context = {
        'head': 'Mission',
        'Mission': "The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) \
        industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence."

     }
    return render(request, 'CCMSMVG.html', context)

def Vision(request):
    context = {
        'head': 'Vision',
        'Vision': "The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education."

    }
    return render(request, 'CCMSMVG.html', context)

def Goal(request):
    context = {
        'head' : 'Goal',
        'Goal': 'CCMS Program Educational Objectives After graduation, alumni of MSEUF-CCMS programs shall:', 
        'one' : '1. Be employed and demonstrate professionalism, competence and passion in solving contemporary computing problems by developing or utilizing innovative IT solutions;',
        'two' : '2. Embark in lifelong learning or research to attune to the continuous innovation in the IT industry in order to adapt to the changing demands of the global market: and', 
        'three' : '3. Exhibit leadership and teamwork, and commitment to their respective local or global organizations.'

    }
    return render(request, 'CCMSMVG.html', context)



