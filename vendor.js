// Vendor Dashboard JavaScript

// Global variables
let currentVendor = JSON.parse(localStorage.getItem('currentVendor') || 'null');
let vendorTransactions = JSON.parse(localStorage.getItem('vendorTransactions') || '[]');
let coupons = JSON.parse(localStorage.getItem('coupons') || '[]');

// Demo vendor credentials
const vendorCredentials = {
    'demo': {
        password: 'demo123',
        restaurant: 'iit-delhi-canteen',
        name: 'IIT Delhi Central Canteen',
        manager: 'Raj Kumar'
    },
    'miranda': {
        password: 'cafe123',
        restaurant: 'du-miranda-cafe', 
        name: 'DU Miranda House Cafeteria',
        manager: 'Priya Sharma'
    },
    'amity': {
        password: 'food123',
        restaurant: 'amity-food-court',
        name: 'Amity University Food Court', 
        manager: 'Arjun Singh'
    }
};

// Restaurant data
const restaurantData = {
    'iit-delhi-canteen': {
        name: 'IIT Delhi Central Canteen',
        location: 'IIT Delhi, Hauz Khas',
        speciality: 'North Indian & Continental',
        popularItems: ['Chole Bhature ₹80', 'Rajma Rice ₹70', 'Maggi ₹40', 'Tea ₹15', 'Samosa ₹20']
    },
    'du-miranda-cafe': {
        name: 'DU Miranda House Cafeteria',
        location: 'Miranda House, University of Delhi',
        speciality: 'Snacks & Beverages',
        popularItems: ['Cold Coffee ₹50', 'Pasta ₹90', 'Sandwich ₹60', 'Momos ₹50']
    },
    'amity-food-court': {
        name: 'Amity University Food Court',
        location: 'Amity University, Noida',
        speciality: 'Multi-cuisine',
        popularItems: ['Biryani ₹120', 'Pizza ₹150', 'Noodles ₹80', 'Dosa ₹60']
    },
    'punjabi-dhaba-vit': {
        name: 'Punjabi Dhaba Near VIT',
        location: 'Near VIT Vellore Campus',
        speciality: 'Authentic Punjabi',
        popularItems: ['Butter Chicken ₹180', 'Naan ₹30', 'Lassi ₹40', 'Dal Makhani ₹100']
    },
    'south-indian-bits': {
        name: 'South Indian Corner - BITS',
        location: 'BITS Pilani Campus',
        speciality: 'South Indian',
        popularItems: ['Dosa ₹50', 'Idli ₹40', 'Filter Coffee ₹25', 'Vada ₹30']
    },
    'ccd-nit': {
        name: 'Café Coffee Day - NIT',
        location: 'NIT Trichy Campus',
        speciality: 'Café & Snacks',
        popularItems: ['Cappuccino ₹80', 'Brownie ₹120', 'Sandwich ₹100', 'Frappe ₹140']
    }
};

// Initialize vendor dashboard
document.addEventListener('DOMContentLoaded', function() {
    if (currentVendor) {
        showVendorDashboard();
    } else {
        showVendorLogin();
    }

    setupVendorEventListeners();
    loadDemoTransactions();
    updateDashboardStats();
});

// Setup event listeners
function setupVendorEventListeners() {
    const vendorLoginForm = document.getElementById('vendorLoginForm');
    if (vendorLoginForm) {
        vendorLoginForm.addEventListener('submit', handleVendorLogin);
    }
}

// Load demo transactions
function loadDemoTransactions() {
    if (vendorTransactions.length === 0) {
        const demoTransactions = [
            {
                id: 'TXN001',
                couponCode: 'BD23A1C7',
                customerName: 'Priya S.',
                amount: 200,
                items: 'Chole Bhature, Tea',
                timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(), // 2 hours ago
                status: 'completed',
                restaurant: 'iit-delhi-canteen'
            },
            {
                id: 'TXN002', 
                couponCode: 'BD23B2D8',
                customerName: 'Arjun K.',
                amount: 150,
                items: 'Maggi, Cold Coffee',
                timestamp: new Date(Date.now() - 3 * 60 * 60 * 1000).toISOString(), // 3 hours ago
                status: 'completed',
                restaurant: 'iit-delhi-canteen'
            },
            {
                id: 'TXN003',
                couponCode: 'BD23C3E9', 
                customerName: 'Sneha M.',
                amount: 300,
                items: 'Biryani, Lassi',
                timestamp: new Date(Date.now() - 5 * 60 * 60 * 1000).toISOString(), // 5 hours ago
                status: 'completed',
                restaurant: 'iit-delhi-canteen'
            }
        ];

        vendorTransactions = demoTransactions;
        localStorage.setItem('vendorTransactions', JSON.stringify(vendorTransactions));
    }
}

