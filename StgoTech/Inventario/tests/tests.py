from datetime import datetime
from django import urls
import pytest
from django.contrib.auth.models import User
from Inventario.models import *

# Creación de usuario BD
@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('test', 'test@test.com', '123asdzxc.')
  assert User.objects.count() == 1


# Creación de un objecto en la base de datos y comparación
@pytest.mark.django_db
def test_model_creation():
    obj = Bodega.objects.create(name_bodega="bodega_test")
    assert obj.name_bodega == "bodega_test"

#Creación de una query
@pytest.mark.django_db
def test_model_query():
    obj = Estado.objects.create(estado="Cancela_test")
    resultado = Estado.objects.get(estado="Cancela_test")
    assert resultado == obj


@pytest.mark.parametrize('param', [
	('dashboard'),
])

def test_render_views(client, param):
	temp_url = urls.reverse(param)
	resp = client.get(temp_url)
	assert resp.status_code == 200
	
@pytest.mark.django_db
def test_model_query1():
    obj = Cargo.objects.create(name_cargo="Mecanico")
    resultado = Cargo.objects.get(name_cargo="Mecanico")
    assert resultado == obj

@pytest.mark.django_db
def test_model_query2():
    obj = Ubicacion.objects.create(name_ubicacion="01-2432")
    resultado = Ubicacion.objects.get(name_ubicacion="01-2432")
    assert resultado == obj


@pytest.mark.django_db
def test_model_query3():
    # Crear objetos para cubrir todo el modelo
    obj1 = Comat.objects.create(stdf_pk=646533, awb="awb1", hawb="hawb1", num_manifiesto="manifiesto1",
                                corr_interno="corr1", pcs=10, peso=20.5, f_control=datetime.now(),
                                f_manifiesto=datetime.now(), f_recepcion=datetime.now(), f_stdf=datetime.now().date(),
                                fob=30.5, flete=15.5, seguro=5.5, sum_cif=60.5, observaciones="Observaciones1",
                                prioridad="Media", bodega_fk=Bodega.objects.create(name_bodega="Bodega1"),
                                origen_fk=Origen.objects.create(name_origen="Origen1"), estado_fk=Estado.objects.create(estado="Estado1"),
                                usuario=User.objects.create(username="usuario1"), compania_fk=Compania.objects.create(cod_compania=1, nom_compania="Compania1"))

    resultado1 = Comat.objects.get(stdf_pk=646533)
    assert resultado1 == obj1



