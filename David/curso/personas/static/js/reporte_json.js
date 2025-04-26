/* const mostrarContenido = () =>{
    var contenido = document.getElementById('parrafo').innerHTML;
    alert(contenido);
}
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
            url: 'http://localhost:8005/personas_api_json/',
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