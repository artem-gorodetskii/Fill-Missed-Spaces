from api import (
    health_check,
    space_prediction,
    error_handler,
    home
)


routes = [health_check.routes,
          space_prediction.routes,
          error_handler.routes,
          home.routes]
