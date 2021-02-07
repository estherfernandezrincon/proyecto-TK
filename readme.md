
# REQUIREMENTS  
En el fichero requirements.txt están las dependencias necesarias para el funcionamiento.
Creamos un entorno virtual, desde consola ejecutamos:
python -m venv venv
venv\Scripts\activate (para windows)  
. venv/bin/activate (para Linux o Mac)
pip install -r requirements.txt


# OBTENER API KEY

Desde la url de CoinMarketCap obtenemos nuestra apikey. 
Entramos en  https://coinmarketcap.com/api/



# CREAR TABLA EN BASE DE DATOS
Crear Base de Datos en DB Browser. La tabla  se tiene que  llamar MOVEMENTS y se crea como sigue:

''' CREATE TABLE  MOVEMENTS (
    id ,
    Date  ,
    Time ,
    MoneyF ,
    MoneyQ ,
    CurrencyT ,
    CurrencyQ ,
    P 
    )'''
     )

   **  id es de tipo INTEGER , primary key**
   ** Date, Time, MoneyF, CurrencyT son de tipo TEXT**
   ** MoneyQ, CurrencyQ y P, son de tipo REAL.**

   ##Carpeta base de datos: creamos una carpeta de Base de datos que estará ubicada dentro de MYCRIPTOS


   # CREAR ARCHIVO PARA PROTEGER RUTA BASE DE DATOS Y APIKEY

   Creamos un fichero dentro de MYCRIPTOS con nombre config.ini. El fichero comienza con [DEFAULT]
   En él creamos dos variables, una con nuestra apikey y otra con nuestra ruta a base de datos.
   Ambas de deben escribir sin comillas ni espacios.
   Ver archivo config_template.ini como referencia.

   # MANEJO APLICACION

   Una vez abierta la aplicación, vemos en la parte central NUEVA TRANSACCIÓN.
   En el desplegable FROM, elegimos entre las monedas que tienen saldo, la primera vez solo tenemos EUR.
   En el entry Q, ponemos la cantidad que queremos invertir. 
   En el desplegable TO, elegimos la moneda que queremos comprar.
   Pulsamos el boton Consulta Api, donde nos muestra los siguientes importes:
   ***En Q, nos aparecerá el importe de la criptomoneda elegida según el importe invertido.***
   ***En P.U. nos aparecerá el valor unitario de la criptomoneda elegida.***

   Si nuestra eleccion no nos es válida, pulsamos Cancelar y volemos a elegir nuestra opcion.
   Si pulsamos Aceptar, realizamos la compra de la criptomoneda y grabamos en nuestra base de datos.

   Para saber nuestros Euros invertidos y el valor Actual de las criptomonedas en Euros, pulsamos el boton Calcular.
   Para poder realizar compras de criptomonedas, inviendo criptomonedas, haremos primero la consulta de nuestro saldo de criptomonedas pulsando el boton Consultar Saldo.

   





 