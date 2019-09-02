# Python Scrapy Crawl 糗事百科
（此项目仅供个人学习使用）
## 安装

### 安装Python

至少Python3.5以上

### 安装MongoDB/Mysql

安装好之后将Mongodb服务开启

### 配置mongodb/Mysql连接参数

进入sp_qsbk目录，修改settings.py文件
```
MONGO_URI = 'mongodb://127.0.0.1:27017'
MONGO_DB = 'SpQsbk'
```
```
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_DB_NAME = 'SPQSBK_DB'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'your password'
```

#### 安装依赖

```
pip3 install -r requirements.txt
```

#### 运行

```
python3 cmd_start.py
```
(注：此项目目前性能尚未测试与优化)<br>
该网站的反爬机制有：
- 点击滑块验证
- 封ip（response返回403状态码(即服务器禁止访问)）
