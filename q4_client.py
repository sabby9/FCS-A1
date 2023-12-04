import socket
import hashlib
import pickle
import sys



def client_program():
    host = socket.gethostname()
    port = 5000  

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created")
    except socket.error as err:
        print ("socket creation failed with error %s" %(err))

    try:
        client_socket.connect((host, port))
        print('Successfully connected to client')
    except:
        print('Connection to server failed')

    message = "Hello, Server!".encode('utf-8')  # take input
    hashed_string = hashlib.sha256(message).hexdigest().encode('utf-8')
    # print(hashed_string)
    d = {message:hashed_string}
    bytes_data = pickle.dumps(d)

    client_socket.send(bytes_data)  # send message
    #data = client_socket.recv(1024).decode()  # receive response
    data = client_socket.recv(1024) 
    data = pickle.loads(data)
    if data:
        print('verifying the hash')
        key = []
        for k in data.keys():
            key.append(k)
        key = key[0]

        value = []
        for v in data.values():
            value.append(v)
        value = value[0]

        # print(key)
        # print(value)

    hash_from_key = hashlib.sha256(key).hexdigest().encode('utf-8')
        # print(hash_from_key)

    if hash_from_key == value:
        print("Message from server verified.")
        print("Message from server:" + str(key.decode()))
        sys.exit()

    else:
        print("Could not verify hash, msg from server tampered")
        sys.exit()


    print('Received from server: ' + data)  # show in terminal

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()