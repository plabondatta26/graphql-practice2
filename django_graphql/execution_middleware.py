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
            success_message = getattr(request, 'success_message', None)
            error_message = getattr(request, 'error_message', None)
            total_count = getattr(request, 'total_count', None)
            if success_message:
                content['success_message'] = success_message
            if error_message:
                content['error_message'] = error_message
            if total_count:
                content['total_count'] = total_count

            response.content = json.dumps(content)
        return response


class GraphQLPaginationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if 'application/json' in response.get('Content-Type', ''):
            content = json.loads(response.content)
            for key, value in content:
                if type(value) == list:
                    pass
                    # content['execution'] = {'executionTime': f'{execution_time} seconds'}
            response.content = json.dumps(content)
        return response
