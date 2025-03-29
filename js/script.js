// Wait for DOM content to be loaded
document.addEventListener('DOMContentLoaded', () => {
    // Elements
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');
    const navLinksItems = document.querySelectorAll('.nav-link');
    const backToTopBtn = document.getElementById('backToTop');
    const contactForm = document.getElementById('contactForm');
    const formInputs = document.querySelectorAll('#contactForm input, #contactForm textarea');
    const header = document.querySelector('header');
    const profileImage = document.querySelector('.about-image .image-container');
    const projectCards = document.querySelectorAll('.project-card');

    // Handle errors for images - fallback for GitHub Pages
    document.querySelectorAll('img').forEach(img => {
        img.addEventListener('error', function() {
            // If image fails to load, replace with placeholder
            const imgPath = this.getAttribute('src');
            console.log(`Image failed to load: ${imgPath}`);
            
            // Try to determine what kind of image this is
            if (imgPath.includes('profile')) {
                this.src = 'https://via.placeholder.com/400x400/4a89dc/ffffff?text=Profile+Image';
            } else if (imgPath.includes('project')) {
                this.src = 'https://via.placeholder.com/350x200/4a89dc/ffffff?text=Project+Image';
            } else {
                this.src = 'https://via.placeholder.com/300x300/4a89dc/ffffff?text=Image';
            }
            
            // Remove loading="lazy" to ensure placeholder is loaded
            this.removeAttribute('loading');
        });
    });

    // Toggle mobile menu
    hamburger.addEventListener('click', () => {
        hamburger.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Close mobile menu when clicking on a nav link
    navLinksItems.forEach(link => {
        link.addEventListener('click', () => {
            hamburger.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });

    // Back to top button and parallax scrolling
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopBtn.classList.add('show');
        } else {
            backToTopBtn.classList.remove('show');
        }

        // Add header shadow on scroll
        if (window.scrollY > 50) {
            header.style.boxShadow = '0 5px 20px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        }

        // Parallax effect for profile image
        if (profileImage) {
            const scrollPosition = window.scrollY;
            const parallaxValue = scrollPosition * 0.05;
            
            if (parallaxValue < 50) { // Limit the effect
                profileImage.style.transform = `translateY(${parallaxValue}px) rotate(${parallaxValue * 0.1}deg)`;
            }
        }

        // Active nav links based on scroll position
        const sections = document.querySelectorAll('section');
        const scrollPosition = window.scrollY + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            
            if (sectionId && scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinksItems.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    });

    // 3D tilt effect for project cards
    if (window.innerWidth > 768) {
        projectCards.forEach(card => {
            card.addEventListener('mousemove', function(e) {
                const cardRect = this.getBoundingClientRect();
                const cardCenterX = cardRect.left + cardRect.width / 2;
                const cardCenterY = cardRect.top + cardRect.height / 2;
                const mouseX = e.clientX - cardCenterX;
                const mouseY = e.clientY - cardCenterY;
                
                // Calculate rotation values (max 10 degrees)
                const rotateY = mouseX * 0.01;
                const rotateX = -mouseY * 0.01;
                
                this.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
                
                // Move the image slightly for depth effect
                const projectImg = this.querySelector('.project-img');
                if (projectImg) {
                    projectImg.style.transform = `translateX(${mouseX * 0.025}px) translateY(${mouseY * 0.025}px)`;
                }
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = '';
                const projectImg = this.querySelector('.project-img');
                if (projectImg) {
                    projectImg.style.transform = '';
                }
            });
        });
    }

    // Smooth scroll for nav links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                window.scrollTo({
                    top: target.offsetTop - 70,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Back to top button click event
    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    // Form validation
    function validateForm(e) {
        let valid = true;
        
        formInputs.forEach(input => {
            const errorMessage = input.nextElementSibling;
            
            // Reset errors
            errorMessage.textContent = '';
            input.style.borderColor = '';
            
            if (!input.value.trim()) {
                errorMessage.textContent = `${input.previousElementSibling.textContent} is required`;
                input.style.borderColor = 'var(--error-color)';
                valid = false;
            } else if (input.type === 'email' && !validateEmail(input.value)) {
                errorMessage.textContent = 'Please enter a valid email address';
                input.style.borderColor = 'var(--error-color)';
                valid = false;
            }
        });
        
        if (!valid) {
            e.preventDefault();
        }
        
        return valid;
    }

    // Email validation
    function validateEmail(email) {
        const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }

    // Form submit event
    contactForm.addEventListener('submit', validateForm);

    // Real-time validation on input
    formInputs.forEach(input => {
        input.addEventListener('blur', () => {
            const errorMessage = input.nextElementSibling;
            
            // Reset errors
            errorMessage.textContent = '';
            input.style.borderColor = '';
            
            if (!input.value.trim()) {
                errorMessage.textContent = `${input.previousElementSibling.textContent} is required`;
                input.style.borderColor = 'var(--error-color)';
            } else if (input.type === 'email' && !validateEmail(input.value)) {
                errorMessage.textContent = 'Please enter a valid email address';
                input.style.borderColor = 'var(--error-color)';
            }
        });
        
        input.addEventListener('input', () => {
            if (input.value.trim()) {
                input.nextElementSibling.textContent = '';
                input.style.borderColor = '';
            }
        });
    });

    // Enhance images with IntersectionObserver for animations and lazy loading
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.2
    };

    // Animation observer
    const animationObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
                // Once the animation is applied, we don't need to observe it anymore
                animationObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe skill items and project cards for animation
    document.querySelectorAll('.skill-item, .project-card').forEach((item, index) => {
        // Add staggered animation with delay based on index
        item.classList.add('fade-in');
        item.style.transitionDelay = `${index * 0.1}s`;
        animationObserver.observe(item);
    });

    // Lazy load images that don't use the loading="lazy" attribute
    const lazyLoadObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                const src = img.getAttribute('data-src');
                
                if (src) {
                    img.src = src;
                    img.removeAttribute('data-src');
                }
                
                lazyLoadObserver.unobserve(img);
            }
        });
    }, {
        rootMargin: '200px 0px'
    });

    // Find images with data-src attribute for lazy loading
    document.querySelectorAll('img[data-src]').forEach(img => {
        lazyLoadObserver.observe(img);
    });

    // Create image gallery effects
    document.querySelectorAll('.gallery-item').forEach((item, index) => {
        // Add staggered animation
        item.classList.add('stagger-in');
        item.style.animationDelay = `${index * 0.1}s`;
        animationObserver.observe(item);
    });

    // Image hover effects for project cards
    document.querySelectorAll('.project-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            const overlayIcon = this.querySelector('.overlay-icon');
            if (overlayIcon) {
                overlayIcon.style.opacity = '1';
                overlayIcon.style.transform = 'translate(-50%, -50%) scale(1)';
            }
        });

        card.addEventListener('mouseleave', function() {
            const overlayIcon = this.querySelector('.overlay-icon');
            if (overlayIcon) {
                overlayIcon.style.opacity = '0';
                overlayIcon.style.transform = 'translate(-50%, -50%) scale(0)';
            }
        });
    });
}); 
