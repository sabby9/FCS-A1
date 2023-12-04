import socket
import hashlib
import pickle


def server_program():

    host = socket.gethostname()
    port = 5000  

    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("Socket successfully created")
    except:
        print ("socket creation failed.")
 
    try:
        server_socket.bind((host, port)) 
        print("Server bind complete")
    except:
        print("error occured in bind")


    try:    
        server_socket.listen(1)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection established with client.")
    except:
        print("connection establishment failed.")

    #data = conn.recv(1024).decode()
    data = conn.recv(1024) 
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
            print("Message Verified.")
            print("Message from client: " + str(key.decode()))
            # conn.send(("Message Verified".encode('utf-8')))
            message = "Hello, Client!".encode('utf-8')  # take input
            hashed_string = hashlib.sha256(message).hexdigest().encode('utf-8')
            # print(hashed_string)
            d = {message:hashed_string}
            bytes_data = pickle.dumps(d)
            conn.send(bytes_data)  # send message
        else:

            #conn.send(("Message Tampered.".encode('utf-8')))
            message = "Server received tampered message".encode('utf-8')  # take input
            hashed_string = hashlib.sha256(message).hexdigest().encode('utf-8')
            print(hashed_string)
            d = {message:hashed_string}
            bytes_data = pickle.dumps(d)
            conn.send(bytes_data)  # send message


    else:
        print("Could not get data from server.")

    conn.close() 


if __name__ == '__main__':
    server_program()