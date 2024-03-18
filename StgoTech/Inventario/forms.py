from django.forms import ModelForm, ValidationError
from .models import *
from django import forms
from datetime import date



# -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- #
class ComatForm(ModelForm):
    stdf_pk = forms.CharField(widget=forms.NumberInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa STDF"}),label='STDF')
    awb = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa AWB"}),label='AWB')
    hawb = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa HAWB"}),label='HAWB', required=False)
    num_manifiesto = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Número de Manifiesto"}),label='Número Manifiesto')
    corr_interno = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido","placeholder": "Ingresa Correlativo Interno"}),label='Correlativo Interno')
    pcs = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Cantidad de Piezas"}),label='Piezas')
    peso = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa el Peso"}),label='Peso')

    f_control = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control reducido", 'type': 'datetime-local', 'placeholder':'Selecciona la fecha', 'id':'id_f_control'}), required=True, label='Fecha de Control')
    # f_control = forms.DateTimeField(widget=AdminDateWidget())
    f_manifiesto = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control reducido", 'type': 'datetime-local', 'placeholder':'Selecciona la fecha'}), required=True, label='Fecha de Manifiesto')
    f_recepcion = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"class":"form-control reducido", 'type': 'datetime-local', 'placeholder':'Selecciona la fecha'}), required=True, label='Fecha de Recepción')
    f_stdf = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control reducido", 'type': 'date', 'placeholder':'Selecciona la fecha'}), required=True, label='Fecha de STDF')

    fob = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa el valor del FOB Formato - Utilice coma para separar  00,00"}),label='FOB')
    flete = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa el valor del Flete - Utilice coma para separar  00,00"}),label='Flete')
    seguro = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa el valor del Seguro - Utilice coma para separar  00,00"}),label='Seguro')
    observaciones = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa la observación"}),label='Observaciones' , required=False)
    # prioridad = forms.ChoiceField(choices=Prioridad,widget=forms.Select(attrs={"class":"form-control reducido", "placeholder": "Ingresa la Prioridad"}),label='Prioridad',required=True) 
    n_part_numbers = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Cantidad de Part Numbers"}),label='Cantidad de Part Numbers')
    bodega_fk = forms.ModelChoiceField(queryset=Bodega.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingresa la Bodega"}), label='Bodega')
    origen_fk = forms.ModelChoiceField(queryset=Origen.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingresa el Origen"}), label='Origen')
    compania_fk = forms.ModelChoiceField(queryset=Compania.objects.all(),widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingresa el Compañia"}), label='Compañia')
    
    class Meta:
        model = Comat
        fields = [ 
        'stdf_pk',
        'awb',
        'hawb',
        'num_manifiesto',
        'corr_interno',
        'pcs',
        'peso',
        'f_control',
        'f_manifiesto',
        'f_recepcion',
        'f_stdf',
        'fob',
        'flete',
        'seguro',
        'n_part_numbers',
        # 'prioridad',
        'compania_fk',
        'bodega_fk',
        'origen_fk',
        'observaciones',
        
        ]
# -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- #
class IncomingForm(ModelForm):

    sn_batch_pk = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Serial Number"}),label='Serial Number', required=False)
    batch_pk = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Batch Number"}),label='Batch Number', required=False)
    part_number = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Part Number"}),label='Part Number')
    f_incoming = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control reducido", 'type': 'date', 'placeholder': 'Selecciona la fecha'}),required=True,label='Fecha Ingreso Incoming',initial=date.today())
    po = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Product Order"}),label='PO')
    qty = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Cantidad"}),label='Quantity')
    u_purchase_cost = forms.DecimalField(widget=forms.NumberInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Unit Purchase Cost"}),label='Unit Purchase Cost')
    check_periodica = forms.BooleanField(required=False,label='Check Periodica',widget=forms.CheckboxInput,initial=True)
    f_check_periodica = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control reducido", 'type': 'date', "placeholder":'Seleccione fecha'}), required=False, label='Fecha Check Periodica')
    vencimiento = forms.BooleanField(required=False,label='¿Aplica Fecha de vencimiento?',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=True)
    f_vencimiento = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control reducido", 'type': 'date', "placeholder":'Seleccione fecha'}), required=False, label='Fecha Vencimiento')
    descripcion = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Descripción"}),label='Descripción')
    observaciones = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Observaciones"}),label='Observaciones',required=True)
    #categoria_fk = forms.ModelChoiceField(queryset=Categotia_incoming.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingresa la Categoria SN o BN"}), label='Categoria')
    clasificacion_fk = forms.ModelChoiceField(queryset=Clasificacion.objects.all(), widget=forms.Select(attrs={"class": "form-control reducido","placeholder": "Ingresa la Clasificación"}), label='Clasificación')
    ubicacion_fk = forms.ModelChoiceField(queryset=Ubicacion.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingresa la Ubicacion"}), label='Ubicación')
    uom_fk = forms.ModelChoiceField(queryset=Uom.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingreso Uom"}), label='Uom')
    owner_fk = forms.ModelChoiceField(queryset=Owner.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingreso Owner"}), label='Owner')
    condicion_fk = forms.ModelChoiceField(queryset=Condicion.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingresa Condicion"}), label='Condicion')
    ficha_fk = forms.ModelChoiceField(queryset=Ficha.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingreso N° Ficha"}), label='N° Ficha')
    stdf_fk = forms.ModelChoiceField(queryset=Comat.objects.all(),widget=forms.HiddenInput(attrs={"class": "select2-selection select2-selection--single", "placeholder": ""}), label='')
    #stdf_fk = forms.CharField(widget=forms.HiddenInput())
    # stdf_fk = forms.CharField(widget=forms.Select(attrs={"class": "form-control","placeholder": "Ingresa STDF", "id":"id_stdf_fk"}), label='STDF')
    #stdf_fk = forms.ModelChoiceField(queryset= Comat.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingresa STDF", "id":"id_stdf_fk"}), label='STDF')
    class Meta:
        model = Incoming
        fields = [
        'sn_batch_pk',
        #'categoria_fk',
        'batch_pk',
        'part_number',
        'f_incoming',
        'po',
        'qty',
        'u_purchase_cost',
        'check_periodica',
        'f_check_periodica',
        'vencimiento',
        'f_vencimiento',
        'descripcion',
        'clasificacion_fk', 
        'ubicacion_fk', 
        'uom_fk' , 
        'owner_fk' , 
        'condicion_fk', 
        'ficha_fk' , 
        'observaciones', 
        'stdf_fk',   
    ]

# -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- #
class ConsumosForm(ModelForm):
    # consumo_pk = forms.IntegerField(widget=forms.NumberInput())
    qty_extraida = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Cantidad Extraida"}),label='Cantidad Extraida', min_value=1)
    matricula_aeronave = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Matricula"}),label='Matricula Aeronave')
    observaciones = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Observaciones"}),label='Observaciones',required=False)
    f_transaccion = forms.DateTimeField(widget=forms.DateInput(attrs={"class":"form-control reducido",'type': 'date', "placeholder": "Seleccione fecha"}), required=False, label='Fecha de Transacción')
    incoming_fk = forms.ModelChoiceField(queryset=Incoming.objects.all(),widget=forms.HiddenInput(attrs={"class": "select2-selection select2-selection--single", "placeholder": ""}), label='')
    #incoming_fk = forms.ModelChoiceField(queryset=Incoming.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "incoming_id"}), label='incoming')
    consumidor_fk = forms.ModelChoiceField(queryset=Consumidor.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingresa Consumidor"}), label='Consumidor')
    # incoming_id = forms.CharField(widget=forms.ChoiceField(attrs={"class":"form-control"}),label='Serial Number')
    # id_estado = forms.CharField(widget=forms.ChoiceField(attrs={"class":"form-control"}),label='Estado')
    class Meta:
        model = Consumos
        fields = [
            
            'qty_extraida',
            'matricula_aeronave',
            'f_transaccion',
            'consumidor_fk',
            'observaciones',
            'incoming_fk',
        ]

    # def __init__(self, *args, **kwargs):
    #     super(ConsumosForm, self).__init__(*args, **kwargs)
    #     self.fields['incoming_fk'].label_from_instance = self.label_from_instance
    def label_from_instance(self, obj):
        return f'{obj.sn_batch_pk} - {obj.stdf_fk.stdf_pk}'

# -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- #
# class CategoriaForm(ModelForm):
#     name_categoria = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Nueva Categoria", 'id':'name_categoria'}),label='Categoria')

#     class Meta:
#         model = Categotia_incoming
#         fields = '__all__'

class EstadoForm(ModelForm):
    estado = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa Nuevo Estado", 'id':'estado'}),label='Estado')

    class Meta:
        model = Estado
        fields = '__all__'

class UbicacionForm(ModelForm):
    name_ubicacion = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa la Ubicación", 'id':'name_ubicacion'}),label='Ubicación')

    class Meta:
        model = Ubicacion
        fields = '__all__'

class UserForm(ModelForm):
    
    class Meta:
        model = User
        fields = '__all__'

class UomForm(ModelForm):
    name_uom = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa el Uom", 'id':'name_uom'}),label='Uom')
    
    class Meta:
        model = Uom
        fields = '__all__'

class OwnerForm(ModelForm):
    name_owner = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa el Owner", 'id':'name_owner'}),label='Owner')

    class Meta:
        model = Owner
        fields = '__all__'

class FichaForm(ModelForm):
    name_ficha = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa el N de Ficha", 'id':'name_ficha'}),label='Número de Ficha')

    class Meta:
        model = Ficha
        fields = '__all__'

class ConditionForm(ModelForm):
    name_condicion = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa la Condición", 'id':'name_condicion'}),label='Condición')

    class Meta:
        model = Condicion
        fields = '__all__'

class BodegaForm(ModelForm):
    name_bodega = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa una bodega", 'id':'name_bodega'}),label='Bodega')

    class Meta:
        model = Bodega
        fields = '__all__'

class OrigenForm(ModelForm):
    name_origen = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa un Origen", 'id':'name_origen'}),label='Origen')

    class Meta:
        model = Origen
        fields = '__all__'

class CargoForm(ModelForm):
    name_cargo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa un Cargo", 'id':'name_cargo'}),label='Cargo')

    class Meta:
        model = Cargo
        fields = '__all__'

class ClasificacionForm(ModelForm):
    name_clasificacion = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa una clasificación", 'id':'name_clasificacion'}),label='Clasificación')

    class Meta:
        model = Clasificacion
        fields = '__all__'

class ConsumidorForm(ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa una Nombre", 'id':'nombre'}),label='Nombre')
    apellido = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa un Apellido", 'id':'apellido'}),label='Apellido')
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa un Email", 'id':'email'}),label='Email')
    cargo = forms.ModelChoiceField(queryset=Cargo.objects.all(), widget=forms.Select(attrs={"class":"form-control", "placeholder": "Ingresa un Cargo", 'id':'cargo'}),label='Cargo')

    class Meta:
        model = Consumidor
        fields = '__all__'

class EstadoRepuestoForm(ModelForm):
    name_estado = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa un estado de repuesto", 'id':'name_estado'}),label='Estado Repuesto')

    class Meta:
        model = Estado_Repuesto
        fields = '__all__'

class CompaniaForm(ModelForm):
    nom_compania = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa un nombre de Compañia", 'id':'nom_compania'}),label='Nombre Compañia')

    class Meta:
        model = Compania
        fields = '__all__'

class LicenciaForm(ModelForm):
    name_licencia = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Ingresa una Licencia", 'id':'name_licencia'}),label='Nombre Licencia')

    class Meta:
        model = Licencia
        fields = '__all__'
# -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- ## -- # -- # -- # -- # -- # -- #

class DetalleForm(ModelForm):
    rcv_n = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa RCV N°"}),label='RCV N°', required=False)
    modelo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Modelo"}),label='Modelo', required=False)
    Proveedor = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Proveedor del Producto"}),label='Proveedor del Producto', required=False)
    taller_reparadora = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Ingresa Taller/Cia. Reparadora"}),label='Taller/Cia. Reparadora', required=False)
    trabajo_solicitado = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Trabajo Solicitado"}),label='Trabajo Solicitado', required=False)
    propiedad = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "Propiedad de"}),label='Propiedad de', required=False)
    ro_n = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "RO N°"}),label='RO N°', required=False)
    wo_n = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido", "placeholder": "WO N°"}),label='WO N°', required=False)
    aceptado = forms.CharField(widget=forms.Select(choices=ACEPTADO, attrs={"class":"form-control reducido",}),label='¿Aceptado?', required=False)
    item1 =  forms.BooleanField(required=False,label='1) Producto conforme a lo indicado en la lista de Embarque (Packing List)',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item2 =  forms.BooleanField(required=False,label='2) Factura del Proveedor conforme a la orden de compra o solicitud de trabajo (Invoice)',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item3 =  forms.BooleanField(required=False,label='3) Cartilla/Orden de Trabajo, Cartilla de prueba, Si corresponde, del taller que repara',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item4 =  forms.BooleanField(required=False,label='4) Producto sin daños visibles (Inspeccion Visual)',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item5 =  forms.BooleanField(required=False,label='5) Producto protegido en embalaje apropiado',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item6 =  forms.BooleanField(required=False,label='6) Placa de identificacion del componente',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item7 =  forms.BooleanField(required=False,label='7) Documentacion Técnica completa requerida por reglamentacion (Trazabilidad)',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item8 =  forms.BooleanField(required=False,label='8) Formulario FAA 8130-3',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item9 =  forms.BooleanField(required=False,label='9) Formulario EASA Form One o JAA Form One o CAA Form One',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)      
    item10 =  forms.BooleanField(required=False,label='10) Formulario DGAC Chile 8130-3',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item11 =  forms.BooleanField(required=False,label='11) Formulario ANAC Argentina 8130-3',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item12 =  forms.BooleanField(required=False,label='12) Placa o Etiqueta para Herramientas o equipos con calibracion',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item13 =  forms.BooleanField(required=False,label='13) Certificado de Calibración en laboratorio reconocido por el estado local',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    n_item13 = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control reducido",}),label='13.5) N° de Certificado de Calibración', required=False)
    item14 =  forms.BooleanField(required=False,label='14) Materiales con vida limite (Verificacion de Shelf life data y MSDS)',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item15 =  forms.BooleanField(required=False,label='15) Certificado de flamabilidad, si corresponde',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    n_item15 = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control reducido",}),label='15.5) N° de Certificado de Flamabilidad', required=False)
    item16 =  forms.BooleanField(required=False,label='16) Certificado de conformidad  y/o Analisis',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    n_item16 = forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control reducido",}),label='16.5) N° Certificado de conformidad y/o Analisis', required=False)
    item17 =  forms.BooleanField(required=False,label='17) Numero de lote de fabricacion, si corresponde',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    n_item17 = forms.IntegerField(widget=forms.TextInput( attrs={"class":"form-control reducido",}),label='17.5)Numero de lote de Fabricacion', required=False)
    item18 =  forms.BooleanField(required=False,label='18) TSO / TSN (Si Aplica)',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    n_item18tsn = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control reducido",}),label='18.5.1) Especifique Numero de TSN', required=False)
    n_item18tso = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control reducido",}),label='18.5.1) Especifique Numero de TSO', required=False)
    n_item18csn = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control reducido",}),label='18.5.1) Especifique Numero de CSN', required=False)
    n_item18cso = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control reducido",}),label='18.5.1) Especifique Numero de TSN/TSO/CSN/CSO', required=False)
    item19 =  forms.BooleanField(required=False,label='19) Material Safety Data Sheet',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item20 =  forms.BooleanField(required=False,label='20) Material con restriccion bajo el programa ESD',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item21 =  forms.BooleanField(required=False,label='21) Material con restriccion de almacenamiento (Hielo Seco)',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    item22 =  forms.BooleanField(required=False,label='22) Cartilla Mantencion CMA Autorizado',widget=forms.CheckboxInput(attrs={'class': 'checkbox-custom'}),initial=False)
    n_item22 = forms.IntegerField(widget=forms.TextInput(attrs={"class":"form-control reducido",}),label='22.5) N° de Catilla Mantencion CMA Autorizado', required=False)
    estado_repuesto_fk = forms.ModelChoiceField(queryset=Estado_Repuesto.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingresa el Estado del Repuesto"}), label='Estado del Repuesto', required=False)
    # incoming_fk = forms.ModelChoiceField(queryset=Incoming.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Ingresa el SN O BN"}), label='Serial Number o Batch Number')
    incoming_fk = forms.ModelChoiceField(queryset=Incoming.objects.all(), widget=forms.HiddenInput(), label='')
    licencia = forms.ModelChoiceField(queryset=Licencia.objects.all(), widget=forms.Select(attrs={"class": "select2-selection select2-selection--single","placeholder": "Licencia"}), label='Licencia')

    class Meta:
        model = Detalle_Incoming
        fields = [
            'rcv_n',
            'modelo',
            'Proveedor',
            'taller_reparadora',
            'trabajo_solicitado',
            'propiedad',
            'ro_n',
            'wo_n',
            'aceptado',
            'licencia',
            'estado_repuesto_fk',
            'item1',
            'item2',
            'item3',
            'item4',
            'item5',
            'item6',
            'item7',
            'item8',
            'item9',
            'item10',
            'item11',
            'item12',
            'item13',
            'n_item13',
            'item14',
            'item15',
            'n_item15',           
            'item16',
            'n_item16',
            'item17',
            'n_item17',
            'item18',
            'n_item18tsn',
            'n_item18tso',
            'n_item18csn',
            'n_item18cso',
            'item19',
            'item20',
            'item21',
            'item22',
            'n_item22',
        ]

class ImpresoraForm(forms.Form):
    nombre_impresora = forms.ChoiceField(label="Selecciona una impresora", choices=[])
    cantidad_hojas = forms.IntegerField(
        label="Cantidad de hojas",
        min_value=1,
        initial=1  # Valor inicial predeterminado
    )

    def __init__(self, *args, **kwargs):
        impresoras = kwargs.pop('impresoras', [])
        super(ImpresoraForm, self).__init__(*args, **kwargs)
        self.fields['nombre_impresora'].choices = [(impresora, impresora) for impresora in impresoras]

class OrdenConsumoForm(forms.Form):
    fechainicio = forms.DateField(widget=forms.DateInput(attrs={"class": "form-control reducido", 'type':'date'}),label='Fecha de Inicio',required=True)
    fechatermino = forms.DateField(widget=forms.DateInput(attrs={'type':'date',"class": "form-control reducido"}), label='Fecha de Termino',required=True)
    compania = forms.ChoiceField(choices=COMPANIA,widget=forms.Select(attrs={"class": "form-control reducido"}),label='Compañía que Presenta',required=True)
    aduana = forms.CharField(initial='METROPOLITANA', widget=forms.TextInput(attrs={"class":"form-control reducido"}),label='Aduana de Presentacion', required=True)
    resolucion_habilitacion = forms.CharField(initial='8144 / 03-03-2020' , widget=forms.TextInput(attrs={"class":"form-control reducido"}),label='Resolucion de Habilitacion', required=True)
    orden_consumo = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control reducido"}),label='Orden de Consumos', required=True)
    