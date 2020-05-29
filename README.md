### 运行爬虫
- 本地测试
```sh
scrapy crawl <spider_name>
```
- 线上运行
```
nohup python3 run.py > logs/log 2>&1 &
```

- kill掉所有python程序
```sh
ps -ef | grep python3 | grep -v grep | awk '{ print $2}'|xargs kill -9
```

### Splash解析服务
- http://47.101.37.196:8050/

### mysql最大连接数
- [pymysql.err.OperationalError: (1040, 'Too many connections')](https://www.jianshu.com/p/f682d5e7bc96)
1. 查看myqsl连接数
```sql
show variables like '%max_connections%';
```
2. 临时修改
```sql
set global max_connections=500;
```
3. 修改启动配置
```sh
vim /etc/my.cnf

set-variable=max_connections=800

/etc/init.d/mysqld restart
```


### 数据比对问题
- 1、11x5的基本走势错误 (广东11x5)    ok
- 2、11x5的和值数据错误     ok
- 3、k3奇偶走势 数据错误     ok
- 4、k3基本走势 数据错误     ok
- 5、北京快乐8 五行数据错误  ok
- 6、甘肃快3没出数据 内蒙古快3没出数据  开彩在十点以后没问题  ok
- 7、新疆时时彩没有数据 和上海11选5一样 开奖时间跨越0点，解决方案就是指定爬取今明两天的数据      ok
- 8、k3 江苏快3定位走势第二个号码|第三个号码 以及大小单双数据有问题  ok
- 9、重庆幸运农场开奖号码有问题 ok        去数据库查询清理掉脏数据
- 10、重庆幸运农场大小走势的大小比&单双走势的单双比有问题     ok      清理数据库脏数据
- 11、十一运夺金&十一选5 龙虎走势的第五球数据      ok
- 12、十一运夺金&十一选5 龙虎走势的龙虎数据错误     ok


### 报错集锦
- `pymysql.err.OperationalError: (1213, 'Deadlock found when trying to get lock; try restarting transaction')`
- `mysql报错：2003, "Can't connect to MySQL server on ' ' [Errno 99] Cannot assign requested address`
    - [[Errno 99] Cannot assign requested address](https://blog.csdn.net/hty46565/article/details/103499739)

- `pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '192.168.10.15' ([WinError 10048] 通常每个套接字地址(协议/网络地址/端口)只允许使用一次。)")`
    - [解决mysql 10048 错误](https://blog.csdn.net/qq_22520587/article/details/62454317)




### 动态的给url拼接指定日期
由于内存机制，定义的爬虫类属性，在程序运行/重启时的日期值被缓存到内存中，不会动态的改变。
解决方案：
1. reload()  重新加载模块以刷新缓存；
2. 重写start_requests()方法，format()动态的拼接url封装成scrapy.Request对象给scrapy调度器处理。例如：
```python
def start_requests(self):
    """
    重写start_requests()方法
    动态的指定爬取日期
    :return:
    """
    # for url in self.start_urls[1:]:
    for url in self.start_urls:
        yield scrapy.Request(   # 直接给scrapy调度器处理
            url=url.format(datetime.datetime.today().strftime('%Y-%m-%d')),
            callback=self.parse
        )
```


### 参考文献
- [pip更换国内源](https://blog.csdn.net/chenghuikai/article/details/55258957)
- [子线程调用scrapy报ReactorNotRestartable的错误](https://www.cnblogs.com/WalkOnMars/p/11934535.html)
- [Splash服务&&scrapy-splash](https://blog.csdn.net/Lijuhao_blog/article/details/89070929)
- 手机模拟器中App&&微信小程序的抓包
    - [使用charls抓包微信小程序](https://www.cnblogs.com/macliu/p/11379480.html)
    - [APP 抓包和微信小程序抓包-Charles](https://blog.csdn.net/liqing0013/article/details/83010531)
- [基于网易邮箱、哔哩哔哩、csdn、豆瓣、脸书、京东、拉钩、链家、猎聘、qq空间、淘宝、推特、微信、知乎的爬虫](https://github.com/jackgithup/mainWebsitesProject)
- [python scrapy 修改时间统计信息源码](https://blog.csdn.net/qq_27648991/article/details/83501625)
- [线程中调用scrapy报ReactorNotRestartable的错误](https://www.cnblogs.com/WalkOnMars/p/11934535.html)
- 调用DecryptLogin库请求登陆访问
    - [参考博客](https://blog.csdn.net/qq_45414559/article/details/106005684?utm_medium=distribute.pc_category.none-task-blog-hot-12.nonecase&depth_1-utm_source=distribute.pc_category.none-task-blog-hot-12.nonecase&request_id=)
    - [官方文档](https://httpsgithubcomcharlespikachudecryptlogin.readthedocs.io/zh/latest/INSTALL.html)
- mitmproxy
    - [官方文档](https://mitmproxy.readthedocs.io/en/v2.0.2/scripting/api.html)
- httpbin.org
    - [官方文档](http://httpbin.org/)
    - 参考博客
        - [httpbin.org的使用](https://blog.csdn.net/Hubz131/article/details/89157089)
        - [HttpBin 介绍](https://www.quchao.net/httpbin.html)
- APP抓包，针对SSL-Pinning反爬
    - [VirtualXposed+justtrustme下载安装](https://www.cnblogs.com/junjunzhazha/p/10444702.html)
    - [xposed+justTrustme介绍与使用](https://blog.csdn.net/u011215939/article/details/95461286)
    - [VirtualXposed 免ROOT使用Xposed模块](https://blog.csdn.net/qq_37486616/article/details/90409094)
- [Scrapy中间件详解](https://www.cnblogs.com/fengf233/p/11453375.html)
- [python多线程执行类中的静态方法](https://www.cnblogs.com/dasheng-maritime/p/8365409.html)
- [HTML5优质模版网站](http://html5up.net/)