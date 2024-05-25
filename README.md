- clone repository locally

```
git clone https://github.com/Shavkatjon-O/tempo-clone.git
```
```
python -m venv venv
```
```
source venv/bin/activate
```
```
pip install -r requirements/develop.txt
```
```
cp .env.example .env
```
```
python manage.py runserver
```

- setup pre-commit

```
pre-commit install
pre-commit run --all-files
```

- run django tailwind css

```
sudo npm install -g cross-env
python manage.py tailwind install
python manage.py tailwind start
```

- do this if you run gunicorn manually

```
gunicorn -c gunicorn_conf.py core.wsgi:application
```
