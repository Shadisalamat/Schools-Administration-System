Schools-Administration-System (SAS)

Django

1- cd django

2- pip install django

3- py manage.py runserver // run server django


----
=======
Vue js
1- cd vue/cli

2- npm install package.json
>>>>>>> upstream/master

3- npm run serve // run server vue

Test - Alaa-sw
------------------------------ sohep
17.09.2019

git clone https://github.com/Alaa-sw/Schools-Administration-System.git

git pull --rebase

git status

git add .

git commit -m "note"

git push

Installing Git

Linux openSu?e leap 2015

sudo -i

mkdir demoproject

chmod -R 777 demoproject

cd demoproject

zypper install git-core git

git --version

Create your identity First, you need to set your user name and email address with git. This is very important as every Git commits you made uses this information.

git config --global user.name "Alaa Alswedan"

git config --global user.email swedan.alaa@gmail.com

install python3 python3-pip

python3 -V

pip3 -V

pip3 install Django

django-admin --version

cd /var/www

django-admin startproject django_app

cd django_app

python3 manage.py migrate

python3 manage.py createsuperuser

vi django_app/settings.py

ALLOWED_HOSTS = ['192.168.1.239']

python3 manage.py runserver 192.168.1.239:8000

------------------------------------
install npm
node -v

npm -v

npm i -g @vue/cli

vue create vue


$ cd vue

$ npm run serve

vue ui

http://linux-dak6:8080/

---------------------------------
kill Process windows:

netstat -ano | findstr 127.0.0.1

taskkill /F /PID 1596
--------------------------
quide  to change the repo 
1- fork from https://github.com/sohepalslamat/Schools-Administration-System.git
2- creat folder 
3- git clone  https://github.com/sohepalslamat/Schools-Administration-System.git
4- go to Visual Studio Code 
5-open Terminal  
###6-7 only one time ! 
6-  git remote add  origin https://github.com/Shadisalamat/Schools-Administration-System-master
7 - git remote add   upstream        https://github.com/sohepalslamat/Schools-Administration-System.git
##### change what do you want and add the changes to stages  .......
6- git add .
7- git commit -m "Hallo this is my changes "
8- git push orgin master 
9-pull request to Remote (go to your github  ---> choose commit ---> pull request ---> send !!! )
-----------------------------------------------------------
############# get updates from remote repo ############################
######ps ::: download files to local projects --->  you need to merge the changes with merge .....
1-  git  fetch upstram master
2-  git  merge upstream\master ###  if there is a conflict ---> you need to fix the Conflict manually .!!! 
3- git push origin master 
##############################
