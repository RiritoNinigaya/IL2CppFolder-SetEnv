import os

def Main():
    os.environ['IL2CPPFOLDER'] = "C:\\Program Files\\Unity\\Hub\\Editor\\2022.3.14f1\\Editor\\Data\\il2cpp\\libil2cpp"
    print(os.environ['IL2CPPFOLDER'])
    res = input("Do You Want Restart? :")
    if res == "yes":
        os.system("shutdown /r /t 0")
    else:
        print("OKAY!!!")
        exit(5545)
if __name__ == "__main__":
    Main()