// Vendor login handling
function handleVendorLogin(e) {
    e.preventDefault();

    const restaurant = document.getElementById('vendorSelect').value;
    const username = document.getElementById('vendorUsername').value;
    const password = document.getElementById('vendorPassword').value;

    if (!restaurant || !username || !password) {
        showVendorError('Please fill all fields');
        return;
    }

    // Check credentials
    const vendor = vendorCredentials[username];
    if (vendor && vendor.password === password) {
        currentVendor = {
            username: username,
            restaurant: restaurant,
            name: restaurantData[restaurant]?.name || 'Unknown Restaurant',
            manager: vendor.manager,
            loginTime: new Date().toISOString()
        };

        localStorage.setItem('currentVendor', JSON.stringify(currentVendor));
        showVendorDashboard();
        showVendorSuccess('Login successful! Welcome to vendor dashboard.');
    } else {
        showVendorError('Invalid credentials. Try: demo / demo123');
    }
}

// Show/hide sections
function showVendorLogin() {
    document.getElementById('vendorLogin').style.display = 'block';
    document.getElementById('vendorDashboard').style.display = 'none';
}

function showVendorDashboard() {
    document.getElementById('vendorLogin').style.display = 'none';
    document.getElementById('vendorDashboard').style.display = 'block';

    if (currentVendor) {
        document.getElementById('vendorName').textContent = currentVendor.name;
        updateDashboardStats();
        updateTransactionsTable();
    }
}

// Update dashboard statistics
function updateDashboardStats() {
    if (!currentVendor) return;

    const today = new Date().toDateString();
    const todayTransactions = vendorTransactions.filter(t => 
        new Date(t.timestamp).toDateString() === today && 
        t.restaurant === currentVendor.restaurant
    );

    const todayRevenue = todayTransactions.reduce((sum, t) => sum + t.amount, 0);
    const todayCoupons = todayTransactions.length;
    const uniqueCustomers = new Set(todayTransactions.map(t => t.customerName)).size;

    // Update stat cards
    const statCards = document.querySelectorAll('.stat-card');
    if (statCards.length >= 4) {
        statCards[0].querySelector('h3').textContent = `₹${todayRevenue}`;
        statCards[1].querySelector('h3').textContent = todayCoupons;
        statCards[2].querySelector('h3').textContent = uniqueCustomers;
        statCards[3].querySelector('h3').textContent = '4.8'; // Fixed rating
    }
}

// Update transactions table
function updateTransactionsTable() {
    const tbody = document.getElementById('transactionsBody');
    if (!tbody || !currentVendor) return;

    const vendorTransactionsFiltered = vendorTransactions
        .filter(t => t.restaurant === currentVendor.restaurant)
        .sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp))
        .slice(0, 10); // Show last 10 transactions

    tbody.innerHTML = vendorTransactionsFiltered.map(transaction => {
        const time = new Date(transaction.timestamp).toLocaleTimeString('en-IN', {
            hour: '2-digit',
            minute: '2-digit'
        });

        return `
            <tr>
                <td>${time}</td>
                <td>${transaction.couponCode}</td>
                <td>${transaction.customerName}</td>
                <td>₹${transaction.amount}</td>
                <td>${transaction.items}</td>
                <td><span class="status ${transaction.status}">${transaction.status}</span></td>
            </tr>
        `;
    }).join('');
}

// Quick actions
function showQuickValidate() {
    document.getElementById('validateCouponModal').style.display = 'block';
}

function showMenuManager() {
    showVendorSuccess('Menu management feature coming soon!');
}

function showReports() {
    showVendorSuccess('Detailed reports feature coming soon!');
}

function showVendorSettings() {
    showVendorSuccess('Settings panel coming soon!');
}

// Coupon validation
function startQRValidation() {
    document.getElementById('qrValidationDiv').style.display = 'block';
    document.getElementById('codeValidationDiv').style.display = 'none';
    document.getElementById('validationResult').style.display = 'none';
}

function startCodeValidation() {
    document.getElementById('qrValidationDiv').style.display = 'none';
    document.getElementById('codeValidationDiv').style.display = 'block';
    document.getElementById('validationResult').style.display = 'none';
}

function simulateValidation() {
    // Simulate QR code scan - find a valid unused coupon
    const validCoupons = coupons.filter(c => 
        !c.used && 
        c.restaurants.includes(currentVendor.restaurant) &&
        new Date(c.validUntil) >= new Date()
    );

    if (validCoupons.length > 0) {
        const coupon = validCoupons[Math.floor(Math.random() * validCoupons.length)];
        showValidationResult(coupon);
    } else {
        showVendorError('No valid coupons found in demo data');
    }
}

function validateCouponByCode() {
    const code = document.getElementById('validationCodeInput').value.toUpperCase().trim();

    if (!code) {
        showVendorError('Please enter coupon code');
        return;
    }

    const coupon = coupons.find(c => 
        c.id === code && 
        !c.used && 
        c.restaurants.includes(currentVendor.restaurant) &&
        new Date(c.validUntil) >= new Date()
    );

    if (coupon) {
        showValidationResult(coupon);
    } else {
        showVendorError('Invalid, expired, or already used coupon code');
    }
}

