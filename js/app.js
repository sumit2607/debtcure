document.addEventListener('DOMContentLoaded', () => {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-toggle');
    const nav = document.querySelector('.nav');

    mobileMenuBtn.addEventListener('click', () => {
        nav.classList.toggle('active');

        // Animate hamburger to X
        const spans = mobileMenuBtn.querySelectorAll('span');
        if (nav.classList.contains('active')) {
            spans[0].style.transform = 'rotate(45deg) translate(5px, 6px)';
            spans[1].style.opacity = '0';
            spans[2].style.transform = 'rotate(-45deg) translate(5px, -6px)';
        } else {
            spans[0].style.transform = 'none';
            spans[1].style.opacity = '1';
            spans[2].style.transform = 'none';
        }
    });

    // Sticky Header
    const header = document.getElementById('main-header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            header.style.boxShadow = '0 4px 12px rgba(0,0,0,0.05)';
            header.style.padding = '0';
        } else {
            header.style.boxShadow = 'none';
        }
    });

    // Smooth Scrolling for Anchors
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
                // Close mobile menu if open
                if (nav.style.display === 'block' && window.innerWidth <= 900) {
                    nav.style.display = 'none';
                }
            }
        });
    });

    // FAQ Architecture
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        question.addEventListener('click', () => {
            // Close other items
            faqItems.forEach(otherItem => {
                if (otherItem !== item) {
                    otherItem.classList.remove('active');
                }
            });
            // Toggle current
            item.classList.toggle('active');
        });
    });

    // Modal Logic
    const modal = document.getElementById('lead-modal');
    const closeBtn = document.querySelector('.close-modal');
    const consultBtns = document.querySelectorAll('.btn-primary'); // All primary buttons trigger modal

    // Open modal on button clicks (except submit)
    consultBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (btn.type !== 'submit') {
                e.preventDefault();
                modal.style.display = 'flex';
                document.body.style.overflow = 'hidden'; // Prevent scrolling
            }
        });
    });

    // Close modal
    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    });

    // Close on outside click
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
            document.body.style.overflow = 'auto';
        }
    });

    // Exit Intent Popup
    let exitIntentShown = false;
    document.addEventListener('mouseleave', (e) => {
        if (e.clientY < 0 && !exitIntentShown) {
            modal.style.display = 'flex';
            exitIntentShown = true;
        }
    });

    // Form Submission Placeholder
    const form = document.getElementById('lead-form');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const btn = form.querySelector('button');
        const originalText = btn.innerText;

        btn.innerText = 'Submitting...';
        btn.disabled = true;

        // Simulate API call
        setTimeout(() => {
            alert('Thank you! Your request has been received. Our legal expert will call you shortly.');
            modal.style.display = 'none';
            btn.innerText = originalText;
            btn.disabled = false;
            form.reset();
            document.body.style.overflow = 'auto';
        }, 1500);
    });

    // Intersection Observer for Animations
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Add fade-in-up class to sections/elements to animate
    const animatedElements = document.querySelectorAll('.service-card, .feature-item, .section-title, .hero-text, .rights-content, .scenario-card');
    animatedElements.forEach(el => {
        el.classList.add('fade-in-up');
        observer.observe(el);
    });

    // Hero Carousel Auto-Rotation
    const slides = document.querySelectorAll('.carousel-slide');
    if (slides.length > 0) {
        let currentSlide = 0;
        const slideInterval = 4000; // 4 seconds

        setInterval(() => {
            // Remove active class from current
            slides[currentSlide].classList.remove('active');
            // Move to next
            currentSlide = (currentSlide + 1) % slides.length;
            // Add active class to new
            slides[currentSlide].classList.add('active');
        }, slideInterval);
    }
});
