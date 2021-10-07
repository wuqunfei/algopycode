import glob
from datetime import date, datetime, timedelta
from ordered_set import OrderedSet
from pytz import timezone
from typing import List
import git


class Question:

    def __init__(self):
        self.question_id: str = None
        self.question_name: str = None
        self.dates: List[date] = None
        self.reviewed: OrderedSet = OrderedSet()
        self.reviews: dict = {1: {}, 2: {}, 4: {}, 7: {}, 15: {}}

    def __str__(self):
        return f'id: {self.question_id}, ' \
               f'name: {self.question_name}, ' \
               f'reviews: {self.reviews}, ' \
               f'reviewed: {self.reviewed}'


class LeetCodeCurve:

    def __init__(self):
        self.github_token = None
        self.github_repository = 'https://github.com/wuqunfei/algopycode.git'
        self.repository_path = '.'
        self.repository = git.Repo(self.repository_path)
        self.path = './leetcode/editor/en/*.py'

    def __int__(self):
        ...
        # self.repository.clone(self.repository_path)

    def find_question_by_commit(self) -> List:
        """
        1. question id KEY
        2. review days
        :return:{8:[], 146:[1,2,4]}
        """
        tree = self.repository.tree()
        questions = []
        for file_path in glob.glob(self.path):
            commits = list(self.repository.iter_commits(paths=file_path, max_count=-1))
            question = self.get_question_info(file_path, commits)
            if question:
                questions.append(question)
        return questions

    def get_question_info(self, file_path, commits):
        left_index = file_path.find('[')
        right_index = file_path.find(']') + 1
        if left_index and right_index:
            question_id = file_path[left_index: right_index]
            question_name = file_path[right_index:]
            question_dates = []
            for commit in commits:
                question_dates.append(commit.committed_datetime)

            qs = Question()
            qs.question_id = question_id
            qs.question_name = question_name
            qs.dates = question_dates
            return qs

    def review_question_by_day(self, questions: List[Question], day: date = None) -> List[Question]:
        if day is None:
            day = datetime.now()
        tz = timezone('Europe/Berlin')
        for index, question in enumerate(questions):
            for j, committed_day in enumerate(sorted(question.dates)):
                if j == 0:
                    questions[index] = self.review_match(question, committed_day)
                day_delta = tz.localize(day) - committed_day
                days = day_delta.days
                question.reviewed.add(days)
            questions[index] = question
        return questions

    def review_match(self, question: Question, start_day: date):
        for key, value in question.reviews.items():
            question.reviews[key] = start_day + timedelta(days=key)
        return question


curve = LeetCodeCurve()
questions = curve.find_question_by_commit()
questions = curve.review_question_by_day(questions, None)
for question in questions:
    print(question)
