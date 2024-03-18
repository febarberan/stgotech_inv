from django.db import models
from django.core.validators import MinValueValidator
from .choices import *
from django.contrib.auth.models import User


class Cargo(models.Model):
    id = models.AutoField
    name_cargo = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "cargo"
    
    def __str__(self):

        return self.name_cargo

class Consumidor(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(blank=True, null=True, max_length=50)
    apellido = models.CharField(blank=True, null=True, max_length=50)
    email = models.CharField(blank=True , null=True , max_length=50)
    cargo  = models.ForeignKey(Cargo, on_delete=models.SET_NULL , null=True , blank=True)

    class Meta:
        db_table = "consumidor"
    
    def __str__(self):

        return self.nombre + ' ' + self.apellido

# Create your models here.
#TABLA CATEGORIA INCOMING
# class Categotia_incoming(models.Model):
#     categoria_pk = models.AutoField(primary_key=True, unique=True)   
#     name_categoria = models.CharField(blank=True , null=True, max_length=50)

#     class Meta:
#         db_table = "categoria_incoming"
    
#     def __str__(self):

#         return self.name_categoria

#TABLA ESTADO  
class Estado(models.Model):
    estado_pk = models.AutoField(primary_key=True, unique=True)
    estado = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "estado"
    
    def __str__(self):
        return self.estado
    

#TABLA UBICACION
class Ubicacion(models.Model):
    ubicacion_pk = models.AutoField(primary_key=True, unique= True)
    name_ubicacion = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "ubicacion"
    
    def __str__(self):
        return self.name_ubicacion
    


#TABLA UOM
class Uom(models.Model):
    uom_pk = models.AutoField(primary_key=True, unique=True)
    name_uom = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "uom"

    def __str__(self):
        return self.name_uom
    
#TABLA OWNER
class Owner(models.Model):
    owner_pk = models.AutoField(primary_key=True, unique=True)
    name_owner = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "owner"
    
    def __str__(self):
        return self.name_owner
        
#TABLA N_FICHA
class Ficha(models.Model):
    ficha_pk = models.AutoField(primary_key=True, unique=True)
    name_ficha = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "n_ficha"
    
    def __str__(self):
        return self.name_ficha

#TABLA CONDICION
class Condicion(models.Model):
    condicion_pk = models.AutoField(primary_key=True, unique=True)
    name_condicion = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "condicion"
    
    def __str__(self):
        return self.name_condicion
    

#TABLA CLASIFICACION
class Clasificacion(models.Model):
    clasificacion_pk = models.AutoField(primary_key=True, unique=True)
    name_clasificacion = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "clasificacion"
    
    def __str__(self):
        return self.name_clasificacion

#TABLA BODEGA
class Bodega(models.Model):
    bodega_pk = models.AutoField(primary_key=True, unique=True)
    name_bodega = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "bodega"

    def __str__(self):
        return self.name_bodega

#TABLA ORIGEN
class Origen(models.Model):
    origen_pk = models.AutoField(primary_key=True, unique=True)
    name_origen = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "origen"

    def __str__(self):
        return self.name_origen
    

#TABLA COMPAÑIA
class Compania(models.Model):
    cod_compania = models.IntegerField(primary_key=True , unique=True)
    nom_compania = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "compania"

    def __str__(self):
        return self.nom_compania
    


#Tabla Comat 
class Comat(models.Model):
    stdf_pk = models.CharField(primary_key=True, unique=True)
    awb = models.CharField(blank=True, null=True, max_length=50)
    hawb = models.CharField(blank=True, null=True, max_length=50)
    num_manifiesto = models.CharField(blank=True, null=True, max_length=50)
    corr_interno = models.CharField(blank=True, null=True, max_length=50)
    pcs = models.IntegerField(blank=True, null=True)
    peso = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2, default="0,00")
    f_control = models.DateTimeField(null=True, blank=True)
    f_manifiesto = models.DateTimeField(null=True, blank=True)
    f_recepcion = models.DateTimeField(null=True, blank=True)
    f_stdf = models.DateField(null=True, blank=True)
    fob = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2, default="0,00")
    flete = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2, default="0,00")
    seguro = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2, default="0,00")
    sum_cif = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=2, default="0,00")
    observaciones = models.CharField(blank=True, null=True, max_length=250)
    n_part_numbers = models.IntegerField(blank = True , null = True)
    #Claves Foraneas
    bodega_fk = models.ForeignKey(Bodega , on_delete=models.SET_NULL, null=True)
    origen_fk = models.ForeignKey(Origen, on_delete=models.SET_NULL, null=True)
    estado_fk = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True , default=1)
    usuario =  models.ForeignKey(User, on_delete=models.SET_NULL , null=True , blank=True)
    compania_fk = models.ForeignKey(Compania, on_delete=models.SET_NULL, null=True , blank=True)

    class Meta:
        db_table = 'comat'

    def __str__(self):
        return str(self.stdf_pk)
    
