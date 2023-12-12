$(document).ready(function () {
    var dataTable = $('#tabla-incoming').DataTable({
        // scrollY: true,
        // scrollX: true,
        searching: false,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "{% url 'obtener_datos_incoming' %}",
            "type": "GET",
            "data": function (d) {
                d.e = '{{ query_inco }}';
            }

        },
        "columns": [
            // Define las columnas que deseas mostrar
            { "data": "sn_batch_pk" },
            { "data": "categoria_fk" },
            { "data": "part_number" },
            { "data": "descripcion" },
            { "data": "qty" },
            { "data": "f_vencimiento" },
            { "data": "usuario" },
            { "data": "saldo" },

            {
                "data": null,
                "render": function (data, type, row, meta) {
                    var sn_batch_pk = data.sn_batch_pk;
                    var url = "/detalle_incoming/" + sn_batch_pk + "/";
                    return '<a href="' + url + '" class="ver-detalles" data-sn_batch_pk="' + sn_batch_pk + '">Detalles</a>';
                }
            }
        ]
    });
});


$(document).ready(function () {
    var dataTable = $('#tabla-comat').DataTable({
        // scrollY: true,
        // scrollX: true,
        searching: false,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "{% url 'obtener_datos_comat' %}",
            "type": "GET",
            "data": function (d) {
                d.c = '{{ query_comat }}';
            }

        },
        "columns": [
            // Define las columnas que deseas mostrar
            { "data": "stdf_pk" },
            { "data": "awb" },
            { "data": "hawb" },
            { "data": "num_manifiesto" },
            { "data": "sum_cif" },
            { "data": "bodega_fk" },
            { "data": "usuario" },
            {
                "data": null,
                "render": function (data, type, row, meta) {
                    var stdf_pk = data.stdf_pk;
                    var url = "/detalle_comat/" + stdf_pk + "/";
                    return '<a href="' + url + '" class="ver-detalles" data-stdf_pk="' + stdf_pk + '">Ver Detalles</a>';
                }
            },
        ]
    });
});




$(document).ready(function () {
    var goTopButton = $("#goTopButton");

    // Inicialmente oculta el botón
    goTopButton.hide();

    // Mostrar el botón cuando el usuario desplaza hacia abajo 200px
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            goTopButton.fadeIn(100); // Animación de desvanecimiento en 300ms
        } else {
            goTopButton.fadeOut(100); // Animación de desvanecimiento en 300ms
        }
    });

    // Volver arriba cuando se hace clic en el botón
    goTopButton.click(function () {
        $("html, body").animate({ scrollTop: 0 }, "fast");
    });
});

document.addEventListener('DOMContentLoaded', function () {
    var item18 = document.getElementById('id_form2-item18');
    var item18tsn = document.getElementById('id_form2-item_18tsn');
    var n_item18tsn = document.getElementById('id_form2-n_item18tsn');

    function disableField(field) {
        field.disabled = true;
        field.parentNode.style.display = 'none';
    }

    function enableField(field) {
        field.disabled = false;
        field.parentNode.style.display = 'block';
    }

    item18.addEventListener('change', function () {
        if (item18.value === '1' || item18.value === '' || item18.value === 'N/A') { // Cambia '1' a 'NO' para desactivar los campos en caso de "NO"
            disableField(item18tsn);
            disableField(n_item18tsn);
        } else {
            enableField(item18tsn);
            enableField(n_item18tsn);
        }
    });

    // Inicialmente, ocultar y desactivar los campos si la opción seleccionada en item18 es "NO"
    if (item18.value === '1' || item18.value === '' || item18.value === 'N/A') {
        disableField(item18tsn);
        disableField(n_item18tsn);
    }
});

document.addEventListener('DOMContentLoaded', function () {
    var item13 = document.getElementById('id_form2-item13');
    var n_item13 = document.getElementById('id_form2-n_item13');


    function disableField(field) {
        field.disabled = true;
        field.parentNode.style.display = 'none';
    }

    function enableField(field) {
        field.disabled = false;
        field.parentNode.style.display = 'block';
    }

    item13.addEventListener('change', function () {
        if (item13.value === '1' || item13.value === '' || item13.value === 'N/A') { // Cambia '1' a 'NO' para desactivar los campos en caso de "NO"
            disableField(n_item13);

        } else {
            enableField(n_item13);

        }
    });

    // Inicialmente, ocultar y desactivar los campos si la opción seleccionada en item13 es "NO"
    if (item13.value === '1' || item13.value === '' || item13.value === 'N/A') {
        disableField(n_item13);

    }
});


