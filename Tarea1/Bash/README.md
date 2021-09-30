Este es un script generado en bash el cual analiza el sistema opetavio que se esta usando, consigue la IP de la maquina, escanea las direcciones IP activas
y de esas IP busca los puertos activos de las mismas.

¿COMO SE USA?

1.- Puede guardarlo en cualquier sitio, lo unico que debe de hacer es darle privilegios de ejecucion con el siguiente comando:
	
	chmod +x OsInfo

2.- Una ves realizado esto solo queda ejecuatrlo utilizando el comando:    
	
	./OsInfo

3.- Al momento de que corre el programa se le mostrara la IP de la maquina al igual que le pedira los primeros octetos de la ip, Ej:
	
	IP: 234.321.456.123

	1) Ingrese el Primer: 234
	2) Ingrese el Segundo: 321
	3) Ingrese el tercero: 456 

3.- Cuando haya ingresado esta informacion simplemente debe de esperar hasta que el script genere el informe (el cual se generara en el mismo lugar que el archivo)
y listo tendra informacion de las diferentes  IP's y puertos abiertos.
