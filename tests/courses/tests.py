import random
from locust import constant, task, TaskSet

stage_url = 'https://stage.deepskills.ru/api/v1/'


class CourseTaskSet(TaskSet):
    wait_time = constant(1)

    @task
    def courses_page(self):
        url_name = 'Страница курсов'
        url = 'https://stage.deepskills.ru/courses'
        response = self.client.get(url)
        print(f'{url_name} код {response.status_code}')

    @task
    def get_profession(self):
        url = stage_url + 'career_tracks/'
        response = self.client.get(url)

    @task
    def get_detail_profession(self):
        url = stage_url + 'career_tracks/1/'
        response = self.client.get(url)

    @task
    def get_detail_admin_profession(self):
        url = stage_url + 'admin/career_tracks/'
        response = self.client.get(url)
        # print(response.status_code)