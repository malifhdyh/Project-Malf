// Template slider functionality
function scrollTemplates(direction) {
    const grid = document.getElementById('templateGrid');
    const scrollAmount = 300 * direction;
    grid.scrollBy({
        left: scrollAmount,
        behavior: 'smooth'
    });
}

document.addEventListener('DOMContentLoaded', function() {
    // Optional: Add touch support for mobile
    const templateGrid = document.getElementById('templateGrid');
    let touchStartX = 0;
    let touchEndX = 0;

    templateGrid.addEventListener('touchstart', e => {
        touchStartX = e.changedTouches[0].screenX;
    });

    templateGrid.addEventListener('touchend', e => {
        touchEndX = e.changedTouches[0].screenX;
        if (touchStartX - touchEndX > 50) {
            scrollTemplates(1); // Scroll right
        } else if (touchEndX - touchStartX > 50) {
            scrollTemplates(-1); // Scroll left
        }
    });
});