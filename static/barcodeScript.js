/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function showTypes() {
    document.getElementById("sortType").classList.toggle("show");
}
  
// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.sort-button')) {
        var types = document.getElementsByClassName("sort-type");
        for (var i = 0; i < types.length; i++) {
            var openTypes = types[i];
            if (openTypes.classList.contains('show')) {
            openTypes.classList.remove('show');
            }
        }
    }
}