FROM debian:bullseye

RUN apt-get update && \
    apt-get install -y postfix && \
    apt-get clean

COPY main.cf /etc/postfix/main.cf

CMD ["/usr/sbin/postfix", "start-fg"]