// JavaScript para el efecto de "shrink"
window.onscroll = function() {shrinkHeader()};

function shrinkHeader() {
    var header = document.querySelector("header"); // Seleccionamos el header
    if (window.pageYOffset > 50) { // Si el scroll es mayor a 50px
        header.classList.add("shrunken"); // Añadimos la clase 'shrunken'
        document.body.style.paddingTop = '60px'; // Ajustamos el padding del body
    } else {
        header.classList.remove("shrunken"); // Quitamos la clase 'shrunken' cuando volvemos arriba
        document.body.style.paddingTop = '150px'; // Restauramos el padding del body
    }
}
