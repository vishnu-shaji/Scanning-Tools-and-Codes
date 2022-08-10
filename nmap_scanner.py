import nmap
x = int(input("Enter the port starting range: "))
y = int(input("Enter the port ending range: "))
target = input("Enter the host address: ")
scanner = nmap.PortScanner()

for i in range(x, y+1):
    res = scanner.scan(target, str(i))
    res = res['scan'][target]['tcp'][i]['state']
    print(f'port {i} is {res}.')