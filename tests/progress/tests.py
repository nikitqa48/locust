import random
from locust import constant, task, TaskSet
from settings import stage_url, headers


class ProgressTaskSet(TaskSet):
    wait_time = constant(1)

    @task
    def get_progress(self):
        url = stage_url + 'api/v1/progress/'
        response = self.client.get(url, headers=headers)
        print(response.status_code)

    @task
    def get_allcoures_progress(self):
        url = stage_url + 'api/v1/courses_done/'
        response = self.client.get(url, headers=headers)
        print(response.status_code)

    @task
    def get_skills_progress(self):
        url = stage_url + 'api/v1/skills_progress/'
        response = self.client.get(url, headers=headers)
        print(response.status_code)

    @task
    def get_careers_progress(self):
        url = stage_url + 'api/v1/careers_progress/'
        response = self.client.get(url, headers=headers)

    @task
    def clean_progress(self):
        url = stage_url + 'api/v1/drop_progress/introduction-to-python/'
        response = self.client.delete(url, headers=headers)
