FROM ubuntu:trusty
MAINTAINER niusmallnan <zhangzb@neunn.com>

# Replace default source list with 163 and update
RUN rm -f /etc/apt/sources.list.d/proposed.list
RUN echo 'deb http://mirrors.aliyun.com/ubuntu/ trusty main multiverse restricted universe' > /etc/apt/sources.list
RUN echo 'deb http://mirrors.aliyun.com/ubuntu/ trusty-security main multiverse restricted universe' >> /etc/apt/sources.list
RUN echo 'deb http://mirrors.aliyun.com/ubuntu/ trusty-updates main multiverse restricted universe' >> /etc/apt/sources.list
RUN apt-get -y update 

# Install packages required
RUN apt-get -y install build-essential  \
			autoconf \ 
			automake \ 
			flex \
			bison \
			python-dev \
			zlib1g-dev \
			libxslt-dev \
			git  \
			curl \
			vim \
			python-eventlet \
			python-mysqldb \
			python-amqp \
			tmux \
                        cron \
                        python-pip

RUN mkdir -p /root/.pip
ADD pip.conf /root/.pip/pip.conf

# Copy configs to container
add set_ssh.sh /set_ssh.sh
add set_ostf.sh /set_ostf.sh
add run.sh /run.sh
RUN chmod +x /*.sh
RUN /set_ostf.sh

ENV PROCESS_NAME neunn_ostf

# expose ostf port
EXPOSE 8777 22

CMD /run.sh
