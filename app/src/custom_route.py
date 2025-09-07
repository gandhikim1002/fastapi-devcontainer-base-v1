from fastapi.routing import APIRoute
from typing import Callable

class CustomRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_handler(request):
            # Add custom logic before or after calling the original handler
            print(f"Request received: {request.url}")
            response = await original_route_handler(request)
            print(f"Response sent: {response.status_code}")
            return response
        return custom_handler