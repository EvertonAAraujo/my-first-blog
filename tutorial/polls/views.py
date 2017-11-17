from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Pergunta, Escolha


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Pergunta.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Pergunta
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Pergunta
    template_name = 'polls/results.html'

def voto(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        selected_escolha = pergunta.escolha_set.get(pk=request.POST['escolha'])
    except (KeyError, Escolha.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': pergunta,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_escolha.votos += 1
        selected_escolha.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(pergunta.id,)))