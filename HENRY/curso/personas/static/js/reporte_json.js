/* 
Antes de usar jQuery 
const mostrarContenido = () =>{
    var contenido = document.getElementById('parrafo1').innerHTML;
    alert(contenido);
}
*/
// Equivalente a lo anterior
/*
function mostrarContenido(){
    alert(contenido);
}
*/

/**
 * Ahora empleando jQuery
 * Ubicación: https://jquery.com/
 * https://htmlcheatsheet.com/jquery/
 */
$(document).ready(function(){

    $('#btnMostrar').click(function(){
        var contenido = $('#parrafo1').html();
        console.log(contenido);
        alert(contenido);
    })

    $('#btnObtener').click(function(){
        mensaje = { datos : '' };
        $.ajax({
            data: mensaje,
            url: 'http://localhost:8000/personas_api_json/',
            type: 'get',
            beforeSend:function(){
                $('#resultado').html('Procesando solicitud de datos...');
            },
            success:function(response){
                console.log(response);
            }
        })
    })
})


