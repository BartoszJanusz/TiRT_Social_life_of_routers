FROM tiagopeixoto/graph-tool
RUN pacman -S --noconfirm imagemagick vim
VOLUME /root/home
WORKDIR /root/home/data