document.addEventListener('DOMContentLoaded', function () {
    var item15 = document.getElementById('id_form2-item15');
    var n_item15 = document.getElementById('id_form2-n_item15');


    function disableField(field) {
        field.disabled = true;
        field.parentNode.style.display = 'none';
    }

    function enableField(field) {
        field.disabled = false;
        field.parentNode.style.display = 'block';
    }

    item15.addEventListener('change', function () {
        if (item15.value === '1' || item15.value === '' || item15.value === 'N/A') { // Cambia '1' a 'NO' para desactivar los campos en caso de "NO"
            disableField(n_item15);

        } else {
            enableField(n_item15);

        }
    });

    // Inicialmente, ocultar y desactivar los campos si la opción seleccionada en item13 es "NO"
    if (item15.value === '1' || item15.value === '' || item15.value === 'N/A') {
        disableField(n_item15);

    }
});

document.addEventListener('DOMContentLoaded', function () {
    var item22 = document.getElementById('id_form2-item22');
    var n_item22 = document.getElementById('id_form2-n_item22');


    function disableField(field) {
        field.disabled = true;
        field.parentNode.style.display = 'none';
    }

    function enableField(field) {
        field.disabled = false;
        field.parentNode.style.display = 'block';
    }

    item22.addEventListener('change', function () {
        if (item22.value === '1' || item22.value === '' || item22.value === 'N/A') { // Cambia '1' a 'NO' para desactivar los campos en caso de "NO"
            disableField(n_item22);

        } else {
            enableField(n_item22);

        }
    });

    // Inicialmente, ocultar y desactivar los campos si la opción seleccionada en item13 es "NO"
    if (item22.value === '1' || item22.value === '' || item22.value === 'N/A') {
        disableField(n_item22);

    }
});


// $(".selector").flatpickr(optional_config);

flatpickr("input[type=datetime-local]", {
    enableTime: true,
    allowInput: true,
    ariaDateFormat: 'd-m-Y H:i',
    dateFormat: "Y-m-d H:i",
    time_24hr: true,
});

flatpickr("input[type=date]", {
    allowInput: true,
    altFormat: 'd-m-Y',
    dateFormat: "Y-m-d",
});






$(document).ready(function () {
    $('#id_form1-incoming_fk').select2({ 'placeholder': 'Seleccione Serial Number o Batch Number' });
    $('#id_bodega_fk').select2({ 'placeholder': 'Seleccione Bodega' });
    $('#id_origen_fk').select2({ 'placeholder': 'Seleccione Origen' });
    $('#id_ubicacion_fk').select2({ 'placeholder': 'Seleccione Ubicación' });
    $('#id_clasificacion_fk').select2({ 'placeholder': 'Seleccione Clasificación' });
    $('#id_uom_fk').select2({ 'placeholder': 'Seleccione UOM' });
    $('#id_condicion_fk').select2({ 'placeholder': 'Seleccione Condición' });
    $('#id_ficha_fk').select2({ 'placeholder': 'Seleccione N° de Ficha' });
    $('#id_stdf_fk').select2({ 'placeholder': 'Seleccione STDF' });
    $('#id_incoming_fk').select2({ 'placeholder': 'Seleccione Serial/Batch Number' });
    $('#id_owner_fk').select2({ 'placeholder': 'Seleccione Owner' });
    $('#id_categoria_fk').select2({ 'placeholder': 'Seleccione Categoria' });

});

