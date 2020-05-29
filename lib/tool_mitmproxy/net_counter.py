# run: mitmdump -s script <saveurl.py> -p 8081

from mitmproxy.script import concurrent
import json, datetime
from sqlalchemy.databases import mysql
from sqlalchemy import Column, create_engine, Integer, Text, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Proxy(Base):
    __tablename__ = 'Proxy'
    id = Column(Integer, primary_key=True, autoincrement=True)
    str = Column(mysql.MSMediumText)
    time = Column(DateTime, default=datetime.datetime.utcnow)


engine = create_engine('mysql+pymysql://root:root@192.168.10.15:3306/test')
DBSession = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
session = DBSession()

result = {}


@concurrent
def request(flow):
    domain = flow.request.host
    method = flow.request.method
    result['scheme'] = flow.request.scheme
    result['request_headers'] = {}
    for item in flow.request.headers:
        result['request_headers'][item] = flow.request.headers[item]
    url_path = flow.request.path
    result['get_data'] = parser_data(flow.request.query)

    result['post_data'] = parser_data(flow.request.urlencoded_form)  #


@concurrent
def response(flow):
    status_code = flow.response.status_code
    result['response_headers'] = {}
    for item in flow.response.headers:
        result['response_headers'][item] = flow.response.headers[item]
    result['response_content'] = flow.response.get_text()
    result_json = json.dumps(result)
    # print(result_json)

    # 插入数据库
    new_url = Proxy(str=result_json)
    session.add(new_url)
    session.commit()
    # 关闭session:
    # session.close()


def parser_data(query):
    data = {}
    for key, value in query.items():
        data[key] = value
    return data
