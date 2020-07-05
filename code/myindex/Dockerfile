FROM python:3.7
ADD app.py /
COPY  templates /templates
ADD requirements.txt /
RUN pip3 install --trusted-host https://mirrors.aliyun.com/pypi/simple/  -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
EXPOSE 5001
ENTRYPOINT ["./app.py"]

