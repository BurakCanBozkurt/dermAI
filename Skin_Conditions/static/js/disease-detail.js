// Navbar Toggle Fonksiyonu
function toggleNavbar() {
    const navbarLinks = document.querySelector('.navbar-links');
    navbarLinks.classList.toggle('active');
}

// Görsel Galerisi Fonksiyonları
function changeMainImage(thumbnail) {
    const mainImage = document.querySelector('.main-image img');
    const thumbnailImage = thumbnail.querySelector('img');
    
    // Ana görsel ile thumbnail'ı değiştir
    const tempSrc = mainImage.src;
    mainImage.src = thumbnailImage.src;
    thumbnailImage.src = tempSrc;

    // Aktif thumbnail'ı işaretle
    document.querySelectorAll('.thumbnail').forEach(thumb => {
        thumb.classList.remove('active');
    });
    thumbnail.classList.add('active');
}

// İçerik Navigasyonu Fonksiyonları
function updateActiveNavItem() {
    const sections = document.querySelectorAll('.section');
    const navItems = document.querySelectorAll('.nav-item');
    
    let currentSection = '';
    
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 190;
        const sectionHeight = section.clientHeight;
        const scroll = window.pageYOffset;
        
        if (scroll >= sectionTop && scroll < sectionTop + sectionHeight) {
            currentSection = section.getAttribute('id');
        }
    });
    
    navItems.forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('href').slice(1) === currentSection) {
            item.classList.add('active');
        }
    });
}

// SSS Toggle Fonksiyonu
function toggleFaq(question) {
    const faqItem = question.parentElement;
    const isActive = faqItem.classList.contains('active');
    
    // Diğer tüm SSS öğelerini kapat
    document.querySelectorAll('.faq-item').forEach(item => {
        item.classList.remove('active');
    });

    // Seçili SSS öğesini aç/kapat
    if (!isActive) {
        faqItem.classList.add('active');
    }
}

// Smooth Scroll Fonksiyonu
function smoothScroll(target, duration) {
    const targetElement = document.querySelector(target);
    const targetPosition = targetElement.offsetTop - 150;
    const startPosition = window.pageYOffset;
    const distance = targetPosition - startPosition;
    let startTime = null;

    function animation(currentTime) {
        if (startTime === null) startTime = currentTime;
        const timeElapsed = currentTime - startTime;
        const run = ease(timeElapsed, startPosition, distance, duration);
        window.scrollTo(0, run);
        if (timeElapsed < duration) requestAnimationFrame(animation);
    }

    function ease(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t + b;
        t--;
        return -c / 2 * (t * (t - 2) - 1) + b;
    }

    requestAnimationFrame(animation);
}

// Sayfa yüklendiğinde
document.addEventListener('DOMContentLoaded', function() {
    // AOS kütüphanesini başlat
    AOS.init({
        duration: 800,
        once: true,
        offset: 100
    });

    // Navbar scroll efekti
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
            navbar.style.backdropFilter = 'blur(10px)';
        } else {
            navbar.style.backgroundColor = 'var(--white)';
            navbar.style.backdropFilter = 'none';
        }
        
        // İçerik navigasyonunu güncelle
        updateActiveNavItem();
    });

    // Smooth scroll için tüm iç linkleri seç
    document.querySelectorAll('.nav-item').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            smoothScroll(targetId, 1000);
        });
    });
}); 