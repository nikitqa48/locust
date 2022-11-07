from locust import HttpUser, TaskSet, task, HttpLocust
from tasks import TaskSet

from tests.courses.tests import CourseTaskSet
from tests.exercsises.tests import ExersiseTaskSet
from tests.progress.tests import ProgressTaskSet


class WebsiteUser(HttpUser):
    @task
    class TaskSets(ExersiseTaskSet):
        pass

