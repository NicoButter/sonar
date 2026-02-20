// JavaScript para el efecto de "shrink"
window.onscroll = function() {shrinkHeader()};

function shrinkHeader() {
    var header = document.querySelector("header"); // Seleccionamos el header
    if (window.pageYOffset > 50) { // Si el scroll es mayor a 50px
        header.classList.add("shrunken"); // Añadimos la clase 'shrunken'
    } else {
        header.classList.remove("shrunken"); // Quitamos la clase 'shrunken' cuando volvemos arriba
    }
}

shrinkHeader();
