#! python2
# -*- coding: utf-8 -*-

from fabric.api import env, run
from fabric.operations import sudo


# 远程库地址
GIT_REPO = "https://github.com/pengguangxing/django-blog.git"

# 远程登录的用户名和密码
env.user = 'pgx'
env.password = 'pgX5967973'

# 主机对应的域名
env.hosts = ['www.pengguangxing.top']

# 端口号
env.port = '22'


def deploy():
    # 资源目录
    source_folder = '/home/pgx/sites/www.pengguangxing.top/django-blog'
    # 打开资源目录从远程库拉取代码（2条命名中间用&&连接）
    run('cd %s && git pull' % source_folder)
    # 虚拟环境下安装依赖库；收集静态文件；数据库迁移
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    # 重启gunicorn和nginx.两条命令要在超级权限下运行所以用了sudo
    sudo('restart gunicorn-www.pengguangxing.top')
    sudo('service nginx reload')


