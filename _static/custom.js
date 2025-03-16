document.addEventListener("DOMContentLoaded", function() {
    // Expand all nav items
    document.querySelectorAll('li.toctree-l1').forEach(function(item) {
        item.classList.add('current');
    });
    document.querySelectorAll('li.toctree-l2').forEach(function(item) {
        item.classList.add('current');
    });
    // Add more levels if needed (toctree-l3, toctree-l4, etc.)
});