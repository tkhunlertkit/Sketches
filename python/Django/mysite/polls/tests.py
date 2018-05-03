import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question, Choice

# Create your tests here.

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

def create_choice(question, choice_text):
    return Choice.objects.create(question=question, choice_text=choice_text)

class QuestionIndexViewTests(TestCase):

    def test_no_question(self):
        """
        If not question exists, appropriate message is displayed
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available.')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_questions(self):
        """
        Questions with pub date in the past is displayed
        """
        q = create_question(question_text='Past question.', days=-30)
        create_choice(question=q, choice_text='1')
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
        pass

    def test_past_question_max_5(self):
        """
        Questions with pub date in the past is displayed, caped to a maximum of 5 questions
        """
        for i in range(7):
            q = create_question(question_text='blah %s' % i, days=-i)
            create_choice(question=q, choice_text=i)
        expected_list = ['<Question: blah %s>' % i for i in range(5)]
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], expected_list)
        self.assertEqual(len(response.context['latest_question_list']), 5)

    def test_future_questions(self):
        """
        Questions in the future are not included in the list
        """
        q = create_question(question_text='for infinity and beyond...', days=40)
        create_choice(question=q, choice_text='First Choice')
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_and_past_questions(self):
        """
        Questions in the future are not included in the list
        """
        for i in range(-2, 3):
            q = create_question(question_text='blah %s' % i, days=i)
            create_choice(question=q, choice_text=i)
        expected_output = ['<Question: blah %s>' % i for i in reversed(range(-2, 1))]
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], expected_output)
        self.assertEqual(len(response.context['latest_question_list']), 3)

    def test_question_with_only_choices_present_expect_empty_list(self):
        """
        Questions with no choices are not displayed.
        All questions do not have choices for this test
        """
        q = create_question('no choice', days=0)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_question_with_only_choices_present(self):
        """
        Questions with no choices are not displayed
        """
        q = create_question('no choice', days=0)
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerysetEqual(response.context['latest_question_list'], [])


class QuestionDetailViewTests(TestCase):

    def test_future_question(self):
        """
        Questions in the future are not accessible by know urls
        """
        future_question = create_question(question_text='Future Question', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        Questions in the past are shown correctly
        """
        past_question = create_question(question_text='Past Question.', days=-12)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_question.question_text)


class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)