#Tabla Incoming
class Incoming(models.Model):
    id_incoming = models.AutoField(primary_key=True,unique=True)
    sn_batch_pk = models.CharField(blank=True, null=True, max_length=50)
    batch_pk = models.CharField(blank=True, null=True, max_length=50)
    part_number = models.CharField(blank=True, null=True, max_length=50)
    f_incoming = models.DateField(blank=True, null=True)
    descripcion = models.CharField(blank=True , null=True, max_length=250)
    po = models.CharField(blank=True, null=True, max_length=50)
    qty = models.IntegerField(blank=True, null=True)
    u_purchase_cost = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    total_u_purchase_cost = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    check_periodica = models.BooleanField(blank=True, null=True, default=False)
    f_check_periodica = models.DateField(blank=True, null=True)
    vencimiento = models.BooleanField(blank=True, null=True, default=False)
    f_vencimiento = models.DateField(blank=True, null=True)
    saldo = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0)])
    observaciones = models.CharField(blank=True, null=True, max_length=250)
    #Llaves foraneas
    #categoria_fk = models.ForeignKey(Categotia_incoming, on_delete=models.SET_NULL, null=True)
    clasificacion_fk = models.ForeignKey(Clasificacion, on_delete=models.SET_NULL, null=True)
    ubicacion_fk = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True)
    uom_fk = models.ForeignKey(Uom, on_delete=models.SET_NULL, null=True)
    owner_fk = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
    condicion_fk = models.ForeignKey(Condicion,on_delete=models.SET_NULL, null=True)
    ficha_fk = models.ForeignKey(Ficha, on_delete=models.SET_NULL, null=True)
    stdf_fk = models.ForeignKey(Comat, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL , null=True , blank=True)

    class Meta:
        db_table = 'incoming'
    
    def __int__(self):
        return self.id_incoming
    
    
class Estado_Repuesto(models.Model):
    id = models.AutoField(primary_key=True, unique=True ,validators=[MinValueValidator(1)] ) 
    name_estado = models.CharField( blank=True, null=True, max_length=50)

    class Meta:
        db_table = "estado_repuesto"
    
    def __str__(self):
        return self.name_estado
    
class Licencia(models.Model):
    id = models.AutoField(primary_key=True, unique=True ,validators=[MinValueValidator(1)] ) 
    name_licencia = models.CharField(blank=True, null=True, max_length=50)

    class Meta:
        db_table = "licencia"
    
    def __str__(self):
        return self.name_licencia


