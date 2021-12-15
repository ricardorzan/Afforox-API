from peewee import *

database = PostgresqlDatabase('Afforox', **{'user': 'ricardodars', 'password': 'gatodeportivo'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Aceptado(BaseModel):
    aceptado = CharField(null=True)
    aceptadoid = AutoField()

    class Meta:
        table_name = 'aceptado'

class Dia(BaseModel):
    dia = CharField(null=True)
    diaid = AutoField()

    class Meta:
        table_name = 'dia'

class Domicilio(BaseModel):
    calle = CharField(null=True)
    ciudad = CharField(null=True)
    colonia = CharField(null=True)
    domicilioid = AutoField()
    estado = CharField(null=True)
    municipio = CharField(null=True)
    numeroexterior = SmallIntegerField(null=True)
    numerointerior = SmallIntegerField(null=True)
    pais = CharField(null=True)

    class Meta:
        table_name = 'domicilio'

class Usuario(BaseModel):
    aceptadoid = ForeignKeyField(column_name='aceptadoid', constraints=[SQL("DEFAULT nextval('usuario_aceptadoid_seq'::regclass)")], field='aceptadoid', model=Aceptado)
    codigoautenticacion = CharField(null=True)
    contrasenia = CharField(null=True)
    correoelectronico = CharField(primary_key=True)
    domicilioid = ForeignKeyField(column_name='domicilioid', constraints=[SQL("DEFAULT nextval('usuario_domicilioid_seq'::regclass)")], field='domicilioid', model=Domicilio)
    edad = SmallIntegerField(null=True)
    fechanacimiento = DateField(null=True)
    fotoperfil = BlobField(null=True)
    nombrecompleto = CharField(null=True)
    telefono = CharField(null=True)

    class Meta:
        table_name = 'usuario'

class Tiponegocio(BaseModel):
    tiponegocio = CharField(null=True)
    tiponegocioid = AutoField()

    class Meta:
        table_name = 'tiponegocio'

class Negocio(BaseModel):
    correoelectronico = CharField(null=True)
    correoelectronicousuario = ForeignKeyField(column_name='correoelectronicousuario', field='correoelectronico', model=Usuario)
    facebook = CharField(null=True)
    fotoperfil = BlobField(null=True)
    instagram = CharField(null=True)
    negocioid = AutoField()
    nombrenegocio = CharField(null=True)
    telefono = CharField(null=True)
    tiponegocioid = ForeignKeyField(column_name='tiponegocioid', constraints=[SQL("DEFAULT nextval('negocio_tiponegocioid_seq'::regclass)")], field='tiponegocioid', model=Tiponegocio)
    whatsapp = CharField(null=True)

    class Meta:
        table_name = 'negocio'

class Sucursal(BaseModel):
    aforoactual = SmallIntegerField(null=True)
    aforototal = SmallIntegerField(null=True)
    domicilioid = ForeignKeyField(column_name='domicilioid', constraints=[SQL("DEFAULT nextval('sucursal_domicilioid_seq'::regclass)")], field='domicilioid', model=Domicilio)
    negocioid = ForeignKeyField(column_name='negocioid', constraints=[SQL("DEFAULT nextval('sucursal_negocioid_seq'::regclass)")], field='negocioid', model=Negocio)
    nombresucursal = CharField(null=True)
    sucursalid = AutoField()
    telefono = CharField(null=True)

    class Meta:
        table_name = 'sucursal'

class Favorito(BaseModel):
    correoelectronico = ForeignKeyField(column_name='correoelectronico', field='correoelectronico', model=Usuario)
    sucursalid = ForeignKeyField(column_name='sucursalid', constraints=[SQL("DEFAULT nextval('favorito_sucursalid_seq'::regclass)")], field='sucursalid', model=Sucursal)

    class Meta:
        table_name = 'favorito'
        indexes = (
            (('sucursalid', 'correoelectronico'), True),
        )
        primary_key = CompositeKey('correoelectronico', 'sucursalid')

class Horario(BaseModel):
    diaid = ForeignKeyField(column_name='diaid', constraints=[SQL("DEFAULT nextval('horario_diaid_seq'::regclass)")], field='diaid', model=Dia)
    horarioapertura = TimeField(null=True)
    horariocierre = TimeField(null=True)
    horarioid = AutoField()
    sucursalid = ForeignKeyField(column_name='sucursalid', constraints=[SQL("DEFAULT nextval('horario_sucursalid_seq'::regclass)")], field='sucursalid', model=Sucursal)

    class Meta:
        table_name = 'horario'

class Medidasseguridad(BaseModel):
    medidaseguridad = CharField(null=True)
    medidasseguridadid = AutoField()

    class Meta:
        table_name = 'medidasseguridad'

class Opinion(BaseModel):
    calificacion = SmallIntegerField(null=True)
    comentario = CharField(null=True)
    correoelectronico = ForeignKeyField(column_name='correoelectronico', field='correoelectronico', model=Usuario)
    fechaopinion = DateTimeField(null=True)
    sucursalid = ForeignKeyField(column_name='sucursalid', constraints=[SQL("DEFAULT nextval('opinion_sucursalid_seq'::regclass)")], field='sucursalid', model=Sucursal)

    class Meta:
        table_name = 'opinion'
        indexes = (
            (('correoelectronico', 'sucursalid'), True),
        )
        primary_key = CompositeKey('correoelectronico', 'sucursalid')

class Reservacion(BaseModel):
    cantidadreservada = SmallIntegerField(null=True)
    correoelectronico = ForeignKeyField(column_name='correoelectronico', field='correoelectronico', model=Usuario, null=True)
    fechareservacion = DateTimeField(null=True)
    reservacionid = AutoField()
    sucursalid = ForeignKeyField(column_name='sucursalid', constraints=[SQL("DEFAULT nextval('reservacion_sucursalid_seq'::regclass)")], field='sucursalid', model=Sucursal)

    class Meta:
        table_name = 'reservacion'

class Servicios(BaseModel):
    servicio = CharField(null=True)
    serviciosid = AutoField()

    class Meta:
        table_name = 'servicios'

class Sucursalmedidasseguridad(BaseModel):
    medidasseguridadid = ForeignKeyField(column_name='medidasseguridadid', constraints=[SQL("DEFAULT nextval('sucursalmedidasseguridad_medidasseguridadid_seq'::regclass)")], field='medidasseguridadid', model=Medidasseguridad)
    sucursalid = ForeignKeyField(column_name='sucursalid', constraints=[SQL("DEFAULT nextval('sucursalmedidasseguridad_sucursalid_seq'::regclass)")], field='sucursalid', model=Sucursal)

    class Meta:
        table_name = 'sucursalmedidasseguridad'
        indexes = (
            (('medidasseguridadid', 'sucursalid'), True),
        )
        primary_key = CompositeKey('medidasseguridadid', 'sucursalid')

class Sucursalservicios(BaseModel):
    serviciosid = ForeignKeyField(column_name='serviciosid', constraints=[SQL("DEFAULT nextval('sucursalservicios_serviciosid_seq'::regclass)")], field='serviciosid', model=Servicios)
    sucursalid = ForeignKeyField(column_name='sucursalid', constraints=[SQL("DEFAULT nextval('sucursalservicios_sucursalid_seq'::regclass)")], field='sucursalid', model=Sucursal)

    class Meta:
        table_name = 'sucursalservicios'
        indexes = (
            (('serviciosid', 'sucursalid'), True),
        )
        primary_key = CompositeKey('serviciosid', 'sucursalid')

