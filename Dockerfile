FROM ubuntu/bind9:latest
WORKDIR /LandingNetwork
COPY . .
ENV robot version
CMD [ "python3", "LandingNetwork" ]