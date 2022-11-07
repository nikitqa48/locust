import random
from locust import constant, task, TaskSet, SequentialTaskSet
from settings import stage_url, headers


courses = {}


def get_all_courses(locust):
    global courses
    courses = {
        'slugs': [],
    }
    url = stage_url + 'api/v1/courses/'
    response = locust.client.get(url)
    json = response.json()
    courses['slugs'] = [i['slug'] for i in json]


def check_exercises(locust):
    global courses
    courses['course'] = []
    for slug in courses['slugs']:
        url = stage_url + f'api/v1/admin/courses/{slug}/'
        response = locust.client.get(url, headers=headers)
        json = response.json()
        exercices = []
        for exercise in json['exercises']:
            url = stage_url + f'api/v1/courses/{slug}/exercises/{exercise["id"]}/'
            exercise_response = locust.client.get(url)
            exercise_json = exercise_response.json()
            exercise = {
                'id': exercise_json['id'],
                'solution': exercise_json['solution'],
                'course_slug': slug
            }
            exercices.append(exercise)
        course = {
            'slug': slug,
            'exercises': exercices
        }
        courses['course'].append(course)
        return 'ok'


def factory(exercise):
    def _locust(locust):
        url = f'{stage_url}/checkExercise/{exercise["id"]}?isGraphRequired=false&xp=70&userId=171'
        response = locust.client.post(url, json=exercise['solution'])
        return response.json()
    return _locust


def test_course_exercise(locust):
    for course in courses['course']:
        for exercise in course['exercises']:
            url = f'{stage_url}checkExercise/{exercise["id"]}?isGraphRequired=false&xp=70&userId=171/'
            response = locust.client.post(url, json=exercise['solution'])
            json = response.json()
            print(json)


mytask = [get_all_courses, check_exercises, test_course_exercise]


class ExersiseTaskSet(SequentialTaskSet):
    min_wait = 1000
    max_wait = 5000
    tasks = mytask

    # @task
    # def get_all_courses(self):
    #     # https://stage.deepskills.ru/api/v1/admin/courses/data-types-in-python-for-data-science
    #     url = stage_url + 'api/v1/courses/'
    #     response = self.client.get(url)
    #     json = response.json()
    #     courses_slug = [i['slug'] for i in json]
    #     url = stage_url + 'api/v1/courses/manipulating-data-with-pandas/'
    #     response = self.client.get(url, headers=headers)
    #     print(response.json())
    #
    #
    # @task
    # def redirect_exersize(self):
    #     url = 'https://stage.deepskills.ru/courses/introduction-to-python/exercises/162'
    #     response = self.client.get(url)
    #
    # @task
    # def complete_exersize(self):
    #     random_course = random.choice(courses_quiz)
    #     url = f'https://stage.deepskills.ru/ipythonshell/v1/execute?exerciseId={random_course["num"]}&userId=171&isGraphRequired=false'
    #     response = self.client.post(url, json=random_course['code'])
    #     code_status = response.content.decode('utf-8')
    #
    # @task
    # def test_code(self):
    #     random_course = random.choice(courses_quiz)
    #     url = f'https://stage.deepskills.ru/checkExercise/{random_course["num"]}?isGraphRequired=false&xp=70&userId=171'
    #     response = self.client.post(url, json=courses_quiz[0]['code'])
    #     code_status = response.content.decode('utf-8')
    #     print('test code')
    #
    #
