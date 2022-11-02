from locust import HttpUser, TaskSet, task
from tasks import TaskSet

from tests.courses.tests import CourseTaskSet
from tests.exercsises.tests import ExersiseTaskSet
from tests.progress.tests import ProgressTaskSet


class WebsiteUser(HttpUser):
    @task
    class TaskSets(ProgressTaskSet, CourseTaskSet):
        pass



