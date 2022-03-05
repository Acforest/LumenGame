# LumenGame
## 开发环境搭建
### 前端 (Vue + Element UI)
在 `LumenGame_Frontend` 目录下使用命令行安装和启动服务:
```bash
npm install
npm run serve
```
### 后端 (Django)
先激活安装有 Django 和相关组件的环境，如果未安装，可以使用 Anaconda 创建虚拟环境并安装:
```bash
conda create -n django_env
conda activate django_env
pip install django
pip install django-cors-headers
```
然后在 `LumenGame_Backend` 目录下使用命令行:
```bash
python manage.py runserver 127.0.0.1:8080
```

## 生产环境搭建 (待补充)
### 前端 (Vue + Element UI)
在 `LumenGame_Frontend` 目录下使用命令行打包静态文件:
```bash
npm run build
```
然后将生成的 `static` 文件夹拷贝至 `LumenGame_Backend` 目录下，`index.html` 和 `favicon.ico` 文件拷贝至 `LumenGame_Backend/templates` 目录下。
### 后端 (Django)
待补充
### 代理服务器 (Nginx)
待补充

### 数据库
将`sql`文件夹中的`game_info.sql`，`recommend1.sql`，`recommend1.sql`，`reposity.sql`,`user.sql`导入数据库。
修改`/LumenGame_Backend/LumenGame_Backend/settings.py`中的数据库配置。
在`LumenGame_Backend`目录下输入命令
```bash
python manage.py inspectdb > models.py
```
将`LumenGame_Backend`目录下新生成的`models.py`中的model替换或添加到`/LumenGame_Backend/api/models.py`中的model。
将`meta class`中的`managed ＝ False`修改为True(user可以不导入，将账号密码数据迁移到auth_user即可)。
删除新生成的models.py，输入如下命令。
```bash
python manage.py migrate
```


