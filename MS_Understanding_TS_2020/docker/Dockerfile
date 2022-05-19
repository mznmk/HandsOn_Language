# [ base image ]
FROM    node:16.15.0

# [ system update ]
# [ install application ]
RUN     apt-get update; \
        apt-get upgarade; \
        apt-get install -y locales; \
        apt-get install -y vim less;
RUN     npm install -g npm typescript

# [ set system environment ]
RUN     locale-gen ja_JP.UTF-8
RUN     localedef -f UTF-8 -i ja_JP ja_JP
ENV     LANG ja_JP.UTF-8
ENV     TZ Asia/Tokyo

# [ set user environment ]
WORKDIR /projects
USER    node