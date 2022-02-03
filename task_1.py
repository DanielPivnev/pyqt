"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""
from ipaddress import ip_address
from subprocess import call, Popen


def host_ping(hosts_ls):
    for host in hosts_ls:
        try:
            ip_addr = ip_address(host)
            response = Popen(['ping', '-c', '1', f'{ip_addr}'], shell=False)
            response.wait()

            if response.returncode:
                print(ip_addr + ' - Узел недоступен')
            else:
                print(ip_addr + ' - Узел доступен')
        except ValueError:
            response = Popen(['ping', '-c', '1', host], shell=False)
            response.wait()

            if response.returncode:
                print(host + ' - Узел недоступен')
            else:
                print(host + ' - Узел доступен')


def main():
    hosts = ['yandex.ru', '2.2.2.2', '192.168.0.100', '192.168.0.101']
    host_ping(hosts)


if __name__ == '__main__':
    main()
