from crypto_utils import hash_master_password,verify_master_password
from storage import save_master_hash,load_master_hash

def main():
    print("Welcome to Password Manager!!!")
    
    stored_hash = load_master_hash()
    
    if stored_hash is None:
        master = input("Set a master password \n")
        hashed = hash_master_password(master)
        save_master_hash(hashed)
        print("Master password set successfully >>>>>")
        
    else:
        while True:
            attempt = input("Enter master password\n")
            if verify_master_password(stored_hash,attempt):
                print("Access Granted!!!!!")
                break
            else:
                print("Invalid Password try again!!")
                
if __name__ == "__main__":
    main()
        