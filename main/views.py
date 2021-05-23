from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView
from docx2python import docx2python

from profanity_filter import ProfanityFilter
import en_core_web_sm

from .models import Words



# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        nlp = en_core_web_sm.load()
        pf = ProfanityFilter(nlps={'en': nlp})
        # pf.custom_profane_word_dictionaries = {'en': {'sold down the river', 'dog'}}
        # pf.extra_profane_word_dictionaries = {'en': {'sold', 'orange'}}
        wordlist = []
        context = {}

        # FILE UPLOADED
        if 'doc' in request.FILES:
            doc = docx2python(request.FILES['doc'], extract_image=False)
            context['doc'] = doc.text

            return render(request, 'index.html', context=context)

        # RETRIEVE WORDS AND SPLIT
        document = request.POST['document']
        word_lines = document.splitlines()
        

        # CHECK EACH WORD IF PROFANITY
        for line in word_lines:
            if line == '':
                wordlist.append(r'\n')

            # NO LINE BREAK CONTINUE HERE
            else:
                words = line.split()
                temp_list = []

                for word in words:
                    in_db = Words.objects.all().filter(word__icontains=word)

                    if pf._is_profane_word('en', word) or not in_db:
                        temp_word = " ".join(temp_list)
                        completed = Words.objects.all().filter(word__iexact=temp_word)

                        if completed:
                            new_word = "*" + temp_word + "*"
                            wordlist.append(new_word)
                            temp_list.clear()
                        else:
                            wordlist.append(temp_word)
                            temp_list.clear()

                        if pf._is_profane_word('en', word):
                            new_word = "*" + word + "*"
                            wordlist.append(new_word)
                        else:
                            wordlist.append(word)
                    else:
                        temp_list.append(word)
                
                if len(temp_list) > 0:
                    temp_word = " ".join(temp_list)
                    completed = Words.objects.all().filter(word__iexact=temp_word)

                    if completed:
                            new_word = "*" + temp_word + "*"
                            wordlist.append(new_word)
                            temp_list.clear()
                    else:
                        wordlist.append(temp_word)
                        temp_list.clear()



        
        context["results"] = " ".join(wordlist)
        context['document'] = document

        return render(request, 'index.html', context=context)
