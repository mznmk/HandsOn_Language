# [ base image ]
FROM    --platform=linux/x86_64 node:10.15.1

# [ system update ]
# [ install application ]
RUN     apt-get update; \
        apt-get install -y locales; \
        apt-get install -y vim;

# [ set system environment ]
RUN     locale-gen ja_JP.UTF-8
RUN     localedef -f UTF-8 -i ja_JP ja_JP
ENV     LANG ja_JP.UTF-8
ENV     TZ Asia/Tokyo

# [ set user environment ]
WORKDIR /node
USER    node