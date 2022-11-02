import random
from locust import constant, task, TaskSet, SequentialTaskSet
from settings import stage_url, headers


class CourseTaskSet(SequentialTaskSet):
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
    def create_course(self):
        data = {
            'title': 'test',
            'description': 'descript',
            'difficulty': 'medium',
            'instructor_id': '16',
            'lang': 'sql',
            'time': '12',
        }
        self.course_data = data
        url = stage_url + 'api/v1/courses/'
        response = self.client.post(url, headers=headers, data=data)
        self.course_id = response.json()['id']
        print('ok')

    @task
    def update_course(self):
        url = stage_url + f'api/v1/courses/{self.course_id}'
        response = self.client.patch(url, headers=headers, data=self.course_data)
        print('updated_data')

    @task
    def delete_course(self):
        url = stage_url + f'api/v1/admin/courses/{self.course_id}/'
        response = self.client.delete(url, headers=headers)
        print(response.status_code, 'all')