function showValidationResult(coupon) {
    document.getElementById('qrValidationDiv').style.display = 'none';
    document.getElementById('codeValidationDiv').style.display = 'none';
    document.getElementById('validationResult').style.display = 'block';

    // Populate validation details
    document.getElementById('validatedCode').textContent = coupon.id;
    document.getElementById('validatedAmount').textContent = coupon.value;
    document.getElementById('validatedSender').textContent = coupon.senderName;
    document.getElementById('validatedMessage').textContent = coupon.message;
    document.getElementById('validatedExpiry').textContent = new Date(coupon.validUntil).toLocaleDateString();

    // Store current coupon for processing
    window.currentValidatedCoupon = coupon;
}

function acceptCoupon() {
    if (!window.currentValidatedCoupon) return;

    closeValidateModal();
    showPaymentModal(window.currentValidatedCoupon);
}

function rejectCoupon() {
    closeValidateModal();
    showVendorError('Coupon validation rejected');
    window.currentValidatedCoupon = null;
}

function showPaymentModal(coupon) {
    const modal = document.getElementById('paymentModal');
    const amount = coupon.value;
    const platformFee = Math.round(amount * 0.02); // 2% platform fee
    const vendorReceives = amount - platformFee;

    document.getElementById('paymentAmount').textContent = amount;
    document.getElementById('platformFee').textContent = platformFee;
    document.getElementById('vendorReceives').textContent = vendorReceives;

    modal.style.display = 'block';
    window.currentPaymentCoupon = coupon;
}

function completeTransaction() {
    if (!window.currentPaymentCoupon) return;

    const coupon = window.currentPaymentCoupon;
    const orderItems = document.getElementById('orderItems').value || 'Items as per customer choice';

    // Mark coupon as used
    const couponIndex = coupons.findIndex(c => c.id === coupon.id);
    if (couponIndex !== -1) {
        coupons[couponIndex].used = true;
        coupons[couponIndex].usedAt = new Date().toISOString();
        coupons[couponIndex].usedBy = currentVendor.restaurant;
        localStorage.setItem('coupons', JSON.stringify(coupons));
    }

    // Add transaction record
    const transaction = {
        id: 'TXN' + Date.now(),
        couponCode: coupon.id,
        customerName: coupon.recipientName,
        amount: coupon.value,
        items: orderItems,
        timestamp: new Date().toISOString(),
        status: 'completed',
        restaurant: currentVendor.restaurant,
        platformFee: Math.round(coupon.value * 0.02),
        vendorAmount: coupon.value - Math.round(coupon.value * 0.02)
    };

    vendorTransactions.unshift(transaction);
    localStorage.setItem('vendorTransactions', JSON.stringify(vendorTransactions));

    // Close modal and update UI
    document.getElementById('paymentModal').style.display = 'none';
    updateDashboardStats();
    updateTransactionsTable();

    showVendorSuccess(`Transaction completed! ₹${transaction.vendorAmount} credited to your account.`);

    // Clear current coupon
    window.currentPaymentCoupon = null;
    document.getElementById('orderItems').value = '';
}

function cancelTransaction() {
    document.getElementById('paymentModal').style.display = 'none';
    window.currentPaymentCoupon = null;
    document.getElementById('orderItems').value = '';
    showVendorError('Transaction cancelled');
}

function closeValidateModal() {
    document.getElementById('validateCouponModal').style.display = 'none';
    document.getElementById('qrValidationDiv').style.display = 'none';
    document.getElementById('codeValidationDiv').style.display = 'none';
    document.getElementById('validationResult').style.display = 'none';
    document.getElementById('validationCodeInput').value = '';
    window.currentValidatedCoupon = null;
}

// Vendor logout
function vendorLogout() {
    currentVendor = null;
    localStorage.removeItem('currentVendor');
    showVendorLogin();
    showVendorSuccess('Logged out successfully');
}

// Vendor signup (placeholder)
function showVendorSignup() {
    showVendorSuccess('Vendor registration is coming soon! Contact support for early access.');
}

// Utility functions for vendor
function showVendorSuccess(message) {
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

function showVendorError(message) {
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

// Close modals when clicking outside
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
}

// Navigation active state
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();

        // Remove active class from all links
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));

        // Add active class to clicked link
        this.classList.add('active');

        // Show corresponding section (placeholder for now)
        const section = this.getAttribute('href').substring(1);
        showVendorSuccess(`${section.charAt(0).toUpperCase() + section.slice(1)} section coming soon!`);
    });
});

// Auto-refresh dashboard stats every 30 seconds
setInterval(() => {
    if (currentVendor && document.getElementById('vendorDashboard').style.display !== 'none') {
        updateDashboardStats();
    }
}, 30000);