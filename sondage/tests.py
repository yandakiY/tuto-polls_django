from django.test import TestCase
from sondage.models import Question , Choice
from django.utils import timezone
from django.urls import reverse
import datetime
# Create your tests here.

def create_question(text: str , duration: int):
    
    time = timezone.now() + datetime.timedelta(days=duration)
    return Question.objects.create(question_text=text , date_pub=time)

class IndexViewTest(TestCase):
    
    # A question recent without a choice
    def testNoChoiceForQuestion(self):
        question = create_question(text="No choice" , duration=0)
        # call index
        response = self.client.get(reverse('sondage:index'))
        # 
        print(response.context['question_lists'])
        self.assertEqual(len(response.context['question_lists']) , 0)
        
    # test no questions in database
    def testNoQuestionInDB(self):
        # calls the url sondage, check status code (200) and the contains
        response = self.client.get(reverse('sondage:index'))
        # status code
        self.assertEqual(response.status_code , 200)
        # Check inner HTML index response
        self.assertContains(response , "No polls in database.")
        
    
    def testQuestionInDBOldDate(self):
        # create a old date publication
        question_past = create_question(text="Old question" , duration=-30)
        # calls url index
        Choice.objects.create(question=question_past , choice_text="Choice 1" , votes=0)
        response = self.client.get(reverse('sondage:index'))
        # check Query set
        self.assertQuerysetEqual(response.context['question_lists'] , [question_past])
    
    # test question with a future date of publication
    def testQuestionInDbFutureDate(self):
        # create a future date pub
        question_future = create_question(text="Future questio" , duration=30)
        # calls url index
        response = self.client.get(reverse('sondage:index'))
        # use assert
        # self.assertContains(response, "No polls in database.")
        self.assertQuerysetEqual(response.context['question_lists'] , [])
    
    # in this we have an old question and a question with a future date of publication
    def testQuestionInDbFutureAndOldDate(self):
        
        # create a recent and future question
        question_past = create_question(text="Old question" , duration=-30)
        # add a choice for past question
        Choice.objects.create(question=question_past , choice_text="Choice 1")
        # future question
        create_question(text="future question" , duration=30)
        # calls sondage:index
        response = self.client.get(reverse('sondage:index'))
        # use assertQueryEqual
        self.assertQuerysetEqual(response.context['question_lists'] , [question_past])

    # in this we have only old question in our DB
    def testQuestionInDbTwoOldDate(self):
        
        # create two olds question
        question_1 = create_question(text="question 1" , duration=-20)
        # add choice for question_1
        Choice.objects.create(question=question_1 , choice_text="Choice 1")
        question_2 = create_question(text="question 2" , duration=-5)
        Choice.objects.create(question=question_2 , choice_text="Choice 2")
        
        # calls index
        response = self.client.get(reverse('sondage:index'))
        self.assertQuerysetEqual(response.context['question_lists'] , [question_2 , question_1])


class DetailViewTest(TestCase):
    
    def testViewFutureQuestio(self):
        
        question_future = create_question(text="Future Q" , duration=30)
        # call details
        url = reverse("sondage:details" , args=(question_future.id,))
        response = self.client.get(url)
        #
        # print()
        # print("Status code" , response)
        self.assertEqual(response.status_code , 404)
        
    def testViewOldQuestion(self):
        
        question_past = create_question(text="Old Question" , duration=-30)
        # calls details url
        url = reverse("sondage:details" , args=(question_past.id,))
        # 
        response = self.client.get(url)
        self.assertEqual(response.status_code , 200)
        
class QuestionModelTest(TestCase):

    # test with a question in date publicatiton in the future
    def testModelWithFutureDatePub(self):
        # create a Question with a future date_pub 
        # use AssertIs
        
        time = datetime.timedelta(days=30) + timezone.now()
        question_future = Question(date_pub=time)
        
        self.assertIs(question_future.is_recent() , False)
        
    
    # test with a question in date publication more than 1 days
    def testModelWithDatePubMoreOneDay(self):
        
        # time, datetime de plus d'un jour => datetime.timedelta(days=1 , seconds=1)
        time = timezone.now() - datetime.timedelta(days=1 , seconds=1)
        #
        question = Question(date_pub=time)
        # 
        self.assertIs(question.is_recent() , False)
        
    def testModelWithDatePubLessOneDay(self):
        
        # time, use datetime less than one 
        time = timezone.now() - datetime.timedelta(hours=23 , minutes=59 , seconds=59)
        # question
        question = Question(date_pub=time)
        # 
        self.assertIs(question.is_recent() , True)