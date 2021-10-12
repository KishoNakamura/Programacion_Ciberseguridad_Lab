import nmap

begin = 70
end = 90

target = input("Ingrese la dirección ip: ")
scanner = nmap.PortScanner()

array_ip= []
count = 1
for x in target:
	if count <= 3:
		if x == '.':
			count += 1
			array_ip.append(x)
		else:
			array_ip.append(x)

ip = ''.join(array_ip)

for x in range(100, 124):
	print('analizando esta ip: ', ip + str(x))
	try:
		new_ip = ip + str(x)		
		for i in range (begin, end+1):

			res = scanner.scan(new_ip, str(i))

			res = res['scan'][new_ip]['tcp'][i]['state']

			print(f'port {i} is {res}.')
			print(scanner.csv())
		print('= = = = = = = = = = = = = = = = = = = = = = = = = = = =\n')
	except KeyError:
		print('No se encontró ningun puerto abierto en:', new_ip)
		print('= = = = = = = = = = = = = = = = = = = = = = = = = = = =\n')


