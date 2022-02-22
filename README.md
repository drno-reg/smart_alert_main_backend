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

Посмотреть логи docker контейнера в реальном времени
```bash
docker logs -f --tail 10 smart_alert_main_backend_local
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

- 
- start_<ENV>.yml

для сборки docker image 

про чувствительные данные для SQLALCHEMY

password:
```bash
@ - %40
# - %23
```

