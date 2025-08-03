# Create the main HTML file for the birthday coupon platform
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Birthday Coupon Platform - Celebrate Together!</title>
    <link rel="stylesheet" href="css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">
                <i class="fas fa-birthday-cake"></i>
                <span>BirthdayTreats</span>
            </div>
            <div class="nav-menu">
                <a href="#home" class="nav-link">Home</a>
                <a href="#how-it-works" class="nav-link">How It Works</a>
                <a href="vendor-login.html" class="nav-link vendor-btn">Vendor Login</a>
                <button class="login-btn" onclick="showLoginModal()">Login</button>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section id="home" class="hero">
        <div class="hero-content">
            <h1>🎉 Celebrate Birthdays Even When Apart!</h1>
            <p>Create digital birthday coupons for your friends and let them enjoy treats at their favorite college spots</p>
            <div class="hero-buttons">
                <button class="cta-btn primary" onclick="showCreateCoupon()">Create Birthday Coupon</button>
                <button class="cta-btn secondary" onclick="showRedeemCoupon()">Redeem Coupon</button>
            </div>
        </div>
        <div class="hero-image">
            <div class="floating-coupon">
                <div class="coupon-sample">
                    <div class="coupon-header">🎂 Happy Birthday!</div>
                    <div class="coupon-value">₹200 Treat</div>
                    <div class="coupon-from">From: Rahul</div>
                </div>
            </div>
        </div>
    </section>

    <!-- How It Works -->
    <section id="how-it-works" class="how-it-works">
        <div class="container">
            <h2>How BirthdayTreats Works</h2>
            <div class="steps">
                <div class="step">
                    <div class="step-icon">🎂</div>
                    <h3>Birthday Person Creates</h3>
                    <p>Set coupon value, choose restaurants, add personal message</p>
                </div>
                <div class="step">
                    <div class="step-icon">📱</div>
                    <h3>Friends Receive</h3>
                    <p>Get QR codes via WhatsApp, SMS, or email</p>
                </div>
                <div class="step">
                    <div class="step-icon">🍕</div>
                    <h3>Enjoy Treats</h3>
                    <p>Show QR code at participating restaurants and enjoy!</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Participating Restaurants -->
    <section class="restaurants">
        <div class="container">
            <h2>Participating College Canteens & Restaurants</h2>
            <div class="restaurant-grid">
                <div class="restaurant-card">
                    <h3>IIT Delhi Central Canteen</h3>
                    <p>North Campus • Indian & Continental</p>
                    <div class="popular-items">Popular: Chole Bhature, Maggi, Tea</div>
                </div>
                <div class="restaurant-card">
                    <h3>DU Miranda House Cafeteria</h3>
                    <p>North Campus • Snacks & Beverages</p>
                    <div class="popular-items">Popular: Samosa, Cold Coffee, Pasta</div>
                </div>
                <div class="restaurant-card">
                    <h3>Amity University Food Court</h3>
                    <p>Noida Campus • Multi-cuisine</p>
                    <div class="popular-items">Popular: Biryani, Pizza, Noodles</div>
                </div>
                <div class="restaurant-card">
                    <h3>Punjabi Dhaba Near VIT</h3>
                    <p>Vellore • Authentic Punjabi</p>
                    <div class="popular-items">Popular: Butter Chicken, Naan, Lassi</div>
                </div>
                <div class="restaurant-card">
                    <h3>South Indian Corner - BITS</h3>
                    <p>Pilani Campus • South Indian</p>
                    <div class="popular-items">Popular: Dosa, Idli, Filter Coffee</div>
                </div>
                <div class="restaurant-card">
                    <h3>Café Coffee Day - NIT</h3>
                    <p>Trichy Campus • Café & Snacks</p>
                    <div class="popular-items">Popular: Cappuccino, Sandwich, Brownie</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Login Modal -->
    <div id="loginModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal('loginModal')">&times;</span>
            <h2>Welcome Back!</h2>
            <form id="loginForm">
                <input type="email" placeholder="Email" required>
                <input type="password" placeholder="Password" required>
                <button type="submit">Login</button>
            </form>
            <p>Don't have an account? <a href="#" onclick="showSignupModal()">Sign up here</a></p>
        </div>
    </div>

    <!-- Signup Modal -->
    <div id="signupModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal('signupModal')">&times;</span>
            <h2>Join BirthdayTreats!</h2>
            <form id="signupForm">
                <input type="text" placeholder="Full Name" required>
                <input type="email" placeholder="Email" required>
                <input type="tel" placeholder="Phone Number" required>
                <input type="password" placeholder="Password" required>
                <select required>
                    <option value="">Select Your College</option>
                    <option value="iit-delhi">IIT Delhi</option>
                    <option value="du-miranda">DU Miranda House</option>
                    <option value="amity-noida">Amity University Noida</option>
                    <option value="vit-vellore">VIT Vellore</option>
                    <option value="bits-pilani">BITS Pilani</option>
                    <option value="nit-trichy">NIT Trichy</option>
                </select>
                <button type="submit">Sign Up</button>
            </form>
        </div>
    </div>

    <!-- Create Coupon Modal -->
    <div id="createCouponModal" class="modal">
        <div class="modal-content large">
            <span class="close" onclick="closeModal('createCouponModal')">&times;</span>
            <h2>🎉 Create Birthday Coupon</h2>
            <form id="createCouponForm">
                <div class="form-row">
                    <div class="form-group">
                        <label>Your Name</label>
                        <input type="text" id="senderName" placeholder="Enter your name" required>
                    </div>
                    <div class="form-group">
                        <label>Birthday Date</label>
                        <input type="date" id="birthdayDate" required>
                    </div>
                </div>
                
                <div class="form-group">
                    <label>Friends' Details (one per line)</label>
                    <textarea id="friendsList" placeholder="Priya - 9876543210&#10;Arjun - 9876543211&#10;Sneha - 9876543212" rows="4" required></textarea>
                    <small>Format: Name - Phone Number</small>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label>Coupon Value</label>
                        <select id="couponValue" required>
                            <option value="">Select Amount</option>
                            <option value="100">₹100</option>
                            <option value="200">₹200</option>
                            <option value="300">₹300</option>
                            <option value="500">₹500</option>
                            <option value="custom">Custom Amount</option>
                        </select>
                    </div>
                    <div class="form-group" id="customValueGroup" style="display: none;">
                        <label>Custom Amount</label>
                        <input type="number" id="customValue" placeholder="Enter amount" min="50" max="2000">
                    </div>
                </div>

                <div class="form-group">
                    <label>Select Restaurants</label>
                    <div class="restaurant-checkboxes">
                        <label class="checkbox-label">
                            <input type="checkbox" value="iit-delhi-canteen"> IIT Delhi Central Canteen
                        </label>
                        <label class="checkbox-label">
                            <input type="checkbox" value="du-miranda-cafe"> DU Miranda House Cafeteria
                        </label>
                        <label class="checkbox-label">
                            <input type="checkbox" value="amity-food-court"> Amity University Food Court
                        </label>
                        <label class="checkbox-label">
                            <input type="checkbox" value="punjabi-dhaba-vit"> Punjabi Dhaba Near VIT
                        </label>
                        <label class="checkbox-label">
                            <input type="checkbox" value="south-indian-bits"> South Indian Corner - BITS
                        </label>
                        <label class="checkbox-label">
                            <input type="checkbox" value="ccd-nit"> Café Coffee Day - NIT
                        </label>
                    </div>
                </div>

                <div class="form-group">
                    <label>Personal Message</label>
                    <textarea id="personalMessage" placeholder="Happy Birthday! Enjoy this treat on me! 🎉" rows="2"></textarea>
                </div>

                <div class="form-group">
                    <label>Coupon Design</label>
                    <div class="design-options">
                        <div class="design-option" data-design="birthday-cake">
                            <div class="design-preview birthday-cake">🎂 Birthday Cake</div>
                        </div>
                        <div class="design-option" data-design="party-balloons">
                            <div class="design-preview party-balloons">🎈 Party Balloons</div>
                        </div>
                        <div class="design-option" data-design="gift-box">
                            <div class="design-preview gift-box">🎁 Gift Box</div>
                        </div>
                        <div class="design-option" data-design="celebration">
                            <div class="design-preview celebration">🎊 Celebration</div>
                        </div>
                    </div>
                </div>

                <button type="submit" class="create-btn">Create & Send Coupons (₹<span id="totalCost">0</span>)</button>
            </form>
        </div>
    </div>

    <!-- Redeem Coupon Modal -->
    <div id="redeemCouponModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal('redeemCouponModal')">&times;</span>
            <h2>🎁 Redeem Your Coupon</h2>
            <div class="redeem-options">
                <button class="redeem-btn" onclick="showQRScanner()">
                    <i class="fas fa-qrcode"></i>
                    Scan QR Code
                </button>
                <button class="redeem-btn" onclick="showCouponCode()">
                    <i class="fas fa-keyboard"></i>
                    Enter Coupon Code
                </button>
            </div>
            
            <div id="qrScannerDiv" style="display: none;">
                <div class="scanner-placeholder">
                    <i class="fas fa-camera"></i>
                    <p>Point your camera at the QR code</p>
                    <button class="demo-btn" onclick="simulateQRScan()">Simulate QR Scan (Demo)</button>
                </div>
            </div>
            
            <div id="couponCodeDiv" style="display: none;">
                <input type="text" id="couponCodeInput" placeholder="Enter coupon code" maxlength="8">
                <button onclick="validateCouponCode()">Validate Coupon</button>
            </div>
        </div>
    </div>

    <!-- Coupon Preview Modal -->
    <div id="couponPreviewModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal('couponPreviewModal')">&times;</span>
            <div id="couponPreview"></div>
            <div class="preview-actions">
                <button onclick="downloadCoupon()">Download</button>
                <button onclick="shareCoupon()">Share</button>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.3/build/qrcode.min.js"></script>
    <script src="js/app.js"></script>
</body>
</html>'''

# Save the HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ Created index.html - Main user interface")