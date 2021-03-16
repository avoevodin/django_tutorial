from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F, Count
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set
        to be published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now(),
            choice__isnull=False,
        ) \
            .annotate(Count('choice')) \
            .filter(choice__count__gte=0) \
            .order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now(),
            choice__isnull=False,
        ) \
            .annotate(Count('choice')) \
            .filter(choice__count__gte=0)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now(),
            choice__isnull=False,
        ) \
            .annotate(Count('choice')) \
            .filter(choice__count__gte=0)


class ResultsVotesView(generic.View):
    def post(self, request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs.get('pk'))
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes = F('votes') + 1
            selected_choice.save()
            # Always returns an HTTPResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse(
                'polls:results',
                args=(question.id,),
            ))
