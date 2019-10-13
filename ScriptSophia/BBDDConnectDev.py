import os
from os import system
import time


opcion = 0
while('3' != opcion):
    opcion = input('''Por favor seleccione un entorno:
     1 Develop
     2 Production
     3 Exit
     ''')
    if( opcion == '1'):
        def login():
            os.system("gcloud config set account andresfrancisco.lopez.contractor@dev.bbva.com")


        def changeDir():
            changeDir = "cd C:\\Users\\alopecol\\cloud_sql_proxy && cloud_sql_proxy_x64 -instances=dev-bbva-dataquality-hod:europe-west1:micro-model=tcp:5432"
            print(changeDir)
            os.system(changeDir)

        def main():
            login()
            time.sleep(1.5)
            changeDir()
        main()
        sys.exit()
    elif(opcion == '2'):
        def login():
            os.system("gcloud config set account andresfrancisco.lopez.contractor@bbva.com")


        def changeDir():
            changeDir = "cd C:\\Users\\alopecol\\cloud_sql_proxy && cloud_sql_proxy_x64 -instances=bbva-dataquality-hod:europe-west1:micro-model=tcp:5433"
            print(changeDir)
            os.system(changeDir)
        def main():
            login()
            time.sleep(1.5)
            changeDir()
        main()
        sys.exit()
print('Fin del programa')




#def loginEnv():
#   os.system("cloud_sql_proxy_x64 -instances=dev-bbva-dataquality-hod:europe-west1:micro-model=tcp:5432")


#    loginEnv()




