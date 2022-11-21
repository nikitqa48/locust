import random
from locust import constant, task, TaskSet, SequentialTaskSet
from settings import stage_url, headers


class ExersiseTaskSet(SequentialTaskSet):
    wait_time = constant(1)


    @task
    def check_exersize(self):
        url = stage_url + f'api/v1/admin/courses/introduction-to-sql/'
        response = self.client.get(url, headers=headers)
        json = response.json()
        for exercise in json['exercises']:
            ex_url = f'{stage_url}api/v1/courses/introduction-to-sql/exercises/{exercise["id"]}/'
            ex_response = self.client.get(ex_url, headers=headers)
            ex = {
                'id': exercise['id'],
                'solution': ex_response.json()['solution']
            }
            url = f'{stage_url}checkExercise/{exercise["id"]}?isGraphRequired=false&xp=70&userId=171/'
            response = self.client.post(url, json=ex['solution'])
            print(response.json())