$(document).ready(function () {
    var dataTable = $('#tabla-consumos').DataTable({
        // scrollY: true,
        // scrollX: true,
        searching: false,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "{% url 'obtener_datos_consumos' %}",
            "type": "GET",
            "data": function (d) {
                d.t = '{{ query_consu }}';
            }

        },
        "columns": [
            // Define las columnas que deseas mostrar
            { "data": "consumo_pk" },
            { "data": "incoming_fk" },
            { "data": "f_transaccion" },
            { "data": "matricula_aeronave" },
            { "data": "orden_consumo" },
            { "data": "qty_extraida" },
            { "data": "usuario" },
            {
                "data": null,
                "render": function (data, type, row, meta) {
                    var consumo_pk = data.consumo_pk;
                    var url = "/detalle_consumos/" + consumo_pk + "/";
                    return '<a href="' + url + '" class="ver-detalles" data-consumo_pk="' + consumo_pk + '">Detalles</a>';
                }
            }
        ]
    });
});
// // Test
//         $(document).ready(function () {
//             // Inicializa el elemento select2
//             $('#id_stdf_fk').select2({
//                 placeholder: 'Selecciona una opción',
//                 ajax: {
//                     url: '/obtener_stdf_incoming/', // La URL donde obtendrás los datos desde Django
//                     dataType: 'json',
//                     // delay: 250,
//                     data: function (params) {
//                         return {
//                             q: params.term // Enviar el término de búsqueda como parámetro de consulta
//                         };
//                     },
//                     processResults: function (data) {
//                         // Modifica la estructura de los resultados si es necesario
//                         const modifiedResults = data.stdf_data.map(item => {
//                             return {
//                                 id: item.stdf_pk,
//                                 text: item.stdf_pk,
//                             };
//                         });
//                         console.log('modifiedResults:', modifiedResults);

//                         return {
//                             results: modifiedResults
//                         };
//                     },
//                     cache: false,
//                     error: function (xhr, textStatus, errorThrown) {
//                         console.error('Error en la solicitud AJAX:', errorThrown);
//                     }
//                 }
//             });
//         });




$(document).ready(function () {
    var dataTableIncoming = $('#tabla-inicio').DataTable({
        scrollY: true,
        scrollX: true,
        searching: false,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "{% url 'buscar_datos_inicio' %}",
            "type": "GET",
            "data": function (d) {
                d.n = '{{ query_inicio }}';
            },
            "dataSrc": "data_incoming"
        },
        "columns": [
            // Define las columnas que deseas mostrar para Incoming
            { "data": "sn_batch_pk" },
            { "data": "categoria_fk__name_categoria" },
            { "data": "part_number" },
            { "data": "descripcion" },
            { "data": "stdf_fk__stdf_pk" },
            { "data": "qty" },
            { "data": "qty_extraida_total" },
            { "data": "saldo" },
            { "data": "stdf_fk__awb" },
            { "data": "stdf_fk__num_manifiesto" },
            { "data": "owner_fk__name_owner" },
            { "data": "ubicacion_fk__name_ubicacion" },
            { "data": "f_vencimiento" },
            {
                "data": null,
                "render": function (data, type, row, meta) {

                    var stdf_fk__stdf_pk = data.stdf_fk__stdf_pk;
                    var url = "/detalle_inicio/" + stdf_fk__stdf_pk + "/";
                    return '<a href="' + url + '" class="ver-detalles" data-stdf_fk__stdf_pk="' + stdf_fk__stdf_pk + '">Detalles</a>';
                }
            }
        ]

    });

    var dataTableComatsSinIncoming = $('#tabla-inicio-no-incomings').DataTable({
        searching: true,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "{% url 'buscar_datos_inicio' %}",
            "type": "GET",
            "data": function (d) {
                d.n = '{{ query_inicio }}';
            },
            "dataSrc": "data_comats_sin_incoming",

        },
        "columns": [
            // Define las columnas que deseas mostrar para Comats sin Incoming
            { "data": "stdf_pk" },
            { "data": "awb" },
            { "data": "hawb" },
            { "data": "prioridad" },

        ]


    });
});


