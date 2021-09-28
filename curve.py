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
        for blob in tree.blobs:
            commits = list(self.repository.iter_commits(paths=blob.path, max_count=-1))
            print(commits)
        return {}

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
