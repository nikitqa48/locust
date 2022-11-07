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

