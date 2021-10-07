import glob
from datetime import date
from typing import List, Dict
import git


class LeetCodeCurve:

    def __init__(self):
        self.review_days: List[int] = [1, 2, 4, 7, 15]
        self.github_token = None
        self.github_repository = 'https://github.com/wuqunfei/algopycode.git'
        self.repository_path = '.'
        self.repository = git.Repo(self.repository_path)
        self.path = './leetcode/editor/en/*.py'

    def __int__(self):
        ...
        # self.repository.clone(self.repository_path)

    def find_question_by_commit(self) -> Dict:
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

            return {'question_id': question_id,
                    'question_name': question_name,
                    'question_dates': question_dates}

    def review_question_by_day(self, day: date) -> List[int]:
        """
        :return:
        """

    def get_reports_by_status(self):
        """

        :return:
        """

    def get_report_by_tags(self):
        """

        :return:
        """

    def get_report_by_company(self, company_name: str):
        """"""


curve = LeetCodeCurve()
curve.find_question_by_commit()
