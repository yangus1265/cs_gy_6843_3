from socket import *

def smtpCommands(clientSocket, commandString, errorType):
    errorMessage = '{0} reply not received from server.'.format(0)
    clientSocket.send(commandString.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != errorType:
        print(errorMessage(errorType))

def smtp_client(port=1025, mailserver='127.0.0.1'):
    # choose a mail server (e.g. Google mail server) if you want ot verify the script beyond gradescoe

    # create socket called clientSocket and establish a TCP connection with mailserver and  port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print(errorMessage('220'))

    # send HELO command and print server response.
    smtpCommands(clientSocket, 'HELO Alice\r\n', '250')

    # send MAIL FROM command and print server response
    smtpCommands(clientSocket, 'MAIL FROM: <eay8225@gmail.com>\r\n', '250')
    
    # send RCPT TO command and print server response
    smtpCommands(clientSocket, 'RCPT TO: <eay8225@gmail.com>\r\n', '250')
    
    # send DATA command and print server response
    smtpCommands(clientSocket, 'DATA', '354')

    # send message data
    msg = "\r\n My message"
    clientSocket.send(msg.encode())

    # Message ends with a single period.
    smtpCommands(clientSocket, "\r\n.\r\n", '250')

    # send QUIT command and get server response
    smtpCommands(clientSocket, 'QUIT\r\n', '221')

    if __name__ == '__main__':
        smtp_client(1025, '127.0.0.1')