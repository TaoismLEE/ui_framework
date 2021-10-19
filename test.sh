#!/bin/bash
#remove legacy image
docker image ls | grep ' v3 '
if [ $? -eq 0 ]; then
	docker image rm -f `docker image ls  | grep ' v3 ' | awk '{print $3}'`
fi

#move to /root folder and clone newest script
cd /root
if [ -d /root/New_Credit ]; then
	rm -rf /root/New_Credit
fi
git clone https://github.com/TaoismLEE/New_Credit.git	
if [ $? -eq 0 ]; then
	cd /root/New_Credit/
fi

#build image
docker build -t automation:v3 .

#remove running container
docker container ls -a |grep 'autoscript'
if [ $? -eq 0 ]; then
	docker container stop `docker container ls -a |grep 'autoscript'|awk '{print $1}'`
	echo "removing automation container!"
	docker container rm -f `docker container ls -a |grep 'autoscript'|awk '{print $1}'`
fi
