from locust import HttpUser, TaskSet, task
from tasks import TaskSet


class WebsiteUser(HttpUser):
    @task
    class MyTask(TaskSet):
        pass

