import os
import environ

env = environ.Env()
env.read_env(".env")

DJANGO_WEB_PORT = env.str("DJANGO_WEB_PORT")

bind = f"0.0.0.0:{DJANGO_WEB_PORT}"
workers = 3

log_dir = "logs"

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

log_access = os.path.join(log_dir, "access.log")
log_error = os.path.join(log_dir, "error.log")
