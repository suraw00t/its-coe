FROM debian:sid
RUN echo 'deb http://mirror.psu.ac.th/debian/ sid main contrib non-free non-free-firmware' > /etc/apt/sources.list
RUN apt update && apt install -y python3 python3-venv python3-pip locales

ENV TZ="Asis/Bangkok"
RUN date
RUN sed -i '/th_TH.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
RUN python3 -m venv /venv
RUN export PYTHONPATH="${PYTHONPATH}:/venv/bin

WORKDIR /app

EXPOSE 8086

COPY . /app
