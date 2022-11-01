import random
from locust import constant, task, TaskSet
from tests.courses import tests as courses_test


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


class ExersiseTaskSet(TaskSet):
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
        print('test code')
