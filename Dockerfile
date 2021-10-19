FROM registry.cn-hangzhou.aliyuncs.com/liyu_os/automation:v2
WORKDIR /root/automation/
COPY . /root/automation/
RUN python execute_test.py
