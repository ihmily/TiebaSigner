# TiebaSigner
百度贴吧一键签到脚本，已稳定运行两年



## 使用说明

#### 源码运行

1.进入项目文件夹

```
cd TiebaSigner
```

2.安装依赖

```
pip install -r requirements.txt
```

3.运行

```
python tieba_sign.py
```



#### Docker运行

1.进入项目文件夹

```
cd TiebaSigner
```

2.构建镜像

```
docker build -t tieba-sign .
```

3.运行

```
docker run tieba-sign
```

如果不想自己构建镜像。可以跳过第二步，然后直接拉取我的docker仓库镜像 ，执行

```
docker pull ihmily/tieba-sign:latest
```

最后运行

```
docker run ihmily/tieba-sign:latest
```



#### 定时运行

1.你可以使用 crontab 来设置定时任务，例如：

```
# 打开当前用户的定时任务编辑器
crontab -e
```

2.然后在编辑器中添加一行类似于下面的内容，以在每天的固定时间执行签到脚本：

```
0 8 * * * python3 /path/to/tieba_sign.py
```

在这个示例中，`0 8 * * *` 表示在每天的上午8点执行，`/app/tieba_sign.py` 是签到脚本在容器中的路径。

3.如果使用的是docker运行，则执行

```
0 8 * * * docker start -a <container_id_or_name>
```

注意，`<container_id_or_name>` 要替换成你的容器ID或者容器名（你可以使用 `docker ps` 命令查看）

设置完毕后，保存并退出编辑器，定时任务将会生效。每天的指定时间，该定时任务都会自动执行容器中的签到脚本。

***

