import environ
import multiprocessing

env = environ.Env()
env.read_env(".env")

cpu_count = multiprocessing.cpu_count()

DJANGO_WEB_PORT = env.str("DJANGO_WEB_PORT")

bind = f"0.0.0.0:{DJANGO_WEB_PORT}"
workers = cpu_count * 2 + 1
