from locust import constant, task, SequentialTaskSet

data = {
    "code": "print(16)"
}


class TaskSet(SequentialTaskSet):
    wait_time = constant(1)

    @task
    def redirect_exersize(self):
        url = 'https://stage.deepskills.ru/courses/introduction-to-python/exercises/162'
        response = self.client.get(url)

    @task
    def complete_exersize(self):
        url = 'https://stage.deepskills.ru/ipythonshell/v1/execute?exerciseId=162&userId=171&isGraphRequired=false'
        response = self.client.post(url, json=data)

    @task
    def test_code(self):
        url = 'https://stage.deepskills.ru/checkExercise/162?isGraphRequired=false&xp=70&userId=171'
        response = self.client.post(url, json=data)


