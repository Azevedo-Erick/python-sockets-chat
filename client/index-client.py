import threading
import socket

def main():
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost',4040))
    
    except:
        return print('\n Não foi possivel conectar')
    
    username = str(input("Como você deseja que te chamem?\nUsuário>  "))
    print('\nConectado')

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()

def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg +'\n')
        except:
            print('\nNão foi possível permanecer conectado\n')
            print('Pressione <Enter> para continuar...')
            client.close()
            break

def sendMessages(client,username):
    while True:
        try:
            msg = input('\n=>')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        
        except:
            return
    

main()