// Configuración del DataTable secundario para comat_data
$(document).ready(function () {
    var url = window.location.pathname;
    var stdf_pk = url.split('/').slice(-2, -1)[0];

    // Configuración del DataTable secundario para comat_data
    var incomingDataTable = $('#tabla-detalle-incoming').DataTable({
        searching: true,
        searchParams: ["search"],
        responsive: true,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "{% url 'detalle_inicio' 0 %}".replace(0, stdf_pk),
            "type": "GET",
            "data": function (d) {
                d.format = 'json';
            },
            "dataSrc": function (json) {
                return json.incoming_data;
            }
        },
        "columns": [
            { "data": "sn_batch_pk", "width": "10%" },
            { "data": "part_number", "width": "10%" },
            { "data": "f_incoming", "width": "10%" },
            { "data": "descripcion", "width": "10%" },
            { "data": "po", "width": "10%" },
            { "data": "qty", "width": "10%" },
            { "data": "u_purchase_cost", "width": "10%" },
            { "data": "total_u_purchase_cost", "width": "10%" },
            { "data": "f_vencimiento", "width": "10%" },
            { "data": "saldo", "width": "10%" },
            { "data": "categoria_fk", "width": "10%" },
            { "data": "clasificacion_fk", "width": "10%" },
            { "data": "ubicacion_fk", "width": "10%" },
            { "data": "uom_fk", "width": "10%" },
            { "data": "owner_fk", "width": "10%" },
            { "data": "condicion_fk", "width": "10%" },
            { "data": "ficha_fk", "width": "10%" },
            { "data": "observaciones", "width": "10%" },
        ],

    });

    // Configuración del DataTable secundario para consumos_data
    var consumosDataTable = $('#tabla-detalle-consumos').DataTable({
        searching: true,
        responsive: true,
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "{% url 'detalle_inicio' 0 %}".replace(0, stdf_pk),
            "type": "GET",
            "data": function (c) {
                c.format = 'json';
            },
            "dataSrc": "consumos_data"
        },
        "columns": [
            { "data": "incoming_fk", "width": "10%" },
            { "data": "orden_consumo", "width": "10%" },
            { "data": "f_transaccion", "width": "10%" },
            { "data": "qty_extraida", "width": "10%" },
            { "data": "matricula_aeronave", "width": "10%" },
            { "data": "observaciones", "width": "10%" },
        ],


    });

});
// Agrega un controlador de eventos para cerrar la ventana emergente cuando se hace clic en cualquier parte del documento
document.addEventListener('click', function (event) {
    const modal = document.getElementById('myModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});
var ctx = document.getElementById('myChart').getContext('2d');
var myChart;

// Realiza la petición AJAX para obtener los datos
fetch('/get_chart_data/')  // Cambia la URL según tu configuración
    .then(response => response.json())
    .then(data => {
        const labels = data.map(item => item.prioridad);
        const counts = data.map(item => item.count);
        const colors = data.map(item => item.color);
        myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.map(item => item.prioridad),
                datasets: [{
                    label: 'Cuenta Total de Prioridad por STDF',
                    data: counts,
                    backgroundColor: colors, // Personaliza según tus necesidades
                    borderColor: 'rgba(75, 192, 192, 1)', // Personaliza según tus necesidades
                    borderWidth: 1
                }]
            },
            options: {
                // Otras opciones de configuración
                // Configuración del gráfico
                onClick: function (event, elements) {
                    if (elements[0]) {
                        const clickedLabel = labels[elements[0].index];
                        const modal = document.getElementById('myModal');
                        const modalContent = document.getElementById('modal-content');
                        // Agrega un controlador de eventos para cerrar la ventana emergente
                        const closeBtn = document.querySelector('.close');
                        closeBtn.addEventListener('click', function () {
                            modal.style.display = 'none';
                        });
                        // Consulta los pk de elementos relacionados con la prioridad
                        fetch(`/get_pks_by_priority/${clickedLabel}/`)
                            .then(response => response.json())
                            .then(data => {
                                const stdfPkList = data.stdf_pk;

                                // Personaliza el mensaje de la ventana emergente
                                let message = `Los elementos con prioridad ${clickedLabel} tienen los siguientes stdf_pk en fila:<br>`;
                                for (const stdfPk of stdfPkList) {
                                    message += `${stdfPk}, `;
                                }
                                message = message.slice(0, -2); // Eliminar la coma final
                                modalContent.innerHTML = message;
                            })
                            .catch(error => {
                                console.error('Error al obtener los stdf_pk:', error);
                            });

                        // Mostrar la ventana emergente
                        modal.style.display = 'block';
                    }
                }
            }
        });
    });
