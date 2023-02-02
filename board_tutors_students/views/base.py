import datetime

from django.views.generic import ListView, DetailView, TemplateView

from accounts.models import Account
from cabinet_parents.models import Survey
from cabinet_tutors.models import TutorCabinets, SubjectsAndCosts, Education
from reviews.models import Review


class BoardTutorView(ListView):
    template_name = 'board_tutor.html'
    model = TutorCabinets
    context_object_name = 'tutors'


class BoardStudentView(ListView):
    template_name = 'board_student.html'
    model = Survey
    context_object_name = 'surveys'


class TutorBoardDetailPageView(DetailView):
    template_name = 'tutor_board_detail_page.html'
    model = TutorCabinets
    context_object_name = 'tutor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tutor = TutorCabinets.objects.get(id=self.object.pk)
        on_tutor_reviews = Review.objects.filter(tutor=tutor.user)
        review_rate_list = []
        for review in on_tutor_reviews:
            review_rate_list.append(review.rate)
        if len(review_rate_list) > 0:
            middle_rate = sum(review_rate_list) / len(review_rate_list)
            context['middle_rate'] = round(middle_rate, 1)

        cost_list = []
        costs = SubjectsAndCosts.objects.filter(tutors=self.object)
        exp = SubjectsAndCosts.objects.first()
        experience = exp.experience
        for cost in costs:
            cost_list.append(cost.cost)
        if len(cost_list) > 0:
            middle_cost = round(sum(cost_list) / len(cost_list))
            context['middle_cost'] = middle_cost
        educations = tutor.education.all()

        reviews = Review.objects.filter(tutor_id=tutor.user.pk)

        reviews_stats = Review.objects.filter(tutor_id=tutor.user.pk)
        if reviews_stats:
            five_sum = []
            four_sum = []
            three_sum = []
            two_sum = []
            one_sum = []
            for rate in reviews_stats:
                if rate.rate == 5:
                    five_sum.append(rate.rate)
                if rate.rate == 4:
                    four_sum.append(rate.rate)
                if rate.rate == 3:
                    three_sum.append(rate.rate)
                if rate.rate == 2:
                    two_sum.append(rate.rate)
                if rate.rate == 1:
                    one_sum.append(rate.rate)
            five_sum = len(five_sum)
            four_sum = len(four_sum)
            three_sum = len(three_sum)
            two_sum = len(two_sum)
            one_sum = len(one_sum)
            summary_rate = five_sum + four_sum + three_sum + two_sum + one_sum
            proportion_five_sum = five_sum * 100 / summary_rate
            proportion_four_sum = four_sum * 100 / summary_rate
            proportion_three_sum = three_sum * 100 / summary_rate
            proportion_two_sum = two_sum * 100 / summary_rate
            proportion_one_sum = one_sum * 100 / summary_rate

            context['proportion_five_sum'] = round(proportion_five_sum)
            context['proportion_four_sum'] = round(proportion_four_sum)
            context['proportion_three_sum'] = round(proportion_three_sum)
            context['proportion_two_sum'] = round(proportion_two_sum)
            context['proportion_one_sum'] = round(proportion_one_sum)

            context['five_sum'] = five_sum
            context['four_sum'] = four_sum
            context['three_sum'] = three_sum
            context['two_sum'] = two_sum
            context['one_sum'] = one_sum

        context['tutor'] = tutor
        context['reviews'] = on_tutor_reviews
        context['reviews_count'] = len(review_rate_list)
        context['educations'] = educations
        context['experience'] = experience
        context['reviews'] = reviews


        return context


class StudentBoardDetailPageView(DetailView):
    template_name = 'student_board_detail_page.html'
    model = Survey
    context_object_name = 'survey'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        survey = Survey.objects.get(id=self.kwargs['pk'])
        date_format = "%m/%Y"
        # print(datetime.datetime.now())
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        print(survey.user.birthday)
        print(now)
        delta = int(now[0:4]) - int(survey.user.birthday[0:4])
        print(delta)
        context['age'] = delta
        return context