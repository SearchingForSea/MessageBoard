[toc]

# About the repo
 Django + DRF + Vuejs `(vue-cli project)` project.


# 使用流程
开始使用容器:
  - `docker-compose up (--build)`

如果你遇到vue-cli错误, 可以尝试`cd src/frontend/ && npm install @vue/cli` 后重新运行

Django建表:
  - `docker-compose run backend migrate`

Docker Createsuperuser:
  - `docker-compose run backend createsuperuser`



# 目录结构

  - 文件 `docker-compose.yml`: containers settings
  - 目录 `dockerfiles`: 
    -  `backend`: Django + DRF
    -  `vuejs`: Vuejs + Webpack + NPM ==
  - 文件 `Pipfile` 和 `Pipfile.lock`: [Pipenv](https://pipenv.readthedocs.io/en/latest/) 文件
  - 目录 `src`:
    - 目录 `backend`: Django + DRF project.
    - 目录 `frontend`: Vuejs project.

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


# 关于前端

## (可选) 本地安装 `vue-cli` 

  前端用docker是一个不明智的选择, 用`npm`或`yarn`显然会更快更方便, 虽然本部分是可选, 但是还是推荐大家本地安装.  
    `npm install -g @vue/cli`  
    `npm install -g @vue/cli-init`
