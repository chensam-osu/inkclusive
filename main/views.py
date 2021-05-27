from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView,View
from docx2python import docx2python

from profanity_filter import ProfanityFilter
import en_core_web_sm

from .models import Words

def clear_punctuation(word):

    punctuation= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for letter in word: 

        if letter in punctuation: 
            word = word.replace(letter, "") 
    
    return word

def format_word(word):

    punctuation_list = ('!','(',')','-','[',']','{','}',';',':',"'",'"','\\',',','<','>','.','/','?','@','#','$','%','^','&','*','_','~')

    new_word = ""

    if word.startswith(punctuation_list) or word.endswith(punctuation_list):

        for punctuation in punctuation_list:

            if word.startswith(punctuation):
                word = word.replace(punctuation, f"{punctuation}*")
                new_word += word + "*"

            elif word.endswith(punctuation):
                new_word += "*"
                word = word.replace(punctuation, f"*{punctuation}")

                new_word += word

    else:
        new_word += "*" + word + "*"

    return new_word


Words.objects.distinct
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
            
            doc = request.FILES['doc']
        

            if doc.name.endswith(".docx"):
                docx = docx2python(doc, extract_image=False)
                context['doc'] = docx.text

            elif doc.name.endswith(".txt"):
                print("THis is a test")
                
                mytext = str(doc.read())

                context['doc'] = mytext

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
                original_list = []

                # LOOP THROUGH EACH WORD.
                for word in words:

                    clean_word = clear_punctuation(word)

                    in_db = Words.objects.all().filter(word__icontains=clean_word)

                    # WORD IS IN DATABASE
                    if in_db:

                        temp_list.append(clean_word)

                        temp_word = " ".join(temp_list)


                        starting_phrase = Words.objects.all().filter(word__startswith=temp_word)

                        # CURRENT WORD IS THE START OF THE PHRASE
                        if starting_phrase:

                            original_list.append(word)

                            completed = Words.objects.all().filter(word__iexact=temp_word)

                            # CURRENT PHRASE IS COMPLETED
                            if completed:
                                original = " ".join(original_list)
                                original_list.clear()

                                new_word = format_word(original)
                                wordlist.append(new_word)

                                temp_list.clear()

                            # TEMP WORD DID NOT COMPLETE THE PHRASE
                            # else:
                            #     temp_list.clear()
                            #     temp_list.append(temp_word)
                                
                        
                        # NOT START OF PHRASE KEEP GOING
                        else:
                            wordlist.append(word)
                            temp_list.clear()
                            original_list.clear()

                    # WORD IS A PROFANITY
                    elif pf._is_profane_word('en', clean_word):

                        temp_word = " ".join(temp_list)
                        wordlist.append(temp_word)

                        new_word = format_word(word)
                        wordlist.append(new_word)
                        temp_list.clear()
                        continue

                    # JUST A REGULAR WORD
                    else:
                        temp_word = " ".join(temp_list)
                        wordlist.append(temp_word)

                        wordlist.append(word)

                        temp_list.clear()

        
        context["results"] = " ".join(wordlist)
        context['document'] = document

        return render(request, 'index.html', context=context)


class DescriptionView(View):

    def get(self, request):

        context = {}
        word = request.GET.get('word')

        word = Words.objects.all().filter(word__iexact=word)

        context['word']= word
        
        return render(request, 'description.html', context)
