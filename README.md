Для начала работы месенджера необходимо:

Создать Django secret-key
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
В дириктории prjchat создать venv/settings.env и в файле settings написать строку 
SECRET_KEY = ''
и в ковычках прописать созданный secret key.
В терминале необходимо прописать
pip install -r requirements.txt

Всё готово к работе с месенжером
