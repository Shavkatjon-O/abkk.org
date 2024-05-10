import environ

env = environ.Env()
env.read_env(".env")

DJANGO_WEB_PORT = env.str("DJANGO_WEB_PORT")

bind = f"0.0.0.0:{DJANGO_WEB_PORT}"
workers = 3
