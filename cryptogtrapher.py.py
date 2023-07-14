import os
import platform
from cryptography.fernet import Fernet

os.listdir()
directory = os.getcwd()# works on the current working directory
def deliti(directory):

#deletes all pdf file extentions
    try :
        for filename in os.listdir(directory):
            if filename.endswith(".pdf"):
                PATH =os.path.join(directory,filename)
                os.remove(PATH)
                print(f"deleted files are {PATH}")
            else :
                print("no pdf files found in the directory")
        return  filename 
        
    except Exception as e:
        print(f"an error occured during execution {e}")   


directory= os.cwd()


def clear_cache():
    #clears thecache of a system
    system=platform.system()
    if system == 'Windows':
        os.system('ipconfig /flushdns')
        os.system('del /q /s /f %temp%\\*')
    
    elif system == 'Linux':
        os.system('sudo sync && echo 3 | sudo /proc/sys/vm/drop_caches')

    elif system == 'Darwin':
        os.system("sudo purge")
    else:
        os.system(f"Cache clearing is not supported on the system{system}")

def encrypter(filename):
    #encrypts all txt files 
    try :
        KEY = Fernet.generate_key()
        with open(filename,'rb') as file:
            data = file.read()
            fernet = Fernet(KEY)
            encrypted = fernet.encrypt(data)
        with open(filename, 'wb') as file:
            file.write(encrypted)
            
        print("FILES ENCRYPTED SUCCESSFULLY")
     
    except Exception as e:
        print(f"an error occured during execution {e}")   

 
def decryptor(filename,KEY):
    #decryptor for the above encryptor
    try:

        with open(filename, 'rb') as file:
            data= file.read()

            fernet=Fernet(KEY)
            decrypted=fernet.decrypt(data,KEY)
            file.write(decrypted)
    except Exception as e:
        print(f"an error occured during execution {e}")   


# not coverd parts like to enter a cli interface to choose between thye options