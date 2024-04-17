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

如果不想自己构建或者这里也可以直接拉取我的docker仓库镜像 ，执行

```
docker pull ihmily/tieba-sign:latest
```

然后运行

```
docker run ihmily/tieba-sign:latest
```

