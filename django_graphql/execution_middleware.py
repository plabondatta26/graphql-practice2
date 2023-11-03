import time
import json


class GraphQLExecutionTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        if 'application/json' in response.get('Content-Type', ''):
            execution_time = end_time - start_time
            content = json.loads(response.content)
            content['execution'] = {'executionTime': f'{execution_time} seconds'}
            response.content = json.dumps(content)
        return response
