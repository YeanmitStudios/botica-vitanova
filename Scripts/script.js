function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    
    // Si ya está activo, lo quitamos, si no, lo ponemos
    if (navLinks.style.display === 'flex') {
        navLinks.style.display = 'none';
    } else {
        navLinks.style.display = 'flex';
        navLinks.style.animation = 'fadeIn 0.3s ease';
    }
}