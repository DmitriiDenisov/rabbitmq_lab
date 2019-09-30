# rabbitmq_lab

Laboratory based on https://www.rabbitmq.com/getstarted.html

Repository contains 6 labs:

<p align="center"> 
<img src="https://i.ibb.co/983ZTHS/Screen-Shot-2019-07-03-at-22-34-42.png?style=centerme">
</p>


And also lab 'tutorial_new' which shows an example with connect from another machine from the same network 


## Install RabbitMQ

Instructions: https://tecadmin.net/install-rabbitmq-server-on-ubuntu/

Default port of RabbitMQ: 15672. I.e full url would be http://localhost:15672/

if you don’t connect to Rabbit from localhost: ```http://[your droplet’s IP]:15672/``` then you have to create a user, instructions:
https://danielpdev.io/get-started-with-rabbitmq-using-reactjs

## Commands
```rabbitmqctl stop ``` - stops RabbitMQ instance

```rabbitmq-server start -detached``` - start and detach

```rabbitmq-server``` - runs RabbitMQ instance

```rabbitmq-server status``` - check if it is already started 

```sudo rabbitmqctl status``` - Get port where rabbitmq is listening. Then see {listeners,...{http 	15672,"::"}...}

```vi /etc/rabbitmq/rabbitmq-env.conf``` - If nothing is there then port is 15672

## Google Cloud open port
In order to open RabbitMQ's web interface you need to open port.
Instructions how to do that:
https://www.youtube.com/watch?v=JmjqPpQdtW8
After doing it Rabbit will be availible by link: http://<external_IP>:15672/ (for example http://35.190.166.28:15672/)

## Static IP on Google Cloud:
Instructions: https://www.youtube.com/watch?v=E6T8iVKSiZo
