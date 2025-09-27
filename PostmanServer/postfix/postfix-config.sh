#!/bin/bash

echo "postfix postfix/mailname string mail.local" | debconf-set-selections
echo "postfix postfix/main_mailer_type string 'Local only'" | debconf-set-selections

DEBIAN_FRONTEND=noninteractive apt-get install -y postfix

# main.cf に最低限の設定を追加
postconf -e "myhostname = mail.local"
postconf -e "mydestination = $myhostname, localhost.localdomain, localhost"
postconf -e "inet_interfaces = all"
postconf -e "inet_protocols = ipv4"
postconf -e "alias_maps = hash:/etc/aliases"
postconf -e "alias_database = hash:/etc/aliases"
postconf -e "local_recipient_maps ="