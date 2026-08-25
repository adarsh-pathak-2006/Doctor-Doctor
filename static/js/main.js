document.addEventListener('DOMContentLoaded', () => {
    // Staggered entrance animation for prescription cards
    const cards = document.querySelectorAll('.prescription-card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add('visible');
        }, index * 100);
    });

    // Loading state for form submission
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Processing...';
                submitBtn.disabled = true;
                
                // Show loader if it's the prescription form
                const loader = document.getElementById('ai-loader');
                if (loader) {
                    loader.style.display = 'block';
                }
            }
        });
    });
});
