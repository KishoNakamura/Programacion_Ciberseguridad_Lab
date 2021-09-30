Write-Host " - - - - Menu - - - -

[1] Cuadrado
[2] Triangulo
[3] Rectangulo
[4] Circulo "

$op = Read-Host -Prompt "Ingrese su opcion: "

switch($op)
{
    1{
        [int] $lado= Read-Host -Prompt "Ingrese el lado del cuadrado: "

        $Res= $lado*$lado
        Write-Host "El area del cuadrado es: " $Res
    }

    2{
        [int] $base= Read-Host -Prompt "Ingrese la base: "
        [int] $altura= Read-Host -Prompt "Ingrese la altura: "

        $Res= ($base*$altura) / 2
        Write-Host "El area del triangulo es: " $Res
    }

    3{
        [int] $base= Read-Host -Prompt "Ingrese la base: "
        [int] $altura= Read-Host -Prompt "Ingrese la altura: "

        $Res= $base*$altura
        Write-Host "El area del rectangulo es: " $Res
    }

    4{
        [int] $radio= Read-Host -Prompt "Ingrese el radio: "
        [float] $pi= 3.1416

        $Res= $pi*($radio*$radio)
        Write-Host "El area del circulo es: " $Res
    }
}
