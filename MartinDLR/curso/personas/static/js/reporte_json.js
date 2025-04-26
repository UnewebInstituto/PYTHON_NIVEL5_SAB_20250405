


/*<!-- antes de sin usar jquery-->
const mostrarContenido = ()=>{
    var contenido = document.getElementById('parrafo1').innerHTML
    alert(contenido)
  }
    */

  /* ahora usando jquery */
$(document).ready(function()
{
  $('#btnMostrar').click(function(){
  
    var contenido = $('#parrafo1').html();
    alert(contenido)
 })
$('#btnObtener').click(function(){

  mensaje = {datos:''};
    $.ajax(
      {
        data:mensaje,
        url:'http://localhost:8002/personas_procesa_json/',
        type: 'get',
        beforeSend:function()
          {
            $('#resultado').html('Procesando solicitud de datos...')
          },
        success:function(respuesta) 
          {
            console.log(respuesta)
          }
      }
    )
  })
})
  