class Detalle_Incoming(models.Model):
    id = models.AutoField(primary_key=True, unique=True ,validators=[MinValueValidator(1)] )
    rcv_n = models.CharField(blank=True, null=True , max_length=50)
    modelo = models.CharField(blank=True, null=True , max_length=50)
    Proveedor = models.CharField(blank=True, null=True, max_length=50)
    taller_reparadora = models.CharField(blank=True, null=True, max_length=50)
    trabajo_solicitado = models.CharField(blank=True, null=True, max_length=50)
    propiedad = models.CharField(blank=True, null=True, max_length=50)
    ro_n = models.CharField(blank=True, null=True, max_length=50)
    wo_n = models.CharField(blank=True, null=True, max_length=50)
    aceptado = models.CharField(blank=True, null=True, max_length=50)
    item1 = models.BooleanField(blank=True, null=True, default=False)
    item2 = models.BooleanField(blank=True, null=True, default=False)
    item3 = models.BooleanField(blank=True, null=True, default=False)
    item4 = models.BooleanField(blank=True, null=True, default=False)
    item5 = models.BooleanField(blank=True, null=True, default=False)
    item6 = models.BooleanField(blank=True, null=True, default=False)
    item7 = models.BooleanField(blank=True, null=True, default=False)
    item8 = models.BooleanField(blank=True, null=True, default=False)
    item9 = models.BooleanField(blank=True, null=True, default=False)
    item10 = models.BooleanField(blank=True, null=True, default=False)
    item11 = models.BooleanField(blank=True, null=True, default=False)
    item12 = models.BooleanField(blank=True, null=True, default=False)
    item13 = models.BooleanField(blank=True, null=True, default=False)
    n_item13 = models.IntegerField(blank=True, null=True)
    item14 = models.BooleanField(blank=True, null=True, default=False)
    item15 = models.BooleanField(blank=True, null=True, default=False)
    n_item15 = models.IntegerField(blank=True, null=True)
    item16 = models.BooleanField(blank=True, null=True, default=False)
    n_item16 = models.IntegerField(blank=True, null=True)
    item17 = models.BooleanField(blank=True, null=True, default=False)
    n_item17 = models.IntegerField(blank=True, null=True)
    item18 = models.BooleanField(blank=True, null=True, default=False)
    n_item18tsn = models.IntegerField(blank=True, null=True)
    n_item18tso = models.IntegerField(blank=True, null=True)
    n_item18csn = models.IntegerField(blank=True, null=True)
    n_item18cso = models.IntegerField(blank=True, null=True)
    item19 = models.BooleanField(blank=True, null=True, default=False)
    item20 = models.BooleanField(blank=True, null=True, default=False)
    item21 = models.BooleanField(blank=True, null=True, default=False)
    item22 = models.BooleanField(blank=True, null=True, default=False)
    n_item22 = models.IntegerField(blank=True, null=True)
    estado_repuesto_fk = models.ForeignKey(Estado_Repuesto, on_delete=models.SET_NULL , null=True , blank=True)
    incoming_fk = models.OneToOneField(Incoming, on_delete=models.SET_NULL , null=True , blank=True)
    licencia = models.ForeignKey(Licencia, on_delete=models.SET_NULL , null=True , blank=True)

    class Meta:
        db_table = "detalle"
        
    def __int__(self):
        return self.id

#Tabla Consumos
class Consumos(models.Model):
    consumo_pk = models.AutoField(primary_key=True, unique=True , validators=[MinValueValidator(1)])
    orden_consumo = models.CharField(blank=True , null=True, max_length=50)
    f_transaccion = models.DateField(blank=True, null=True)
    qty_extraida = models.IntegerField(blank=True, null=True)
    matricula_aeronave = models.CharField(blank=True, null=True, max_length=50)
    observaciones = models.CharField(blank=True, null=True, max_length=250)
    incoming_fk = models.ForeignKey(Incoming, null=True, blank=True,on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL , null=True , blank=True)
    consumidor_fk = models.ForeignKey(Consumidor, on_delete=models.SET_NULL , null=True , blank=True)
    
    class Meta:
        db_table = "consumos"

    def __str__(self):
        return str(self.incoming_fk)
    
    
    




