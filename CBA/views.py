from multiprocessing import context
from django.shortcuts import render

def Mission(request):
    context = {
    'head': 'Mission',
        'Mission': "The MSEUF College of Business and Accountancy shall produce professional accountants and business leaders who adequately\
        prepared in the practice of their profession supportive of national development goals and standards of global Excellence."

     }
    return render(request, 'CBAMVG.html', context)

def Vision(request):
    context = {
    'head': 'Vision',
        'Vision': "The MSEUF College of Business and Accountancy shall be a competitive accounting and business educational institution."

    }
    return render(request, 'CBAMVG.html', context)

def Goal(request):
    context = {
    'head' : 'Goal',
        'Goal': '1. The College of Business and Accountancy provides the student with:', 
         'one' : '2. A common foundation of knowledge and understanding concerning modern business through a balanced program of general education and professional business education; ',
         'two' : '3. A sufficient exposure to relate academic instruction to relate academic instruction to the realities of the business world;', 
         'three' : '4. Adequate training to make graduates immediately employable and/ or engage in their entrepreneurship or self-employment;.',
         'four'  : '5. Proper environment for professional growth through high level of professionalism and productive scholarship through research oriented activities; and',
         'five'  : '6. Proper motivation to commit themselves to meaningful and dynamic participation in the national and regional goals.',

    }
    return render(request, 'CBAMVG.html', context)



