import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.utils.html import escape

from .models import Question, Choice


def create_question(question_text, days):
    """
    Create a question with the given 'question_text' and published the
    given number of 'days' offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


def create_choice(question, choice_text, votes=0):
    return Choice.objects.create(
        question=question,
        choice_text=choice_text,
        votes=votes
    )


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than one day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() \
               - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_model_str(self):
        test_question = create_question('Test question', days=-5)
        self.assertEqual(
            test_question.__str__(),
            "{}: {}".format(test_question.id, test_question.question_text)
        )

    def test_model_repr(self):
        test_question = create_question('Test question', days=-5)
        self.assertEqual(
            test_question.__repr__(),
            test_question.question_text
        )


class ChoiceModelTests(TestCase):
    def test_model_str(self):
        test_choice = create_choice(
            create_question('Test question.', days=-5),
            'Choice text.'
        )
        self.assertEqual(
            test_choice.__str__(),
            "{}: {} ({})".format(
                test_choice.question, test_choice.choice_text,
                test_choice.id
            ))


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Question with a pub_date in the past are displayed on the
        index page.
        """
        past_question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['Past question.']
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on the
        index page.
        """
        future_question = create_question(question_text="Future question.", days=30)
        create_choice(future_question, choice_text='Choice text.')
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['Past question.']
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text='Past question 1.', days=-20)
        create_question(question_text='Past question 2.', days=-24)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['Past question 1.', 'Past question 2.']
        )

    def test_three_past_questions_one_without_choices(self):
        """
        The questions index page may display multiple questions.
        There will be only questions with at least one choice.
        """
        create_question(question_text='Past question 1.', days=-5)
        create_question(question_text='Past question 2.', days=-6)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['Past question 1.', 'Past question 2.']
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class QuestionResultsViewTests(TestCase):
    def test_future_question(self):
        """
        The results view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:results', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The results view of a question with a pub_date in the past
        returns the question vote results
        """
        past_question = create_question(question_text='Past question.', days=-5)
        url = reverse('polls:results', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)


class QuestionResultsVotesViewTests(TestCase):
    def test_post_vote_for_existed_question(self):
        """
        The results view of voted question displays increased
        value in the selected choice. Another choices will not
        be increased.
        """
        choice_1_initial_votes = 10
        choice_2_initial_votes = 100
        test_question = create_question(question_text='Test question.', days=-5)
        test_question_choice_1 = create_choice(
            test_question,
            choice_text='Test question choice 1.',
            votes=choice_1_initial_votes
        )
        test_question_choice_2 = create_choice(
            test_question,
            choice_text='Test question choice 2.',
            votes=choice_2_initial_votes
        )
        response = self.client.post(
            reverse(
                'polls:vote',
                args=(test_question.id,)
            ),
            {
                'choice': test_question_choice_1.id,
            }
        )
        test_question_choice_1.refresh_from_db()
        test_question_choice_2.refresh_from_db()
        self.assertRedirects(response, reverse('polls:results', args=(test_question.id,)), status_code=302)
        self.assertEqual(response.url, reverse('polls:results', args=(test_question.id,)))
        self.assertEqual(choice_1_initial_votes + 1, test_question_choice_1.votes)
        self.assertEqual(choice_2_initial_votes, test_question_choice_2.votes)

    def test_post_vote_for_not_excited_choice(self):
        """
        The results view of voted question displays
        'You didn't select a choice.'
        """
        test_question = create_question('Test question.', days=-5)
        response = self.client.post(
            reverse(
                'polls:vote',
                args=(test_question.id,)
            ),
            {
                'choice': 0,
            }
        )
        self.assertContains(response, escape("You didn't select a choice."))
