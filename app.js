// Main JavaScript for BirthdayTreats Platform

// Global variables
let selectedDesign = 'birthday-cake';
let coupons = JSON.parse(localStorage.getItem('coupons') || '[]');
let currentUser = JSON.parse(localStorage.getItem('currentUser') || 'null');

// Funky coupon messages
const funkyMessages = [
    "🎉 Surprise! Your friend thinks you deserve a treat!",
    "🎂 Another year older, another reason to celebrate with food!",
    "🎈 Because birthdays are better with free food!",
    "🎁 Your friend's gift to you: unlimited stomach happiness!",
    "🍰 Age is just a number, but free food is eternal!",
    "🎊 Congratulations on surviving another year! Here's food!",
    "🥳 Warning: This coupon contains 100% pure birthday magic!",
    "🎪 Step right up for your birthday food extravaganza!",
    "🌟 You're officially awesome! This coupon proves it!",
    "🎭 Life's a party, and this coupon is your VIP pass!"
];

// Indian food items for different restaurants
const restaurantMenus = {
    'iit-delhi-canteen': {
        name: 'IIT Delhi Central Canteen',
        items: ['Chole Bhature ₹80', 'Maggi ₹40', 'Tea ₹15', 'Samosa ₹20', 'Rajma Rice ₹70']
    },
    'du-miranda-cafe': {
        name: 'DU Miranda House Cafeteria', 
        items: ['Cold Coffee ₹50', 'Pasta ₹90', 'Sandwich ₹60', 'Momos ₹50', 'Burger ₹80']
    },
    'amity-food-court': {
        name: 'Amity University Food Court',
        items: ['Biryani ₹120', 'Pizza ₹150', 'Noodles ₹80', 'Dosa ₹60', 'Fried Rice ₹90']
    },
    'punjabi-dhaba-vit': {
        name: 'Punjabi Dhaba Near VIT',
        items: ['Butter Chicken ₹180', 'Naan ₹30', 'Lassi ₹40', 'Dal Makhani ₹100', 'Paneer Tikka ₹150']
    },
    'south-indian-bits': {
        name: 'South Indian Corner - BITS',
        items: ['Dosa ₹50', 'Idli ₹40', 'Filter Coffee ₹25', 'Vada ₹30', 'Uttapam ₹60']
    },
    'ccd-nit': {
        name: 'Café Coffee Day - NIT',
        items: ['Cappuccino ₹80', 'Brownie ₹120', 'Sandwich ₹100', 'Frappe ₹140', 'Cookies ₹60']
    }
};

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    updateUI();
    setupEventListeners();
    loadDemoData();
});

// Setup event listeners
function setupEventListeners() {
    // Coupon value dropdown change
    const couponValueSelect = document.getElementById('couponValue');
    if (couponValueSelect) {
        couponValueSelect.addEventListener('change', function() {
            toggleCustomValue();
            calculateTotalCost();
        });
    }

    // Friends list change
    const friendsList = document.getElementById('friendsList');
    if (friendsList) {
        friendsList.addEventListener('input', calculateTotalCost);
    }

    // Design selection
    const designOptions = document.querySelectorAll('.design-option');
    designOptions.forEach(option => {
        option.addEventListener('click', function() {
            selectDesign(this.dataset.design);
        });
    });

    // Form submissions
    const createCouponForm = document.getElementById('createCouponForm');
    if (createCouponForm) {
        createCouponForm.addEventListener('submit', handleCreateCoupon);
    }

    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', handleLogin);
    }

    const signupForm = document.getElementById('signupForm');
    if (signupForm) {
        signupForm.addEventListener('submit', handleSignup);
    }
}

// Load demo data for testing
function loadDemoData() {
    if (coupons.length === 0) {
        const demoCoupons = [
            {
                id: 'BD23A1C7',
                senderName: 'Rahul Kumar',
                recipientName: 'Priya Singh',
                recipientPhone: '9876543210',
                value: 200,
                message: 'Happy Birthday Priya! Enjoy this treat on me! 🎉',
                design: 'birthday-cake',
                restaurants: ['iit-delhi-canteen'],
                validUntil: new Date().toDateString(),
                used: false,
                createdAt: new Date().toISOString()
            },
            {
                id: 'BD23B2D8',
                senderName: 'Sneha Patel',
                recipientName: 'Arjun Sharma',
                recipientPhone: '9876543211',
                value: 150,
                message: 'Another year of awesomeness! 🎂',
                design: 'party-balloons',
                restaurants: ['du-miranda-cafe'],
                validUntil: new Date().toDateString(),
                used: false,
                createdAt: new Date().toISOString()
            }
        ];

        coupons = demoCoupons;
        localStorage.setItem('coupons', JSON.stringify(coupons));
    }
}

