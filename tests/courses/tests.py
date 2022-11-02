import random
from locust import constant, task, TaskSet
from settings import stage_url, headers


class CourseTaskSet(TaskSet):
    wait_time = constant(1)

    @task
    def courses_page(self):
        url_name = 'Страница курсов'
        url = 'https://stage.deepskills.ru/courses'
        response = self.client.get(url)
        print(f'{url_name} код {response.status_code}')

    @task
    def create_course(self):
        self.client.post(
            url=stage_url+'courses/'
        )

    @task
    def get_profession(self):
        url = stage_url + 'career_tracks/'
        response = self.client.get(url)

    @task
    def get_detail_profession(self):
        url = stage_url + 'career_tracks/1/'
        response = self.client.get(url)

    @task
    def get_detail_course(self):
        url = stage_url + 'courses/1/'
        response = self.client.get(url)

    @task
    def get_all_intsructors(self):
        url = stage_url + 'api/v1/instructors/'
        response = self.client.get(url)

    @task
    def get_all_slugs(self):
        url = stage_url + 'api/v1/courses/slugs/'
        response = self.client.get(url)

    @task
    def get_all_slugs_for_course(self):
        url = stage_url + 'api/v1/courses/1/exercises/slugs/'
        resonse = self.client.get(url)

    @task
    def delete_course(self):
        url = stage_url + '/api/v1/admin/courses/86/'
        pass

    @task
    def create_course(self):
        data = {
            'title': 'test',
            'description': 'descript',
            'difficulty': 'medium',
            'instructor_id': '16',
            'lang': 'sql',
            'time': '12',
        }
        url = stage_url + 'api/v1/courses/'
        response = self.client.post(url, headers=headers, data=data)
        self.coure_id = response.json()['id']

    @task
    def delete_task(self):
        pass