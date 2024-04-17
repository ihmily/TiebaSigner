# TiebaSigner

百度贴吧一键签到脚本，已稳定运行两年



## 使用说明

#### 拉取代码

使用命令或者手动下载仓库代码

```
git clone https://github.com/ihmily/TiebaSigner.git
```

进入项目文件夹

```
cd TiebaSigner
```



#### 源码运行

1.获取百度贴吧登录后的cookie，将其填入cookie.json文件中。

2.安装依赖

```
pip install -r requirements.txt
```

3.运行

```
python tieba_sign.py
```



#### Docker运行

第一种方式：

1.获取你登录百度账号后的cookie，填入cookie.json文件中

2.构建镜像，进入项目文件夹并执行

```
docker build -t tieba-sign .
```

3.运行

```
docker run tieba-sign
```

&emsp;

第二种方式：

1.如果不想自己构建镜像，也可以直接拉取我的docker仓库镜像 ，执行

```
docker pull ihmily/tieba-sign:latest
```

2.修改cookie.json文件，填入你登录百度账号后的cookie

3.然后运行

```
docker run -v /path/to/cookie.json:/app/cookie.json ihmily/tieba-sign:latest
```

其中 `/path/to/cookie.json` 替换为你服务器上cookie.json文件的正确路径（**注意需要绝对路径**）

第一次执行成功后，使用下面命令查询刚创建的容器ID或者容器名

```
docker ps -a
```

之后运行脚本都使用下面的命令

```
docker start -a 容器ID或者容器名称
```

如果每次使用`docker run` 执行，每次都会创建新的容器，占用额外的空间。

&emsp;

#### 定时运行

1.你可以使用 crontab 来设置定时任务，例如：

```
# 打开当前用户的定时任务编辑器
crontab -e
```

2.然后在编辑器中添加一行类似于下面的内容，以在每天的固定时间执行签到脚本：

如果有python环境并且使用源码能正常运行，则填写

```
0 8 * * * python3 /path/to/tieba_sign.py
```

在这个示例中，`0 8 * * *` 表示在每天的上午8点执行，`/path/to/tieba_sign.py` 是签到脚本在服务器中的路径。

&emsp;

如果使用的是docker运行，那么应该填写下面内容

```
0 8 * * * docker start -a <container_id_or_name>
```

注意，`<container_id_or_name>` 要替换成你的容器ID或者容器名（你可以使用 `docker ps` 命令查看）

设置完毕后，保存并退出编辑器，定时任务将会生效。每天的指定时间，该定时任务都会自动执行容器中的签到脚本。

***
