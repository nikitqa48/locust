from locust import HttpUser, TaskSet, task
from tasks import TaskSet

from tests.courses.tests import CourseTaskSet
from tests.exercsises.tests import ExersiseTaskSet

stage_url = 'https://stage.deepskills.ru/api/v1/'


class WebsiteUser(HttpUser):
    @task
    class TaskSets(CourseTaskSet, ExersiseTaskSet):
        pass



