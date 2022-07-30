[toc]

# About the repo

 Django + DRF + Vuejs `(vue-cli project)` project.

# 使用流程

**第一次**使用容器编排启动前后端:

- `docker-compose up --build`

> 备注：如果在上述过程中，有前端 `vue-cli` 相关的报错，请在宿主机（也就是容器外）进入 `frontend` 目录，执行 `yarn install`（需要确保你自己本地已经装了 `yarn`）。之后再重复上面的步骤。

**之后**使用容器编排启动前后端:

- `docker-compose up`


Django建表:

- `docker-compose run backend migrate`

Docker `createsuperuser`:

- `docker exec -ti <对应container id> /bin/bash` 后 `django-admin createsuperuser`即可, container id 可以在用`docker ps`查询

添加如下的三行信息到 `hosts` 文件的最下面——一般对于 Linux 或 MacOS 这个文件在在 `/etc/hosts`，Windows 在 `C:\Windows\System32\drivers\etc\hosts`。

```text
127.0.0.1 frontend.docker.io
127.0.0.1 backend.docker.io
127.0.0.1 production.docker.io
```

# 目录结构

- 文件 `docker-compose.yml`: 编排容器的配置描述
- 目录 `dockerfiles`:
  - `backend`: Django + DRF
  - `vuejs`: Vuejs + Webpack + NPM 等
  - `nginx`: 即 Nginx 相关的配置
- 文件 `Pipfile` 和 `Pipfile.lock`: [Pipenv](https://pipenv.readthedocs.io/en/latest/) 文件
- 目录 `src`:
  - 目录 `backend`: Django + DRF project.
  - 目录 `frontend`: Vuejs webpack project.
- 目录 `nginx`:
- 文件 `backend.conf`: 转发8002端口.  
- 文件 `frontend_develop`: 转发8080端口.  
- 文件 `frontend_production`: 挂载`npm run build`的文件.  

# 关于后端

## Django 相关

  **Question:  如何运行`manage.py` 相关指令**
  
  **Answer:**

   `docker-compose run backend <any manage.py option >`
  
   如你想运行 `manage.py` help, 则应该输入
  
   `docker-compose run backend help`
  
   类似地，
  
   - `docker-compose run backend showmigrations`
   - `python manage.py shell` =>  `docker-compose run backend shell`
  
  **Question: 如何运行 `django-admin`相关指令**
  
  **Answer:**

   同上, `docker-compose run backend django-admin <options>`