// Modal functions
function showLoginModal() {
    document.getElementById('loginModal').style.display = 'block';
}

function showSignupModal() {
    closeModal('loginModal');
    document.getElementById('signupModal').style.display = 'block';
}

function showCreateCoupon() {
    if (!currentUser) {
        showLoginModal();
        return;
    }
    document.getElementById('createCouponModal').style.display = 'block';
    populateRandomMessage();
}

function showRedeemCoupon() {
    document.getElementById('redeemCouponModal').style.display = 'block';
}

function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Close modals when clicking outside
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
}

// Populate random funky message
function populateRandomMessage() {
    const messageField = document.getElementById('personalMessage');
    if (messageField && !messageField.value) {
        const randomMessage = funkyMessages[Math.floor(Math.random() * funkyMessages.length)];
        messageField.value = randomMessage;
    }
}

// Toggle custom value input
function toggleCustomValue() {
    const select = document.getElementById('couponValue');
    const customGroup = document.getElementById('customValueGroup');

    if (select.value === 'custom') {
        customGroup.style.display = 'block';
    } else {
        customGroup.style.display = 'none';
    }
}

// Calculate total cost
function calculateTotalCost() {
    const couponValueSelect = document.getElementById('couponValue');
    const customValueInput = document.getElementById('customValue');
    const friendsList = document.getElementById('friendsList');
    const totalCostSpan = document.getElementById('totalCost');

    if (!couponValueSelect || !friendsList || !totalCostSpan) return;

    let couponValue = 0;
    if (couponValueSelect.value === 'custom') {
        couponValue = parseInt(customValueInput.value) || 0;
    } else {
        couponValue = parseInt(couponValueSelect.value) || 0;
    }

    const friendsCount = friendsList.value.trim().split('\n').filter(f => f.trim()).length;
    const totalCost = couponValue * friendsCount;

    totalCostSpan.textContent = totalCost;
}

// Select design
function selectDesign(design) {
    selectedDesign = design;

    // Update UI
    document.querySelectorAll('.design-option').forEach(option => {
        option.classList.remove('selected');
    });

    document.querySelector(`[data-design="${design}"]`).classList.add('selected');
}

// Handle user authentication
function handleLogin(e) {
    e.preventDefault();

    // Simple demo login
    const email = e.target.querySelector('input[type="email"]').value;
    const password = e.target.querySelector('input[type="password"]').value;

    if (email && password) {
        currentUser = {
            id: Date.now(),
            email: email,
            name: email.split('@')[0]
        };

        localStorage.setItem('currentUser', JSON.stringify(currentUser));
        closeModal('loginModal');
        updateUI();
        showSuccessMessage('Logged in successfully!');
    }
}

function handleSignup(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const userData = {
        id: Date.now(),
        name: formData.get('name') || e.target.querySelector('input[type="text"]').value,
        email: formData.get('email') || e.target.querySelector('input[type="email"]').value,
        phone: formData.get('phone') || e.target.querySelector('input[type="tel"]').value,
        college: formData.get('college') || e.target.querySelector('select').value
    };

    currentUser = userData;
    localStorage.setItem('currentUser', JSON.stringify(currentUser));
    closeModal('signupModal');
    updateUI();
    showSuccessMessage('Account created successfully!');
}

