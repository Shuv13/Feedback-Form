document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('.rating .fa-star');
    const form = document.getElementById('feedbackForm');
    const successModal = document.getElementById('successModal');
    let rating = 0;

    // Star rating functionality
    stars.forEach(star => {
        star.addEventListener('mouseover', function() {
            const rating = this.dataset.rating;
            highlightStars(rating);
        });

        star.addEventListener('mouseout', function() {
            highlightStars(rating);
        });

        star.addEventListener('click', function() {
            rating = this.dataset.rating;
            highlightStars(rating);
        });
    });

    function highlightStars(count) {
        stars.forEach(star => {
            const rating = star.dataset.rating;
            if (rating <= count) {
                star.classList.add('active');
            } else {
                star.classList.remove('active');
            }
        });
    }

    // Form submission
    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            rating: rating,
            category: document.getElementById('category').value,
            message: document.getElementById('message').value
        };

        try {
            const response = await fetch('/submit-feedback', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                showSuccessModal();
                form.reset();
                rating = 0;
                highlightStars(0);
            } else {
                throw new Error('Failed to submit feedback');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Failed to submit feedback. Please try again.');
        }
    });

    function showSuccessModal() {
        successModal.style.display = 'flex';
        setTimeout(() => {
            successModal.classList.add('active');
        }, 10);

        setTimeout(() => {
            successModal.classList.remove('active');
            setTimeout(() => {
                successModal.style.display = 'none';
            }, 300);
        }, 2000);
    }

    // Add input animations
    const inputs = document.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });

        input.addEventListener('blur', function() {
            if (!this.value) {
                this.parentElement.classList.remove('focused');
            }
        });
    });
}); 