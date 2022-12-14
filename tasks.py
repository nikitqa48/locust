import random
from locust import constant, task, TaskSet
from tests.courses import tests as courses_test

stage_url = 'https://stage.deepskills.ru/api/v1/'

courses_quiz = [
    {
        'num': '162',
        'code': 'print(7 + 9)'
    },
    {
        'num': '286',
        'code': '# Сложение'
    },
    {
        'num': '429',
        'code': '100000 ** 10'
    }
]


class TaskSet(TaskSet):
    wait_time = constant(1)

    @task
    def redirect_exersize(self):
        url = 'https://stage.deepskills.ru/courses/introduction-to-python/exercises/162'
        response = self.client.get(url)

    @task
    def complete_exersize(self):
        random_course = random.choice(courses_quiz)
        url = f'https://stage.deepskills.ru/ipythonshell/v1/execute?exerciseId={random_course["num"]}&userId=171&isGraphRequired=false'
        response = self.client.post(url, json=random_course['code'])
        code_status = response.content.decode('utf-8')

    @task
    def test_code(self):
        random_course = random.choice(courses_quiz)
        url = f'https://stage.deepskills.ru/checkExercise/{random_course["num"]}?isGraphRequired=false&xp=70&userId=171'
        response = self.client.post(url, json=courses_quiz[0]['code'])
        code_status = response.content.decode('utf-8')

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
        print(response.status_code)