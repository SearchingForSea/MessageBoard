[toc]

# About the repo
 Django + DRF + Vuejs `(vue-cli project)` project.


# 使用流程
开始使用容器:
  - `docker-compose up -d`
  - `docker-compose up`

Django建表:
  - `docker-compose run backend migrate`

Docker Createsuperuser:
  - `docker-compose run backend createsuperuser`



# 目录结构

  - 文件 `docker-compose.yml`: containers settings
  - 目录 `dockerfiles`: 
    -  `backend`: Django + DRF
    -  `vuejs`: Vuejs + Webpack + NPM ==
    -  `nginx`: 即nginx相关
  - 文件 `Pipfile` 和 `Pipfile.lock`: [Pipenv](https://pipenv.readthedocs.io/en/latest/) 文件
  - 目录 `src`:
    - 目录 `backend`: Django + DRF project.
    - 目录 `frontend`: Vuejs webpack project.   
   - 目录 `nginx`:
    - 文件 `backend.conf`: 转发8000端口.
    - 文件 `frontend_develop`: 转发8080端口.
    - 文件 `frontend_production`: 挂载`npm run build`的文件.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         z

# 关于后端


## Django 相关

  > Question:  如何运行`manage.py` 相关指令
  - Answer: 

    `docker-compose run backend <any manage.py option >`

    如 你想运行 `manage.py` help, 则应该输入

    `docker-compose run backend help`

   类似的

  `docker-compose run backend showmigrations`

   `python manage.py shell` =>  
    `docker-compose run backend shell`

  > Question: 如何运行 `django-admin`相关指令 
  - Answer: 

    同上, `docker-compose run backend django-admin <options>`

