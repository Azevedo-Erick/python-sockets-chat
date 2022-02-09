import threading
import socket

clients = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost',4040))
        server.listen()
    
    except:
        return print('\nNão foi possível iniciar o servidor\n')

    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def systemMessage(msg,client):
    for clientItem in clients:
        if(clientItem!=client):
            try:
                clientItem.send(+msg)
            except:
                removeClient(clientItem)

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg,client)
        except:
            removeClient(client)
            break


def broadcast(msg, client):
    for clientItem in clients:
        if(clientItem!=client):
            try:
                clientItem.send(msg)
            except:
                removeClient(clientItem)

def removeClient(client):
    clients.remove(client)  


main()