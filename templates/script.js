$(document).ready(function() {
    $.ajax({
        url: 'https://colab.research.google.com/drive/1OMVWX57KJR7wuENpBs0rVhCVoZ8sCL-s#scrollTo=XCEKpQ_HD53b',  // Reemplaza con la URL de tu API
        method: 'GET',
        dataType: 'json',
        success: function(response) {
            var apiDataElement = $('#api-data');
            
            // Limpia el contenido existente
            apiDataElement.empty();
            
            // Recorre los datos y agrega elementos de lista a la página
            response.forEach(function(item) {
                var listItem = $('<li>').text(item);
                apiDataElement.append(listItem);
            });
        },
        error: function() {
            console.log('Error al obtener los datos de la API');
        }
    });
});
