# IP Receiver
**IP Receiver** - a program on Python that can get an IP address by just entering a web address. 

### 🛠Links
[Socket's documentation](https://docs.python.org/3/library/socket.html) \
[Source](https://youtu.be/TNNNAxxT-8I)

## 📁Example in code
```
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
```

## 💻Example
![Getting Youtube's ip address🤨](https://github.com/manixonex/basicipreceiver/blob/main/images/example.png)
