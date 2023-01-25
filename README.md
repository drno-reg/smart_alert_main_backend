# smart_alert_main_backend

Собираем docker image

```bash
docker build -t drno/smart_alert_main_backend:0.1.0 -f docker/test/Dockerfile ./
```

Запускам docker container

```bash
docker run --rm --name=smart_alert_main_backend_local \
           --net smart_alert_network \
           --publish 8002:8000 \
           drnoreg/smart_alert_main_backend:0.1.0
```

Подключиться к docker container

```bash
docker exec -it smart_alert_main_backend_local /bin/bash
```


Посмотреть логи docker контейнера в реальном времени
```bash
docker logs -f --tail 10 smart_alert_main_backend_local
```

Получить информцию о docker, предваритель необходимо установить jq
```bash
docker inspect -f '{{json .Config}}' smart_alert_main_backend_local | jq '.Env'
```

Для настройки логов создаем файл
/etc/docker/daemon.json
```bash
{
"log-driver": "json-file",
"log-opts": {"max-size": "10m", "max-file": "3"}
}
```

Удаляем неиспользуемые Docker Images

```bash
docker rmi $(docker images -a -q)
```

в ansible playbook:

перед запуском playbook необходимо объявить ENV чтобы переопделить путь к ansible cfg

```bash
export ANSIBLE_CONFIG="ansible/ansible.cfg"
```

- запустить container в test
```bash
ansible-playbook ansible/run_test.yml -e target_host=local
```

ansible standart vars

```yaml
{{ ansible_ssh_host }}
{{ ansible_fqdn }}
```
```yaml
ansible-lint -x var-naming,fqcn-builtins,no-changed-when,risky-shell-pipe,risky-file-permissions -vvv
```

- 
- start_<ENV>.yml

для сборки docker image 

про чувствительные данные для SQLALCHEMY

password:
```bash
@ - %40
# - %23
```

Для первого тестирования реализации FastAPI был использован материал с 
https://testdriven.io/blog/fastapi-crud/
это notes
```
db.py - описание схем DB
main.py - описание роутов
notes.py - описание handlers
models.py - описание моделей схем! (пока не понял что это такое)
```

ansible
**MacOS**
```
brew install ansible
brew install ansible-linter

ansible-lint -x var-naming,fqcn-builtins,no-changed-when,risky-shell-pipe,risky-file-permissions ansible -vvv
```

**git**
```
git reflog
git log
```

**Немного про pip**

иногда нужно зачистить pip от текущих библиотек
для этого необходимо сначала сделать выгрузку всех актуальных
а потом по этому списку uninstall
```
pip freeze > requirements-all.txt
pip uninstall -y -r requirements-all.txt
```
чтобы он стал чистеньким
```
pip list                                
Package    Version
---------- -------
pip        21.1.2
setuptools 57.0.0
wheel      0.36.2
```

Активируем миграции
```
alembic init migrations
```
появляется подпапка migrations

в появившейся папке находим файл script.py.mako и добавляем
```
import sqlmodel
```
далее в файл env.py добавляем
```
from sqlmodel import SQLModel
from app2.api.models.gems import *
from app2.api.models.users import *
```
и меняем
target_metadata = false
на
target_metadata = SQLModel.metadata

далее необходимо втащить значение URL подключения к БД
предположим что оно у нас будет подбираться из ENV
снова редактируем env.py
```
def get_url():
    url = os.environ.get("SQLALCHEMY_DATABASE_URI")
    return url
```
далее
```
    url = get_url()
    context.configure(
        url=url,
```
и еще
```
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    connectable = engine_from_config(
        configuration,
```
выполняем команду по инициализации первой ревизии
```
alembic revision --autogenerate -m "init"

alembic upgrade head
```

добавляем render_as_batch=True

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"}, render_as_batch=True
    )


        context.configure(
            connection=connection, target_metadata=target_metadata, render_as_batch=True
        )


запуск ansible playbook на удаленном хосте

если пароль вводить самостоятельно

ansible -i inventory example -m ping -u <your_user_name> --ask-pass

если пароль передать как переменную

read -s PASS
ansible windows -i hosts -m win_ping -e "ansible_password=$PASS"