// Handle coupon creation
function handleCreateCoupon(e) {
    e.preventDefault();

    const formData = new FormData(e.target);
    const senderName = document.getElementById('senderName').value;
    const birthdayDate = document.getElementById('birthdayDate').value;
    const friendsList = document.getElementById('friendsList').value;
    const couponValue = document.getElementById('couponValue').value === 'custom' ? 
        document.getElementById('customValue').value : document.getElementById('couponValue').value;
    const personalMessage = document.getElementById('personalMessage').value;

    // Get selected restaurants
    const selectedRestaurants = [];
    document.querySelectorAll('.restaurant-checkboxes input:checked').forEach(checkbox => {
        selectedRestaurants.push(checkbox.value);
    });

    if (!selectedRestaurants.length) {
        showErrorMessage('Please select at least one restaurant!');
        return;
    }

    // Parse friends list
    const friends = friendsList.trim().split('\n').filter(f => f.trim()).map(friend => {
        const parts = friend.split(' - ');
        return {
            name: parts[0]?.trim(),
            phone: parts[1]?.trim()
        };
    });

    if (friends.length === 0 || friends.some(f => !f.name || !f.phone)) {
        showErrorMessage('Please enter friends details correctly (Name - Phone Number)!');
        return;
    }

    // Create coupons for each friend
    const newCoupons = friends.map(friend => ({
        id: generateCouponCode(),
        senderName: senderName,
        recipientName: friend.name,
        recipientPhone: friend.phone,
        value: parseInt(couponValue),
        message: personalMessage || funkyMessages[Math.floor(Math.random() * funkyMessages.length)],
        design: selectedDesign,
        restaurants: selectedRestaurants,
        validUntil: birthdayDate,
        used: false,
        createdAt: new Date().toISOString()
    }));

    // Save to storage
    coupons.push(...newCoupons);
    localStorage.setItem('coupons', JSON.stringify(coupons));

    // Show success and preview
    closeModal('createCouponModal');
    showSuccessMessage(`Successfully created ${newCoupons.length} coupons!`);
    showCouponPreview(newCoupons[0]);

    // Reset form
    e.target.reset();
    selectedDesign = 'birthday-cake';
    selectDesign('birthday-cake');
}

