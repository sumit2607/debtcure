/**
 * DebtCure - Main Application Logic
 */

// Global state
let nav;
let modal;
let exitIntentShown = false;

// Initialize all components
document.addEventListener('DOMContentLoaded', () => {
    initMobileMenu();
    initStickyHeader();
    initSmoothScroll();
    initFAQ();
    initModal();
    initLeadForm();
    initAnimations();
    initCarousel();
    initCalculator();
});

// Mobile Menu Toggle
function initMobileMenu() {
    const mobileMenuBtn = document.querySelector('.mobile-menu-toggle');
    nav = document.querySelector('.nav');

    if (!mobileMenuBtn || !nav) return;

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

    // Close menu when clicking links (mobile)
    const navLinks = nav.querySelectorAll('a');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 900) {
                nav.classList.remove('active');
                const spans = mobileMenuBtn.querySelectorAll('span');
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        });
    });
}

// Sticky Header
function initStickyHeader() {
    const header = document.getElementById('main-header');
    if (!header) return;

    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            header.style.boxShadow = '0 4px 12px rgba(0,0,0,0.05)';
            header.classList.add('scrolled');
        } else {
            header.style.boxShadow = 'none';
            header.classList.remove('scrolled');
        }
    });
}

// Smooth Scrolling
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;

            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                const headerOffset = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// FAQ Accordion
function initFAQ() {
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (!question) return;

        question.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            // Close all
            faqItems.forEach(i => i.classList.remove('active'));

            // Toggle current
            if (!isActive) {
                item.classList.add('active');
            }
        });
    });
}

// Modal Toggle Logic
function initModal() {
    modal = document.getElementById('lead-modal');
    const closeBtn = document.querySelector('.close-modal');
    const triggerButtons = document.querySelectorAll('#consultation-btn, #consultation-btn-sidebar, #calc-cta-btn, .btn-primary.small');

    if (!modal || !closeBtn) return;

    const openModal = () => {
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    };

    const closeModal = () => {
        modal.style.display = 'none';
        document.body.style.overflow = 'auto';
    };

    triggerButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            openModal();
        });
    });

    closeBtn.addEventListener('click', closeModal);

    window.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
    });

    // Exit Intent
    document.addEventListener('mouseleave', (e) => {
        if (e.clientY < 0 && !exitIntentShown) {
            openModal();
            exitIntentShown = true;
        }
    });
}

// Form Submission -> WhatsApp
function initLeadForm() {
    const form = document.getElementById('lead-form');
    if (!form) return;

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const name = form.querySelector('input[placeholder="Your Name"]').value;
        const phone = form.querySelector('input[placeholder="Phone Number"]').value;
        const issue = form.querySelector('textarea').value;
        const btn = form.querySelector('button');
        const originalText = btn.innerText;

        btn.innerText = 'Redirecting to WhatsApp...';
        btn.disabled = true;

        const message = `Hello DebtCure, I need legal advice.\n\n*Name:* ${name}\n*Phone:* ${phone}\n*Issue:* ${issue}`;
        const whatsappUrl = `https://wa.me/919076573857?text=${encodeURIComponent(message)}`;

        setTimeout(() => {
            window.open(whatsappUrl, '_blank');
            if (modal) {
                modal.style.display = 'none';
                document.body.style.overflow = 'auto';
            }
            btn.innerText = originalText;
            btn.disabled = false;
            form.reset();
        }, 800);
    });
}

// Reveal Animations
function initAnimations() {
    const observerOptions = { threshold: 0.1 };
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.service-card, .feature-item, .section-title, .hero-text, .rights-content, .testimonial-card, .marquee-container, .process-step, .process-timeline');
    animatedElements.forEach(el => {
        el.classList.add('fade-in-up');
        observer.observe(el);
    });
}

// Hero Carousel
function initCarousel() {
    const slides = document.querySelectorAll('.carousel-slide');
    if (slides.length <= 1) return;

    let currentSlide = 0;
    setInterval(() => {
        slides[currentSlide].classList.remove('active');
        currentSlide = (currentSlide + 1) % slides.length;
        slides[currentSlide].classList.add('active');
    }, 5000);
}

// Loan Settlement Calculator
function initCalculator() {
    const slider = document.getElementById('loan-amount-slider');
    const loanDisplay = document.getElementById('current-loan-display');
    const settlementDisplay = document.getElementById('settlement-amount-display');
    const savingsDisplay = document.getElementById('savings-display');

    if (!slider) return;

    const updateCalculations = () => {
        const amount = parseInt(slider.value);
        const settlement = Math.round(amount * 0.3); // 30% rule
        const savings = amount - settlement;

        loanDisplay.textContent = amount.toLocaleString('en-IN');
        settlementDisplay.textContent = settlement.toLocaleString('en-IN');
        savingsDisplay.textContent = savings.toLocaleString('en-IN');
    };

    slider.addEventListener('input', updateCalculations);
    updateCalculations(); // Initial run
}
