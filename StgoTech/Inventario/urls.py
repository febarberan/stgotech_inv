from django.urls import path
from . import views
from . import exportar_excel
from . import imprimir_excel
from . import orden_consumo
from . import inventarios

urlpatterns = [
    path('', views.redirect_login, name='redirect_login'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('index/', views.index, name='index'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('comat/', views.comat, name='comat'),
    path('incoming/<str:stdf_pk>/', views.incoming, name='incoming'),
    path('consumos/<int:incoming_fk>/', views.consumos, name='consumos'),
    path('buscar_productos_inicio/', views.buscar_productos_inicio, name='buscar_productos_inicio'),
    path('buscar/', views.buscar_productos, name='buscar_stdf'),
    path('buscar_incoming/', views.buscar_productos_incoming, name='buscar_productos_incoming'),
    path('buscar_productos_consumos/', views.buscar_productos_consumos, name='buscar_productos_consumos'),
    path('obtener_datos_consumos/', views.obtener_datos_consumos, name='obtener_datos_consumos'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('get_chart_data/', views.get_chart_data, name='get_chart_data'),
    path('get_chart_data_repuesto_owner/', views.get_chart_data_repuesto_owner, name='get_chart_data_repuesto_owner'),
    path('top_10_lowest_saldo/', views.top_10_lowest_saldo, name='top_10_lowest_saldo'),
    path('soon_to_expire_parts/', views.soon_to_expire_parts, name='soon_to_expire_parts'),
    path('monthly_weight_chart/', views.monthly_weight_chart, name='monthly_weight_chart'),
    path('monthly_cif_chart/', views.monthly_cif_chart, name='monthly_cif_chart'),
    path('state_pie_chart/', views.state_pie_chart, name='state_pie_chart'),
    path('get_pks_by_priority/<str:priority>/', views.get_pks_by_priority, name='get_pks_by_priority'),
    path('obtener_stdf_incoming/', views.obtener_datos_stdf_incoming, name='obtener_stdf_incoming'),
    path('obtener_sn_consumo/', views.obtener_datos_sn_consumos, name='obtener_sn_consumo'),
    path('obtener_datos_comat/', views.obtener_datos_comat, name='obtener_datos_comat'),
    path('obtener_datos_incoming/', views.obtener_datos_incoming, name='obtener_datos_incoming'),
    path('buscar_datos_inicio/', views.buscar_datos_inicio, name='buscar_datos_inicio'),
    path('detalle_comat/<str:stdf_pk>/', views.detalle_comat, name='detalle_comat'),
    path('detalle_incoming/<str:id_incoming>/', views.detalle_incoming, name='detalle_incoming'),
    path('mostrar_ingreso/', views.mostrar_ingreso , name = 'mostrar_ingreso'),
    path('ingreso/', views.ingreso , name = 'ingreso'),
    path('detalle_consumos/<int:consumo_pk>/', views.detalle_consumos, name='detalle_consumos'),
    path('detalle_inicio/<str:stdf_pk>/', views.detalle_inicio, name='detalle_inicio'),
    path('exportar_excel_incoming/<str:id_incoming>/', exportar_excel.exportar_excel_incoming, name='exportar_excel_incoming'),
    path('detalle_form/<int:incoming_fk>/', views.detalle_form, name='detalle_form'),
    # path('imprimir_excel_incoming/<str:sn_batch_pk>/', imprimir_excel.imprimir_excel_incoming, name='imprimir_excel_incoming'),
    # path('seleccionarimpresora/<str:sn_batch_pk>/', imprimir_excel.seleccionarimpresora, name='seleccionarimpresora'),
    path('orden_consumo/', orden_consumo.orden_consumos, name='orden_consumo'),
    # path('impresoras/', imprimir_excel.impresoras, name='impresoras'),
    path('estadostdf/', views.estadostdf, name='estadostdf'),
    #inventarios
    path('inventario_comat/', inventarios.inventario_comat, name='inventario_comat'),
    path('inventario_incoming/', inventarios.inventario_incoming, name='inventario_incoming'),
    #mantenedores all
    path('mantenedores/', views.mantenedores_all, name='mantenedores'),
    #mantenedores comat
    path('editar_comat/<str:stdf_pk>/', views.editar_comat, name='editar_comat'),
    path('eliminar_comat/<str:stdf_pk>/', views.eliminar_comat, name='eliminar_comat'),
    #mantenedores incoming
    path('editar_incoming/<str:id_incoming>/', views.editar_incoming, name='editar_incoming'),
    path('eliminar_incoming/<str:id_incoming>/', views.eliminar_incoming, name='eliminar_incoming'),
    #mantenedores consumo
    path('editar_consumo/<int:consumo_pk>/', views.editar_consumo, name='editar_consumo'),
    path('eliminar_consumo/<int:consumo_pk>/', views.eliminar_consumo, name='eliminar_consumo'),
    #mantenedores detalle incoming form
    path('editar_detalle_incoming_form/<str:id_incoming>/', views.editar_detalle_incoming_form, name='editar_detalle_incoming_form'),
    #mantenedores categoria incoming
    #path('mantenedor_categoria_incoming/', views.mantenedor_categoria_incoming, name='mantenedor_categoria_incoming'),
    # path('editar_categoria_incoming/<int:categoria_pk>/', views.editar_categoria_incoming, name='editar_categoria_incoming'),
    # path('registrar_categoria_incoming/', views.registrar_categoria_incoming, name='registrar_categoria_incoming'),
    # path('eliminar_categoria_incoming/<int:categoria_pk>', views.eliminar_categoria_incoming, name='eliminar_categoria_incoming'),

    #mantenedores estado
    path('mantenedor_estado/', views.mantenedor_estado, name='mantenedor_estado'),
    path('editar_estado/<int:estado_pk>/', views.editar_estado, name='editar_estado'),
    path('registrar_estado/', views.registrar_estado, name='registrar_estado'),
    path('eliminar_estado/<int:estado_pk>', views.eliminar_estado, name='eliminar_estado'),
    #mantenedores ubicacion
    path('mantenedor_ubicacion/', views.mantenedor_ubicacion, name='mantenedor_ubicacion'),
    path('editar_ubicacion/<int:ubicacion_pk>/', views.editar_ubicacion, name='editar_ubicacion'),
    path('registrar_ubicacion/', views.registrar_ubicacion, name='registrar_ubicacion'),
    path('eliminar_ubicacion/<int:ubicacion_pk>', views.eliminar_ubicacion, name='eliminar_ubicacion'),
    #mantenedores uom
    path('mantenedor_uom/', views.mantenedor_uom, name='mantenedor_uom'),
    path('editar_uom/<int:uom_pk>/', views.editar_uom, name='editar_uom'),
    path('registrar_uom/', views.registrar_uom, name='registrar_uom'),
    path('eliminar_uom/<int:uom_pk>', views.eliminar_uom, name='eliminar_uom'),
    #mantenedores owner
    path('mantenedor_owner/', views.mantenedor_owner, name='mantenedor_owner'),
    path('editar_owner/<int:owner_pk>/', views.editar_owner, name='editar_owner'),
    path('registrar_owner/', views.registrar_owner, name='registrar_owner'),
    path('eliminar_owner/<int:owner_pk>', views.eliminar_owner, name='eliminar_owner'),
    #mantenedores ficha
    path('mantenedor_ficha/', views.mantenedor_ficha, name='mantenedor_ficha'),
    path('editar_ficha/<int:ficha_pk>/', views.editar_ficha, name='editar_ficha'),
    path('registrar_ficha/', views.registrar_ficha, name='registrar_ficha'),
    path('eliminar_ficha/<int:ficha_pk>', views.eliminar_ficha, name='eliminar_ficha'),
    #mantenedores condition
    path('mantenedor_condition/', views.mantenedor_condition, name='mantenedor_condition'),
    path('editar_condition/<int:condicion_pk>/', views.editar_condition, name='editar_condition'),
    path('registrar_condition/', views.registrar_condition, name='registrar_condition'),
    path('eliminar_condition/<int:condicion_pk>', views.eliminar_condition, name='eliminar_condition'),
    #mantenedores bodega
    path('mantenedor_bodega/', views.mantenedor_bodega, name='mantenedor_bodega'),
    path('editar_bodega/<int:bodega_pk>/', views.editar_bodega, name='editar_bodega'),
    path('registrar_bodega/', views.registrar_bodega, name='registrar_bodega'),
    path('eliminar_bodega/<int:bodega_pk>', views.eliminar_bodega, name='eliminar_bodega'),
    #mantenedores origen
    path('mantenedor_origen/', views.mantenedor_origen, name='mantenedor_origen'),
    path('editar_origen/<int:origen_pk>/', views.editar_origen, name='editar_origen'),
    path('registrar_origen/', views.registrar_origen, name='registrar_origen'),
    path('eliminar_origen/<int:origen_pk>', views.eliminar_origen, name='eliminar_origen'),
    #mantenedores cargo
    path('mantenedor_cargo/', views.mantenedor_cargo, name='mantenedor_cargo'),
    path('editar_cargo/<int:id>/', views.editar_cargo, name='editar_cargo'),
    path('registrar_cargo/', views.registrar_cargo, name='registrar_cargo'),
    path('eliminar_cargo/<int:id>', views.eliminar_cargo, name='eliminar_cargo'),
    #mantenedores clasificacion
    path('mantenedor_clasificacion/', views.mantenedor_clasificacion, name='mantenedor_clasificacion'),
    path('editar_clasificacion/<int:clasificacion_pk>/', views.editar_clasificacion, name='editar_clasificacion'),
    path('registrar_clasificacion/', views.registrar_clasificacion, name='registrar_clasificacion'),
    path('eliminar_clasificacion/<int:clasificacion_pk>', views.eliminar_clasificacion, name='eliminar_clasificacion'),
    #mantenedores consumidor
    path('mantenedor_consumidor/', views.mantenedor_consumidor, name='mantenedor_consumidor'),
    path('editar_consumidor/<int:id>/', views.editar_consumidor, name='editar_consumidor'),
    path('registrar_consumidor/', views.registrar_consumidor, name='registrar_consumidor'),
    path('eliminar_consumidor/<int:id>', views.eliminar_consumidor, name='eliminar_consumidor'),
    #mantenedores compañia
    path('mantenedor_compañia/', views.mantenedor_compañia, name='mantenedor_compañia'),
    path('editar_compañia/<int:cod_compania>/', views.editar_compañia, name='editar_compañia'),
    path('registrar_compañia/', views.registrar_compañia, name='registrar_compañia'),
    path('eliminar_compañia/<int:cod_compania>', views.eliminar_compañia, name='eliminar_compañia'),
    #mantenedores estado_repuesto
    path('mantenedor_estado_repuesto/', views.mantenedor_estado_repuesto, name='mantenedor_estado_repuesto'),
    path('editar_estado_repuesto/<int:id>/', views.editar_estado_repuesto, name='editar_estado_repuesto'),
    path('registrar_estado_repuesto/', views.registrar_estado_repuesto, name='registrar_estado_repuesto'),
    path('eliminar_estado_repuesto/<int:id>', views.eliminar_estado_repuesto, name='eliminar_estado_repuesto'),
    #mantenedores licencia
    path('mantenedor_licencia/', views.mantenedor_licencia, name='mantenedor_licencia'),
    path('editar_licencia/<int:id>/', views.editar_licencia, name='editar_licencia'),
    path('registrar_licencia/', views.registrar_licencia, name='registrar_licencia'),
    path('eliminar_licencia/<int:id>', views.eliminar_licencia, name='eliminar_licencia'),
]