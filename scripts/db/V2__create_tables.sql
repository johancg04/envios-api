CREATE TABLE usuario (
    id_usuario serial PRIMARY KEY,
    nombre varchar(50) NOT NULl,
    correo varchar(50) NOT NULL,
    usuario varchar(20) NOT NULL,
    contrasenia varchar(100) NOT NULL,
    rol varchar(20) NOT NULL,
    estado varchar(10) NOT NULL
);

CREATE TABLE cliente (
    id_cliente serial PRIMARY KEY,
    nombre varchar(50) NOT NULL,
    dni char(8) NOT NULL,
    telefono varchar(20) NOT NULL,
    correo varchar(50) NOT NULL
);

CREATE TABLE envio (
    id_envio serial PRIMARY KEY,
    id_cliente integer NOT NULL,
    id_usuario integer NOT NULL,
    codigo_envio varchar(10) NOT NULL, -- 2601080001 o 0000000001
    origen varchar(20) NOT NULL,
    destino varchar(20) NOT NULL,
    peso float NOT NULL,
    importe float NOT NULL,
    fecha_envio timestamp NOT NULL,
    dni_destinatario char(8) NOT NULL,
    nombre_destinatario varchar(50) NOT NULL,
    telefono_destinatario varchar(20) NOT NULL,

    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
);

CREATE TABLE seguimiento (
    id_seguimiento serial PRIMARY KEY,
    id_envio integer NOT NULL,
    origen varchar(20) NOT NULL,
    destino varchar(20) NOT NULL,
    fecha_salida timestamp NOT NULL,
    fecha_llegada timestamp,
    estatus varchar(20) NOT NULL, -- Registrado, En almacen, En camino, En destino, Entregado, (To-do: Retrasado)

    FOREIGN KEY (id_envio) REFERENCES envio(id_envio)
)
