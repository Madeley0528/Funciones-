import mysql.connector
def conectar(consulta_sql):
 

#Configuración de la conexión/ credenciales
    config = {
        'user': 'us7wj5xw2oxjvwzt',
        'password': 'DbeFLFamrWgMyuL8NvFp',
        'host': 'bepj2a0dsxg3jaxcxwwe-mysql.services.clever-cloud.com',
        'database': 'bepj2a0dsxg3jaxcxwwe',
        'raise_on_warnings': True
    }


# Conectar a la base de datos 
    try: 
       conexion = mysql.connector.connect(**config)
       print("Conexión exitosa a la base de datos.")

      #Objeto para crear consultas
       consultas = conexion.cursor()

       #Función para agregar la consulta SQL
       consultas.execute(consulta_sql)
       #Almacenamos el resultado de la consulta SQL
       resultado = consultas.fetchall()

       return resultado
     
    #Respuesta si al conectar da error 
    except mysql.connector.Error as err:
       print(f"Error al conectar a la base de datos: {err}")