// Generate coupon code
function generateCouponCode() {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    let result = 'BD';
    for (let i = 0; i < 6; i++) {
        result += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return result;
}

// Show coupon preview
function showCouponPreview(coupon) {
    const modal = document.getElementById('couponPreviewModal');
    const preview = document.getElementById('couponPreview');

    const qrCodeDiv = document.createElement('div');
    qrCodeDiv.id = 'qrcode-' + coupon.id;

    preview.innerHTML = `
        <div class="coupon-display ${coupon.design}">
            <div class="coupon-header">
                <div class="coupon-title">🎉 Birthday Treat Coupon</div>
                <div class="coupon-value">₹${coupon.value}</div>
                <div class="coupon-message">"${coupon.message}"</div>
            </div>
            <div class="coupon-body">
                <div class="coupon-details">
                    <div class="coupon-detail">
                        <span>From:</span>
                        <span>${coupon.senderName}</span>
                    </div>
                    <div class="coupon-detail">
                        <span>To:</span>
                        <span>${coupon.recipientName}</span>
                    </div>
                    <div class="coupon-detail">
                        <span>Valid Until:</span>
                        <span>${new Date(coupon.validUntil).toLocaleDateString()}</span>
                    </div>
                    <div class="coupon-detail">
                        <span>Restaurants:</span>
                        <span>${coupon.restaurants.length} selected</span>
                    </div>
                </div>
                <div class="qr-code" id="qrcode-${coupon.id}"></div>
                <div class="coupon-code">Code: ${coupon.id}</div>
            </div>
        </div>
    `;

    modal.style.display = 'block';

    // Generate QR code
    setTimeout(() => {
        if (window.QRCode) {
            new QRCode(document.getElementById('qrcode-' + coupon.id), {
                text: JSON.stringify({
                    id: coupon.id,
                    value: coupon.value,
                    sender: coupon.senderName,
                    recipient: coupon.recipientName
                }),
                width: 150,
                height: 150
            });
        }
    }, 100);
}

// QR Scanner simulation
function showQRScanner() {
    document.getElementById('qrScannerDiv').style.display = 'block';
    document.getElementById('couponCodeDiv').style.display = 'none';
}

function showCouponCode() {
    document.getElementById('qrScannerDiv').style.display = 'none';
    document.getElementById('couponCodeDiv').style.display = 'block';
}

function simulateQRScan() {
    const availableCoupons = coupons.filter(c => !c.used);
    if (availableCoupons.length > 0) {
        const randomCoupon = availableCoupons[Math.floor(Math.random() * availableCoupons.length)];
        displayCouponForRedemption(randomCoupon);
    } else {
        showErrorMessage('No valid coupons found!');
    }
}

function validateCouponCode() {
    const code = document.getElementById('couponCodeInput').value.toUpperCase();
    const coupon = coupons.find(c => c.id === code && !c.used);

    if (coupon) {
        displayCouponForRedemption(coupon);
    } else {
        showErrorMessage('Invalid or already used coupon code!');
    }
}

function displayCouponForRedemption(coupon) {
    closeModal('redeemCouponModal');

    // Show coupon details
    const modal = document.getElementById('couponPreviewModal');
    const preview = document.getElementById('couponPreview');

    const restaurantNames = coupon.restaurants.map(r => restaurantMenus[r]?.name || r).join(', ');

    preview.innerHTML = `
        <div class="coupon-display ${coupon.design}">
            <div class="coupon-header">
                <div class="coupon-title">🎉 Valid Birthday Coupon!</div>
                <div class="coupon-value">₹${coupon.value}</div>
                <div class="coupon-message">"${coupon.message}"</div>
            </div>
            <div class="coupon-body">
                <div class="coupon-details">
                    <div class="coupon-detail">
                        <span>From:</span>
                        <span>${coupon.senderName}</span>
                    </div>
                    <div class="coupon-detail">
                        <span>To:</span>
                        <span>${coupon.recipientName}</span>
                    </div>
                    <div class="coupon-detail">
                        <span>Value:</span>
                        <span>₹${coupon.value}</span>
                    </div>
                    <div class="coupon-detail">
                        <span>Valid At:</span>
                        <span>${restaurantNames}</span>
                    </div>
                </div>
                <div class="coupon-code">Code: ${coupon.id}</div>
                <div style="margin-top: 1rem; text-align: center;">
                    <button onclick="useCoupon('${coupon.id}')" class="cta-btn primary">Use This Coupon</button>
                </div>
            </div>
        </div>
    `;

    modal.style.display = 'block';
}

function useCoupon(couponId) {
    const coupon = coupons.find(c => c.id === couponId);
    if (coupon && !coupon.used) {
        coupon.used = true;
        coupon.usedAt = new Date().toISOString();
        localStorage.setItem('coupons', JSON.stringify(coupons));

        closeModal('couponPreviewModal');
        showSuccessMessage('Coupon used successfully! Enjoy your treat! 🎉');
    }
}

// Utility functions
function updateUI() {
    const loginBtn = document.querySelector('.login-btn');
    if (loginBtn && currentUser) {
        loginBtn.textContent = `Hi, ${currentUser.name}`;
        loginBtn.onclick = logout;
    }
}

function logout() {
    currentUser = null;
    localStorage.removeItem('currentUser');
    updateUI();
    showSuccessMessage('Logged out successfully!');
}

function showSuccessMessage(message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'success-message';
    messageDiv.textContent = message;
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '100px';
    messageDiv.style.right = '20px';
    messageDiv.style.zIndex = '3000';
    messageDiv.style.maxWidth = '300px';

    document.body.appendChild(messageDiv);

    setTimeout(() => {
        document.body.removeChild(messageDiv);
    }, 3000);
}

function showErrorMessage(message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'error-message';
    messageDiv.textContent = message;
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '100px';
    messageDiv.style.right = '20px';
    messageDiv.style.zIndex = '3000';
    messageDiv.style.maxWidth = '300px';

    document.body.appendChild(messageDiv);

    setTimeout(() => {
        document.body.removeChild(messageDiv);
    }, 3000);
}

function downloadCoupon() {
    showSuccessMessage('Coupon download started! Check your downloads folder.');
}

function shareCoupon() {
    if (navigator.share) {
        navigator.share({
            title: 'Birthday Coupon',
            text: 'I got you a birthday treat coupon!',
            url: window.location.href
        });
    } else {
        // Fallback - copy to clipboard
        navigator.clipboard.writeText(window.location.href).then(() => {
            showSuccessMessage('Coupon link copied to clipboard!');
        });
    }
}

// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add some animation on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) {
        navbar.style.background = 'rgba(255, 255, 255, 0.98)';
    } else {
        navbar.style.background = 'rgba(255, 255, 255, 0.95)';
    }
});