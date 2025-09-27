FROM debian:bullseye

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y postfix mailutils rsyslog curl && \
    apt-get clean

# Postfix 設定
COPY postfix-config.sh /postfix-config.sh
RUN chmod +x /postfix-config.sh && /postfix-config.sh

# スクリプトと aliases 設定
RUN useradd -m mailbot
COPY receive_mail.py /home/mailbot/receive_mail.py
RUN chmod +x /home/mailbot/receive_mail.py && \
    echo 'mailbot: "|/home/mailbot/receive_mail.py"' >> /etc/aliases && newaliases

# 起動スクリプト（Postfix + syslog 両方）
CMD ["sh", "-c", "service rsyslog start && service postfix start && tail -F /var/log/mail.log"]
