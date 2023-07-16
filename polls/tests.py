from django.test import TestCase
from django.utils import timezone
import datetime
from polls.models import Question , Choice
from django.urls import reverse
 
# Create your tests here.

# def function create question
def create_question(question_text , days):
    """ """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text , date_pub=time)

# Class Question Index View Test
class QuestionIndexViewTests(TestCase):
    
    def test_question_without_choice(self):
        # create question without
        create_question(question_text="Without question" , days=1)
        # calls 'polls:index'
        response = self.client.get(reverse('polls:index'))
        # check with 
        self.assertEqual(len(response.context['join_elements']) , 0)
        
    # def test_question_with_choice(self):
    #     # create question without
    #     question = create_question(question_text="With question" , days=1)
    #     # add Choice
    #     Choice.objects.create(question=question , choice_text="Choice 1")
    #     # calls 'polls:index'
    #     response = self.client.get(reverse('polls:index'))
    #     # check with 
    #     # self.assertQuerysetEqual(response.context['join_elements'] , [question])
    #     print(response.context['join_elements'])
        
    
    
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        # use client (Client())
        # use client.get with self
        # use assertEqual for compare
        # and use assertContains
        response = self.client.get(reverse("polls:index"))
        # print('status' , response.status_code)
        # check status code
        self.assertEqual(response.status_code, 200)
        # check if content is the same
        self.assertContains(response , 'No polls are available.')
        
        
    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        # create a question
        # get response for 'polls:index'
        # compare with assertQuerySetEqual
        # 1- create question
        question = create_question(question_text='Past question' , days=-30) # s'il y'a seulement des questions avec des dates passées
        # add choice to this question
        Choice.objects.create(question=question , choice_text="Choice 1")
        # 2 - get response for 'polls:index'
        response = self.client.get(reverse('polls:index'))
        # 3 - compare Query Set with assertQuerySetEqual
        self.assertQuerysetEqual(response.context['join_elements'] , [question]) 

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        # create a future question
        # get 'polls:index' url
        # use assertContains , for check if content of my 'gabarit' == 'No polls are available.'
        create_question(question_text="Future question" , days=30) # S'il y'a seulement une question avec date_pub dans le futur, on affiche rien normalement
        # calls url 'polls'
        response = self.client.get(reverse('polls:index'))
        # use assertContains
        self.assertContains(response , 'No polls are available.')
        
    def test_future_question_and_past_question(self):
        # create a past question and then future question
        # use client.get to polls:index
        # check with assertQuerySetEqual if 'polls:index' return only the past question
        question = create_question(question_text='Past question' , days=-30)
        # add choice 
        Choice.objects.create(question=question , choice_text="Choice text")
        # future question
        create_question(question_text='Future question' , days=30)
        # calls 'polls:index'
        response = self.client.get(reverse('polls:index'))
        # check with assertQuerySetEqual
        self.assertQuerySetEqual(response.context['join_elements'] , [question])


    def test_two_past_questions(self):
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)

        # Add two choice for each question
        Choice.objects.create(question=question1 , choice_text="Choice 1")
        Choice.objects.create(question=question2 , choice_text="Choice 2")
        # calls 'polls:index'
        response = self.client.get(reverse('polls:index'))
        # check 
        self.assertQuerysetEqual(response.context['join_elements'] , [question2 , question1])


# Class for test Detail View
class QuestionDetailViewTests(TestCase):
    
    def test_future_question(self):
        """The details view of a question with a pub_date in the future
        returns a 404 not found."""
        
        # Create future question
        future_q = create_question(question_text='Future question' , days=30)
        # determine the url, (url = 'polls:detail' and future_q.id)
        url = reverse("polls:details" , args=(future_q.id,))
        # call this urls
        response = self.client.get(url)
        # use assertEqual
        self.assertEqual(response.status_code , 404)
        
    
    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        
        # create past question
        past_question = create_question(question_text='Past question' , days=-30)
        # determine url
        url = reverse("polls:details" , args=(past_question.id,))
        # determine response
        response = self.client.get(url)
        # use assertContains
        self.assertContains(response , past_question.question_text)



class QuestionResultViewTests(TestCase):
    pass
    
    

class QuestionModelTests(TestCase):
    
    # Test if question is a future question
    def test_was_published_recently_with_future_question(self):
        """
        1- Create a Question with a date in future (use datetime.timedelta(days=30))
        2- Returns a False
        """
        # time
        time = timezone.now() + datetime.timedelta(days=30)
        # future question
        future_q = Question(date_pub=time)
        
        self.assertIs(future_q.was_published_recently() , False)
        
    # test if question is an old question
    def test_was_published_recently_with_old_question(self):
        """
            was_published_recently() returns False for questions whose date_pub
            is older than 1 day.
        """
        
        # time
        time = timezone.now() - datetime.timedelta(days=1 , seconds=1)
        # question to test
        future_q = Question(date_pub = time)
        self.assertIs(future_q.was_published_recently() , False)
        
    
    # test if question is recent
    def test_was_published_recently_with_recent_question(self):
        
        time = timezone.now() - datetime.timedelta(hours=23 , minutes=59, seconds=59)
        
        future_q = Question(date_pub = time)
        
        self.assertIs(future_q.was_published_recently() , True)
        
    
    