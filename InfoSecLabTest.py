#!/usr/bin/python3
import os
import sys
import time


f = open('banner.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()
PHP_V=sys.argv[1]


print("Step 1: Install apache")
os.system("sudo apt-get install unzip")
#print("[+] Update your local package : ")
#os.system("sudo apt update")
print("[+] Install the apache2 package:")
os.system("sudo apt-get install apache2 -y")
print("[+] Enable its rewrite module, and restart the service :")
os.system("sudo a2enmod rewrite && systemctl restart apache2")
print("[+] Step 2 - Adjusting the Firewall ")
os.system("sudo ufw app list")
os.system("sudo ufw allow 'Apache'")
os.system("sudo ufw status")
#-----------------------------------------------------------#
print("-------------------------------------------------------")
print("[+] Step 3 - Checking your Web Server")
os.system("sudo systemctl status apache2 --no-pager")
print("[+] Step 4 - Setting Up Virtual Hosts (Recommended)")
print("[+] Assign ownership of the directory:")
os.system("sudo chown -R $USER:$USER /var/www/")
print("[+] The permissions of your web")
os.system("sudo chmod -R 755 /var/www/")
print("[+] Disable the default site defined in 000-default.conf:")
os.system("sudo a2dissite 000-default.conf")
print("[+] Test for configuration errors: ")
os.system("sudo apache2ctl configtest ")
print("[+] Restart Apache to implement your changes:")
os.system("sudo systemctl reload apache2 ")
#-----------------------------------------------------------#
print("-------------------------------------------------------")


print("Step 5: Install MySQL")
os.system("sudo apt-get install mysql-server php-mysql -y")
print("-------------------------------------------------------")
print("This steps for Kali linux")
os.system("sudo ls -lart /var/run/my")
os.system("sudo mkdir /var/run/mysqld")
os.system("sudo touch /var/run/mysqld/.sock")
os.system("sudo chown -R mysql /var/run/mysqld/")
os.system("sudo /etc/init.d/mysql restart")


print("Step 6: Install php")
# for dvwa
os.system("sudo apt-get install php7.2-curl php7.2-mbstring php7.2-xml -y")
os.system("sudo apt-get install php7.3-curl php7.3-mbstring php7.3-xml -y")
os.system("sudo apt-get install php php-mysqli php-gd libapache2-mod-php -y")
print("-------------------------------------------------------")
print("Step 7: Install python")
os.system("sudo apt-get install python3 -y")
os.system("sudo apt-get install python3-pip -y")

os.system("sudo apt-get install python3-mysqldb -y")
os.system("pip3 install mysql-connector-python -y")
os.system("sudo pip install MySQL-python -y")
os.system("sudo apt install python3-pip")

os.system("sudo curl https://bootstrap.pypa.io/get-pip.py -o get-pip2.py")
os.system("sudo python get-pip2.py")



os.system("curl -O https://bootstrap.pypa.io/pip/2.7/get-pip.py")
os.system("python get-pip.py")
os.system("python -m pip install --upgrade 'pip < 21.0'")
os.system("sudo apt-get install python-dev default-libmysqlclient-dev -y")


os.system("sudo apt-get install python3-mysqldb -y")
os.system("pip3 install mysql-connector-python -y")
os.system("sudo pip install MySQL-python -y")

os.system("sudo apt install libmariadb3 libmariadb-dev -y")
os.system("sudo apt install mariadb-server -y")
os.system("sudo service mariadb start")
os.system("pip3 install mariadb")
###########mutillidae 

os.system("sudo apt update -y")
os.system("sudo apt install php-xml php-fpm libapache2-mod-php php-mysql php-gd php-imap php-mysql php-curl php-mbstring -y")
os.system("sudo a2enmod proxy_fcgi setenvif")
os.system("sudo systemctl restart apache2")
os.system("sudo a2enconf php7.4-fpm")
os.system("sudo systemctl reload apache2")
os.system("sudo systemctl restart apache2.service")
os.system("sudo service php7.4-fpm restart")
os.system("sudo systemctl restart mysql")
######################
os.system("sudo apt-get install python-mysqldb -y")
os.system("pip3 install mysql-connector-python -y")
os.system("pip install pymysql -y")
os.system("pip3 install mysql-connector-python")
os.system("sudo apt install python3-dev libpython3-dev")
os.system("sudo apt install python3-mysqldb")
os.system("sudo apt-get install libmysqlclient-dev -y")
os.system("sudo -H pip3 install mysqlclient -y")
os.system("sudo apt-get install python3-dev libmysqlclient-dev -y")

os.system("pip install MySQL-python")

print("-------------------------------------------------------")

# allow url include for dvwa
# Read in the file
with open('/etc/php/'+PHP_V+'/apache2/php.ini', 'r') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('allow_url_include = Off', 'allow_url_include = On')

# Write the file out again
with open('/etc/php/'+PHP_V+'/apache2/php.ini', 'w') as file:
    file.write(filedata)
time.sleep(0.5)
print("--------------------------------------------------------")
# allow url include for dvwa
# Read in the file
with open('/etc/php/'+PHP_V+'/apache2/php.ini', 'r') as file:
    filedata = file.read()

# Replace the target string
filedata = filedata.replace('display_errors = Off', 'display_errors = On')

# Write the file out again
with open('/etc/php/'+PHP_V+'/apache2/php.ini', 'w') as file:
    file.write(filedata)
time.sleep(0.5)

print("Restart Apache2...")
os.system("sudo service apache2 restart")
print("-------------------------------------------------------")

print("[+] Now working with the files ")
# unzip files
os.system("sudo unzip file.zip")
time.sleep(0.5)
os.system("sudo unzip bWAPP.zip")
time.sleep(0.5)
os.system("sudo unzip sqli-labs.zip")
time.sleep(0.5)
os.system("sudo unzip hackademic.zip")
time.sleep(0.5)
os.system("sudo unzip dvwa.zip")
time.sleep(0.5)
os.system("sudo rm -r mutillidae2.zip")
os.system("sudo rm -r mutillidae")

os.system("sudo git clone https://github.com/webpwnized/mutillidae")
time.sleep(0.5)
os.system("sudo tar -xzvf xvwa.tar.gz")

os.system("sudo rm -r *.zip  *.gz")
time.sleep(0.5)

print("[+] Create a sample index.html")
time.sleep(0.5)

time.sleep(0.5)
os.system("sudo unzip webTest.zip")
os.system("sudo mv assets index.html cover.css /var/www/html/")
os.system("sudo mv InfoSecLabWeb /var/www/html/")
time.sleep(0.6)


os.system("clear")
f = open('banner.txt', 'r')
file_contents = f.read()
print("file_contents")
f.close()

Wlecome = input("\033[1;38;40m Welcome to InfoSec-HA-lab version 1, This Project is made for testing vulnerabilities, So if are interesting to try it, go ahead and ...Press Enter to Continue... ") 
def sc_list():
    if Wlecome == '':
        f = open('banner.txt', 'r')
        file_contents = f.read()
        # print("\033[1;32;80m-----------------------------------------------------------------------------------------------")
        print("\033[1;32;80m {} \n\n"  .format(file_contents))
        f.close()
        # print("\033[1;32;80m-----------------------------------------------------------------------------------------------")
        print("\033[1;32;80m--------------------[ Database Configuration ]-------------------")
        print("\033[1;34;80m [+] Enter [13] [ for Database Lab Configuration ]               ") 
        print("\033[1;32;80m--------------------[ Download Labs ]----------------------------")
        # print("\033[1;32;80m[?] Chose any number to install specific lab....") 
        print("\033[1;34;80m [+] Enter (1) to Setup     [ bWAPP ]                            ")
        print("\033[1;34;80m [+] Enter (2) to Setup     [ xvwa ]                             ")
        print("\033[1;34;80m [+] Enter (3) to Setup     [ dvwa ]                             ")
        print("\033[1;34;80m [+] Enter (4) to Setup     [ mutillidae ]                       ")
        print("\033[1;34;80m [+] Enter (5) to Setup     [ hackademic ]                       ")
        print("\033[1;34;80m [+] Enter (6) to Setup     [ sqli-labs ]                        ")
        print("\033[1;34;80m [+] Enter (7) to Setup     [ ALL ]                              ")
        print("\033[0;34;80m [+] Enter (14)  to         [ Exit ]                           \n")
# print("\033[1;36;40m Welcome to SecInfo-lab version 1, This Project is made for Practicing Web BenTest.....\n")
x = 1
sc_list()
while x != 0:
    if x <= 20:
        try:
            x = int(input("\033[1;32;40m  [+] Enter The Number of Your Choise : "))
            if x == 1:
                # if os.system("cd ")
                print("Wait for setup { bWAPP }   ")
                time.sleep(0.5)
                os.system("sudo unzip webTest.zip")
                os.system("sudo mv assets index.html cover.css /var/www/html/")
                os.system("sudo mv InfoSecLabWeb /var/www/html/")
                time.sleep(0.5)
                os.system("sudo unzip bWAPP.zip")
                os.system("sudo cp -r bWAPP /var/www/html/InfoSecLabWeb/testLabs")
                os.system("sudo chmod 777 /var/www/html/InfoSecLabWeb/testLabs/bWAPP/passwords/")
                os.system("sudo chmod 777 /var/www/html/InfoSecLabWeb/testLabs/bWAPP/images/")
                os.system("sudo chmod 777 /var/www/html/InfoSecLabWeb/testLabs/bWAPP/documents/")
                # something want ronge mkdir
                # os.system("sudo mkdir /var/www/html/bWAPP/logs/")
                os.system("sudo chmod 777 /var/www/html/InfoSecLabWeb/testLabs/bWAPP/logs/")
                os.system("sudo chown -R www-data:www-data /var/www/html/InfoSecLabWeb/testLabs/bWAPP/")
                time.sleep(2)
                print("\033[1;32;40m Done, The lab bWAPP installed Successfily in current path:/var/www/html/InfoSecLabWeb/testLabs ")
                print("\033[0;32;80m-------------------------------------------------------")
                print("Now you can use your SecInfo-HA-lab..... ")
                print("Go for Opening your Browser IP Machine is = >>  : ")
                os.system("IP=$(ifconfig | grep -i inet | cut -d ' ' -f 10 | head -1);echo [--] http://$IP/index.html")         
                time.sleep(10)
                sc_list()
            elif x == 2: 
                print("Wait for setup { xvwa } ")
                time.sleep(0.5)
                os.system("sudo unzip webTest.zip")
                os.system("sudo mv assets index.html cover.css /var/www/html/")
                os.system("sudo mv InfoSecLabWeb /var/www/html/")
                time.sleep(0.5)
                os.system("sudo tar -xvzfxvwa.tar.gz")
                os.system("sudo unzip webTest.zip")
                os.system("sudo mv assets index.html cover.css /var/www/html/")
                os.system("sudo mv InfoSecLabWeb /var/www/html/")
                time.sleep(0.5)
                os.system("sudo unzip  xvwa.zip")
                os.system("sudo cp -r xvwa /var/www/html/InfoSecLabWeb/testLabs /var/www/html/InfoSecLabWeb/testLabs")
                time.sleep(2)
                print("\033[1;32;40m Done, The lab xvwa installed Successfily in current path:/var/www/html/InfoSecLabWeb/testLabs ")
                print("\033[0;32;80m-------------------------------------------------------")
                print("Now you can use your SecInfo-HA-lab..... ")
                print("Go for Opening your Browser IP Machine is = >>  : ")
                os.system("IP=$(ifconfig | grep -i inet | cut -d ' ' -f 10 | head -1);echo [--] http://$IP/index.html")
                time.sleep(10)
                sc_list()
            elif x == 3:
                print("Wait for setup { dvwa } ")
                time.sleep(0.5)
                os.system("sudo unzip webTest.zip")
                os.system("sudo mv assets index.html cover.css /var/www/html/")
                os.system("sudo mv InfoSecLabWeb /var/www/html/")
                time.sleep(0.5)
                os.system("sudo unzip dvwa.zip")
                os.system("sudo cp -r dvwa /var/www/html/InfoSecLabWeb/testLabs")
                os.system("sudo chmod -R 777 /var/www/html/InfoSecLabWeb/testLabs/dvwa/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt")
                os.system("sudo chmod -R 777 /var/www/html/InfoSecLabWeb/testLabs/dvwa/hackable/uploads")
                os.system("sudo chmod -R 777 /var/www/html/InfoSecLabWeb/testLabs/dvwa/config")
                time.sleep(2)
                print("\033[1;32;40m Done, The lab dvwa installed Successfily in current path:/var/www/html/InfoSecLabWeb/testLabs ")
                print("\033[0;32;80m-------------------------------------------------------")
                print("Now you can use your SecInfo-HA-lab..... ")
                print("Go for Opening your Browser IP Machine is = >>  : ")
                os.system("IP=$(ifconfig | grep -i inet | cut -d ' ' -f 10 | head -1);echo [--] http://$IP/index.html")
                time.sleep(10)
                sc_list()
            elif x == 4:
                print("Wait for setup { mutillidae } ")
                time.sleep(0.5)
                os.system("sudo unzip webTest.zip")
                os.system("sudo mv assets index.html cover.css /var/www/html/")
                os.system("sudo mv InfoSecLabWeb /var/www/html/")
                time.sleep(0.5)
                os.system("sudo unzip mutillidae.zip")
                os.system("sudo cp -r mutillidae /var/www/html/InfoSecLabWeb/testLabs ;sudo chown -R www-data:www-data /var/www/html/InfoSecLabWeb/testLabs/mutillidae/")
                time.sleep(2)
                print("\033[0;32;80m-------------------------------------------------------")
                time.sleep(10)
                sc_list()
            elif x == 5:
                print("Wait for setup  { hackademic } ")
                time.sleep(0.5)
                os.system("sudo unzip webTest.zip")
                os.system("sudo mv assets index.html cover.css /var/www/html/")
                os.system("sudo mv InfoSecLabWeb /var/www/html/")
                time.sleep(0.5)
                os.system("sudo unzip hackademic.zip")
                os.system("sudo cp -r hackademic /var/www/html/InfoSecLabWeb/testLabs/")
                time.sleep(2)
                print("\033[1;32;40m Done, The lab hackademic installed Successfily in current path:/var/www/html/InfoSecLabWeb/testLabs ")
                print("\033[0;32;80m-------------------------------------------------------")
                print("Now you can use your SecInfo-HA-lab..... ")
                print("Go for Opening your Browser IP Machine is = >>  : ")
                os.system("IP=$(ifconfig | grep -i inet | cut -d ' ' -f 10 | head -1);echo [--] http://$IP/index.html")
                time.sleep(10)
                sc_list()
            elif x == 6:
                print("Wait for setup  { sqli-labs } ")
                time.sleep(0.5)
                os.system("sudo unzip webTest.zip")
                os.system("sudo mv assets index.html cover.css /var/www/html/")
                os.system("sudo mv InfoSecLabWeb /var/www/html/")
                time.sleep(0.5)
                os.system("sudo unzip sqli-labs.zip")    
                os.system("sudo cp -r sqli-labs /var/www/html/InfoSecLabWeb/testLabs/")
                time.sleep(3)
                print("\033[1;32;40m Done, The lab sqli-labs installed Successfily in current path:/var/www/html/InfoSecLabWeb/testLabs ")
                print("\033[0;32;80m-------------------------------------------------------")
                
                print("Now you can use your SecInfo-HA-lab..... ")
                print("Go for Opening your Browser IP Machine is = >>  : ")
                os.system("IP=$(ifconfig | grep -i inet | cut -d ' ' -f 10 | head -1);echo [--] http://$IP/index.html")
                time.sleep(10)
                sc_list()
                
            elif x == 7:
                print("Wait for setup  { ALL } ")
                time.sleep(0.5)
                # os.system("sudo unzip bWAPP.zip")
                # os.system("sudo unzip sqli-labs.zip")
                # os.system("sudo unzip hackademic.zip")
                # os.system("sudo unzip dvwa.zip")
                # os.system("sudo tar -xvzfxvwa.tar.gz")
                # os.system("sudo unzip  xvwa.zip")
                # os.system("sudo unzip mutillidae.zip")
                # time.sleep(4.5)
                os.system("sudo cp -r bWAPP /var/www/html/InfoSecLabWeb/testLabs")
                os.system("sudo chmod 777 /var/www/html/InfoSecLabWeb/testLabs/bWAPP/passwords/")
                os.system("sudo chmod 777 /var/www/html/InfoSecLabWeb/testLabs/bWAPP/images/")
                os.system("sudo chmod 777 /var/www/html/InfoSecLabWeb/testLabs/bWAPP/documents/")
                # something want ronge mkdir
                # os.system("sudo mkdir /var/www/html/bWAPP/logs/")
                os.system("sudo chmod 777 /var/www/html/InfoSecLabWeb/testLabs/bWAPP/logs/")
                os.system("sudo chown -R www-data:www-data /var/www/html/InfoSecLabWeb/testLabs/bWAPP/")
                time.sleep(0.5)
                os.system("sudo cp -r xvwa /var/www/html/InfoSecLabWeb/testLabs")
                os.system("sudo cp -r dvwa /var/www/html/InfoSecLabWeb/testLabs")
                os.system("sudo chmod -R 777 /var/www/html/InfoSecLabWeb/testLabs/dvwa/external/phpids/0.6/lib/IDS/tmp/phpids_log.txt")
                os.system("sudo chmod -R 777 /var/www/html/InfoSecLabWeb/testLabs/dvwa/hackable/uploads")
                os.system("sudo chmod -R 777 /var/www/html/InfoSecLabWeb/testLabs/dvwa/config")
                time.sleep(0.5)
                os.system("sudo cp -r mutillidae /var/www/html/InfoSecLabWeb/testLabs ;sudo chown -R www-data:www-data /var/www/html/InfoSecLabWeb/testLabs/mutillidae/")
                os.system("sudo cp -r hackademic /var/www/html/InfoSecLabWeb/testLabs")
                os.system("sudo cp -r sqli-labs /var/www/html/InfoSecLabWeb/testLabs")
                time.sleep(2)
                print("\033[1;32;40m Done, All labs are  installed Successfily in current path:/var/www/html/InfoSecLabWeb/testLabs ")
                print("\033[0;32;80m-------------------------------------------------------")
                print("Now you can use your SecInfo-HA-lab..... ")
                print("Go for Opening your Browser IP Machine is = >>  : ")
                os.system("IP=$(ifconfig | grep -i inet | cut -d ' ' -f 10 | head -1);echo [--] http://$IP/index.html")
                time.sleep(10)
                sc_list()
            elif x == 13:
                        try:
                            print("Step 9: Create MariaDB databases ")
                            import mariadb
                            time.sleep(0.5)
                            conn = mariadb.connect(
                                user="root",
                                password="",
                                host="localhost",
                                port=3306,
                                database="mysql"
                            )
                            #Create databases using cursor.execute()
                            #Create databases for dvwa with own user dvwa'@'localhost and password dvwa
                            print("Creating databases....")
                            cursor = conn.cursor()
                            print("Step 9.1: Creating dvwa database ")
                            cursor.execute("CREATE DATABASE IF NOT EXISTS  dvwa;")
                            cursor.execute("CREATE USER IF NOT EXISTS 'dvwa'@'localhost' IDENTIFIED BY 'dvwa';")
                            cursor.execute("GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost';")
                            cursor.execute("SHOW GRANTS FOR 'dvwa'@'localhost';")
                            cursor.execute("flush privileges;")
                            time.sleep(0.5)
                            print("dvwa fninshed")
                            #Create databases for xvwa with own user xvwa'@'localhost and password xvwa
                            print("Step 9.2: Creating xvwa database ")
                            cursor.execute("CREATE DATABASE IF NOT EXISTS  xvwa;")
                            cursor.execute("CREATE USER IF NOT EXISTS 'xvwa'@'localhost' IDENTIFIED BY 'xvwa';")
                            cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'xvwa'@'localhost';")
                            cursor.execute("SHOW GRANTS FOR 'xvwa'@'localhost';")
                            cursor.execute("flush privileges;")
                            time.sleep(0.5)
                            print("SQL fninshed")
                            #Create databases for bWAPP with own user bWAPP'@'localhost and password bWAPP
                            print("Step 9.3: Creating bWAPP database ")
                            cursor.execute("CREATE USER IF NOT EXISTS 'bWAPP'@'localhost' IDENTIFIED BY 'bWAPP';")
                            cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'bWAPP'@'localhost';")
                            cursor.execute("SHOW GRANTS FOR 'bWAPP'@'localhost';")
                            cursor.execute("flush privileges;")
                            time.sleep(0.5)
                            #Create databases for secursority and challenges
                            print("Step 9.4: Creating secursority and challenges databases ")
                            cursor.execute("CREATE DATABASE IF NOT EXISTS  secursority;")
                            cursor.execute("CREATE DATABASE IF NOT EXISTS  challenges;")
                            cursor.execute("CREATE USER IF NOT EXISTS 'sql'@'localhost' IDENTIFIED BY 'sql';")
                            cursor.execute("GRANT ALL PRIVILEGES ON *.* TO # data mutillidae; 'sql'@'localhost';")
                            cursor.execute("SHOW GRANTS FOR 'sql'@'localhost';")
                            cursor.execute("flush privileges;")
                            time.sleep(0.5)
                            print("9.4 secursority & challenges fninshed")
                            #Create databases for mutillidae with own user mutillidae'@'localhost and password mutillidae
                            print("Step 9.5: Creating mutillidae  database")
                            cursor.execute("CREATE DATABASE IF NOT EXISTS mutillidae;")
                            cursor.execute("CREATE USER IF NOT EXISTS 'mutillidae'@'localhost' IDENTIFIED BY 'mutillidae';")
                            cursor.execute("GRANT ALL PRIVILEGES ON mutillidae.* TO 'mutillidae'@'localhost';")
                            cursor.execute("SHOW GRANTS FOR 'mutillidae'@'localhost';")
                            cursor.execute("use mysql;")
                            cursor.execute("flush privileges;")
                            print("Mutillidae part 1")
                            time.sleep(0.5)
                            cursor.execute("ALTER USER 'root'@'localhost' IDENTIFIED BY 'mutillidae';")
                            cursor.execute("SET PASSWORD FOR 'root'@'localhost' = PASSWORD('mutillidae');")
                            cursor.execute("flush privileges;")
                            time.sleep(0.5)
                            print("Mutillidae part 2")
                            print("Every thing is going Great...")
                            conn.close()
                        except:
                            import MySQLdb
                            print("Step 10: Create mysql databases ")
                            hostname = 'localhost'
                            username = 'root'
                            password = ''
                            database = 'mysql'
                            # Simple test to run a query on a database and print the results using cur.execute()
                            def doQuery(conn):
                                cur = conn.cursor()
                                # Data dvwa;
                                print("Step 9.1: Creating DVWA database ")
                                cur.execute("CREATE DATABASE IF NOT EXISTS dvwa;")
                                cur.execute("CREATE USER IF NOT EXISTS 'dvwa'@'localhost' IDENTIFIED BY 'dvwa';")
                                cur.execute("GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost';")
                                cur.execute("SHOW GRANTS FOR 'dvwa'@'localhost';")
                                cur.execute("flush privileges;")
                                time.sleep(0.5)
                                # Data sql;
                                cur.execute("CREATE DATABASE IF NOT EXISTS xvwa;")
                                cur.execute("CREATE USER IF NOT EXISTS 'xvwa'@'localhost' IDENTIFIED BY 'xvwa';")
                                cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'xvwa'@'localhost';")
                                cur.execute("SHOW GRANTS FOR 'xvwa'@'localhost';")
                                cur.execute("flush privileges;")
                                time.sleep(0.5)
                                # Data bWAPP;
                                print("Step 9.3: Creating BWAPP database ")
                                cur.execute("CREATE USER IF NOT EXISTS 'bWAPP'@'localhost' IDENTIFIED BY 'bWAPP';")
                                cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'bWAPP'@'localhost';")
                                cur.execute("SHOW GRANTS FOR 'bWAPP'@'localhost';")
                                cur.execute("flush privileges;")
                                time.sleep(0.5)
                                # Data sql;
                                print("Step 9.4: Creating security and challenges databases ")
                                cur.execute("CREATE DATABASE IF NOT EXISTS security;")
                                cur.execute("CREATE DATABASE IF NOT EXISTS challenges;")
                                cur.execute("CREATE USER IF NOT EXISTS 'sql'@'localhost' IDENTIFIED BY 'sql';")
                                cur.execute("GRANT ALL PRIVILEGES ON *.* TO 'sql'@'localhost';")
                                cur.execute("SHOW GRANTS FOR 'sql'@'localhost';")
                                cur.execute("flush privileges;")
                                time.sleep(0.5)
                                # Data mutillidae;
                                print("Step 9.5: Creating mutillidae database ")
                                cur.execute("CREATE DATABASE IF NOT EXISTS mutillidae;")
                                cur.execute("CREATE USER IF NOT EXISTS 'mutillidae'@'localhost' IDENTIFIED BY 'mutillidae';")
                                cur.execute("GRANT ALL PRIVILEGES ON mutillidae.* TO 'mutillidae'@'localhost';")
                                cur.execute("SHOW GRANTS FOR 'mutillidae'@'localhost';")
                                cur.execute("use mysql;")
                                cur.execute("flush privileges;")
                                print("mutillidae part 1")
                                time.sleep(0.5)
                                #Updataing passwords for mutillidae
                                cur.execute("update user set authentication_string=PASSWORD('mutillidae') where user='mutillidae';")
                                cur.execute("update user set plugin='mysql_native_password' where user='mutillidae';")
                                cur.execute("flush privileges;")
                                time.sleep(0.5)
                                #Test databace for list usrs        
                                print("Mutillidae part 2")
                                for firstname, lastname in cur.fetchall():
                                    print(firstname, lastname)
                            print("Using MySQLdb ... ")
                            #Test databace connecation with own user of secinfo-lab       
                            myConnection = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)
                            doQuery(myConnection)
                            myConnection.close()
                            print("Creating databases done ...... \n")
                            print("-------------------------------------------")
                            time.sleep(10)
                            sc_list()
                            print("\033[0;32;80m-------------------------------------------------------")
                            print("Now you can use your SecInfo-HA-lab..... ")
                            print("Go for Opening your Browser IP Machine is = >>  : ")
                            os.system("IP=$(ifconfig | grep -i inet | cut -d ' ' -f 10 | head -1);echo [--] http://$IP/index.html")
                            time.sleep(10)
                            sc_list()
                            print("\033[0;32;80m-------------------------------------------------------")
        except:
            print("\033[0;31;80m [x] We could not understand your choise, Enter exist number!!!")
            time.sleep(15)
    elif x == 14:
        break
print(" Goodbye Friend....")
os.system("sudo service apache2 restart")
os.system("clear")

print("\033[0;32;40m ")
f = open('banner.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()

print("--------------------------------------------------------------")
print("Hello Friend ... ")
print("Now you can use your InfoSec-HA-Lab..... ")
print("Go for Opening your Browser IP Machine is = >>  : ")
os.system("IP=$(ifconfig | grep -i inet | cut -d ' ' -f 10 | head -1);echo [--] http://$IP/index.html")
os.system("exit")
