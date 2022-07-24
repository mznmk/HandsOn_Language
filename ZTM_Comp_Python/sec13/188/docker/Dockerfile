# [ base image ]
FROM    --platform=linux/x86_64 python:3

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

# [ update python module ]
RUN     pip install --upgrade pip;
# [ install python module ]
RUN     pip install translate

# [ set user environment ]
WORKDIR /projects
# USER    node