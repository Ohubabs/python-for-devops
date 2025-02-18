#! /bin/bash
sudo adduser python
sudo echo "python ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/python
sudo su - python
sudo hostnamectl set-hostname python
sudo timedatectl set-timezone America/Los_Angeles
sudo chown python:python -R /etc/ssh/sshd_config
sudo sed -i "/^[^#]*PasswordAuthentication[[:space:]]no/c\PasswordAuthentication yes" /etc/ssh/sshd_config
sudo service sshd restart
sudo apt update
sudo apt install python3-pip
