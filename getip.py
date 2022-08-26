#Importing "Socket" module
import socket


#Getting ip by typing an address
def get_ip_by_hostname():
    hostname = input("Enter a website address / Введите адрес сайта: ")

    try:
        return f'Hostname: {hostname}\nIP address/ Айпи адрес: {socket.gethostbyname(hostname)}'
    except socket.gaierror as error:
        return f'Invalid hostname / Неправильное имя - {error}'


#Finally getting an ip
def main():
    print(get_ip_by_hostname())


#Starting our program
if __name__ == '__main__':
    main()