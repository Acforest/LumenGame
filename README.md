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