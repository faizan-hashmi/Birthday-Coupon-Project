# Create the main CSS file with beautiful styling
css_content = '''/* Main Stylesheet for BirthdayTreats Platform */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    line-height: 1.6;
    color: #333;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Navigation */
.navbar {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    padding: 1rem 0;
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
    box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    display: flex;
    align-items: center;
    font-size: 1.5rem;
    font-weight: 700;
    color: #667eea;
}

.logo i {
    margin-right: 0.5rem;
    color: #ff6b6b;
}

.nav-menu {
    display: flex;
    align-items: center;
    gap: 2rem;
}

.nav-link {
    text-decoration: none;
    color: #333;
    font-weight: 500;
    transition: color 0.3s ease;
}

.nav-link:hover {
    color: #667eea;
}

.vendor-btn {
    background: #f8f9fa;
    padding: 0.5rem 1rem;
    border-radius: 25px;
    border: 2px solid #667eea;
}

.login-btn {
    background: #667eea;
    color: white;
    border: none;
    padding: 0.7rem 1.5rem;
    border-radius: 25px;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s ease;
}

.login-btn:hover {
    background: #5a6fd8;
    transform: translateY(-2px);
}

/* Hero Section */
.hero {
    margin-top: 80px;
    padding: 4rem 0;
    display: flex;
    align-items: center;
    min-height: 80vh;
    color: white;
}

.hero-content {
    flex: 1;
    max-width: 600px;
    padding: 0 2rem;
}

.hero h1 {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 1rem;
    line-height: 1.2;
}

.hero p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    opacity: 0.9;
}

.hero-buttons {
    display: flex;
    gap: 1rem;
}

.cta-btn {
    padding: 1rem 2rem;
    border: none;
    border-radius: 30px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    display: inline-block;
}

.cta-btn.primary {
    background: #ff6b6b;
    color: white;
}

.cta-btn.primary:hover {
    background: #ff5252;
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(255, 107, 107, 0.3);
}

.cta-btn.secondary {
    background: rgba(255, 255, 255, 0.2);
    color: white;
    border: 2px solid rgba(255, 255, 255, 0.3);
}

.cta-btn.secondary:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: translateY(-3px);
}

/* Hero Image */
.hero-image {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}

.floating-coupon {
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
}

.coupon-sample {
    background: linear-gradient(45deg, #ff6b6b, #feca57);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    text-align: center;
    color: white;
    min-width: 250px;
}

.coupon-header {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

.coupon-value {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.coupon-from {
    font-size: 0.9rem;
    opacity: 0.9;
}

/* How It Works Section */
.how-it-works {
    background: white;
    padding: 4rem 0;
}

.how-it-works h2 {
    text-align: center;
    font-size: 2.5rem;
    color: #333;
    margin-bottom: 3rem;
}

.steps {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.step {
    text-align: center;
    padding: 2rem;
    border-radius: 15px;
    background: #f8f9fa;
    transition: transform 0.3s ease;
}

.step:hover {
    transform: translateY(-5px);
}

.step-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.step h3 {
    font-size: 1.3rem;
    color: #333;
    margin-bottom: 1rem;
}

.step p {
    color: #666;
}

/* Restaurants Section */
.restaurants {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    padding: 4rem 0;
    color: white;
}

.restaurants h2 {
    text-align: center;
    font-size: 2.5rem;
    margin-bottom: 3rem;
}

.restaurant-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 2rem;
}

.restaurant-card {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    padding: 2rem;
    border-radius: 15px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    transition: transform 0.3s ease;
}

.restaurant-card:hover {
    transform: translateY(-5px);
}

.restaurant-card h3 {
    font-size: 1.3rem;
    margin-bottom: 0.5rem;
}

.restaurant-card p {
    opacity: 0.9;
    margin-bottom: 1rem;
}

.popular-items {
    background: rgba(255, 255, 255, 0.2);
    padding: 0.8rem;
    border-radius: 8px;
    font-size: 0.9rem;
}

/* Modal Styles */
.modal {
    display: none;
    position: fixed;
    z-index: 2000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(5px);
}

.modal-content {
    background-color: white;
    margin: 5% auto;
    padding: 2rem;
    border-radius: 15px;
    width: 90%;
    max-width: 500px;
    position: relative;
    animation: slideIn 0.3s ease;
}

.modal-content.large {
    max-width: 700px;
}

@keyframes slideIn {
    from { opacity: 0; transform: translateY(-50px); }
    to { opacity: 1; transform: translateY(0); }
}

.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
    cursor: pointer;
    position: absolute;
    right: 20px;
    top: 15px;
}

.close:hover {
    color: #000;
}

/* Form Styles */
.form-group {
    margin-bottom: 1.5rem;
}

.form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: 600;
    color: #333;
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 0.8rem;
    border: 2px solid #e1e8ed;
    border-radius: 8px;
    font-size: 1rem;
    transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: #667eea;
}

.form-group small {
    color: #666;
    font-size: 0.8rem;
}

/* Restaurant Checkboxes */
.restaurant-checkboxes {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 0.5rem;
}

.checkbox-label {
    display: flex;
    align-items: center;
    padding: 0.5rem;
    background: #f8f9fa;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.checkbox-label:hover {
    background: #e9ecef;
}

.checkbox-label input {
    margin-right: 0.5rem;
    width: auto;
}

/* Design Options */
.design-options {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
}

.design-option {
    cursor: pointer;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.3s ease;
}

.design-option:hover {
    transform: scale(1.05);
}

.design-option.selected {
    border: 3px solid #667eea;
}

.design-preview {
    padding: 1rem;
    text-align: center;
    font-weight: 600;
    border-radius: 8px;
}

.design-preview.birthday-cake {
    background: linear-gradient(45deg, #ff6b6b, #feca57);
    color: white;
}

.design-preview.party-balloons {
    background: linear-gradient(45deg, #667eea, #764ba2);
    color: white;
}

.design-preview.gift-box {
    background: linear-gradient(45deg, #f093fb, #f5576c);
    color: white;
}

.design-preview.celebration {
    background: linear-gradient(45deg, #4facfe, #00f2fe);
    color: white;
}

/* Buttons */
.create-btn {
    width: 100%;
    padding: 1rem;
    background: #28a745;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.create-btn:hover {
    background: #218838;
}

/* Redeem Options */
.redeem-options {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin-bottom: 2rem;
}

.redeem-btn {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    background: #f8f9fa;
    border: 2px solid #e1e8ed;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
    color: #333;
}

.redeem-btn:hover {
    border-color: #667eea;
    background: #667eea;
    color: white;
}

.redeem-btn i {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

/* Scanner Placeholder */
.scanner-placeholder {
    text-align: center;
    padding: 3rem;
    background: #f8f9fa;
    border: 2px dashed #dee2e6;
    border-radius: 10px;
    margin: 1rem 0;
}

.scanner-placeholder i {
    font-size: 3rem;
    color: #6c757d;
    margin-bottom: 1rem;
}

.demo-btn {
    background: #6c757d;
    color: white;
    border: none;
    padding: 0.8rem 1.5rem;
    border-radius: 25px;
    cursor: pointer;
    margin-top: 1rem;
}

/* Coupon Display */
.coupon-display {
    max-width: 400px;
    margin: 2rem auto;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}

.coupon-display.birthday-cake {
    background: linear-gradient(45deg, #ff6b6b, #feca57);
}

.coupon-display.party-balloons {
    background: linear-gradient(45deg, #667eea, #764ba2);
}

.coupon-display.gift-box {
    background: linear-gradient(45deg, #f093fb, #f5576c);
}

.coupon-display.celebration {
    background: linear-gradient(45deg, #4facfe, #00f2fe);
}

.coupon-header {
    padding: 1.5rem;
    text-align: center;
    color: white;
}

.coupon-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.coupon-value {
    font-size: 2.5rem;
    font-weight: 800;
    margin: 1rem 0;
}

.coupon-message {
    font-size: 1rem;
    opacity: 0.9;
    margin-bottom: 1rem;
}

.coupon-body {
    background: white;
    padding: 1.5rem;
    color: #333;
}

.coupon-details {
    display: grid;
    gap: 0.5rem;
    margin-bottom: 1.5rem;
}

.coupon-detail {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 0;
    border-bottom: 1px solid #eee;
}

.qr-code {
    text-align: center;
    margin: 1rem 0;
}

.coupon-code {
    font-family: 'Courier New', monospace;
    font-size: 1.2rem;
    font-weight: bold;
    letter-spacing: 2px;
    text-align: center;
    padding: 0.5rem;
    background: #f8f9fa;
    border-radius: 5px;
    margin-top: 1rem;
}

.preview-actions {
    display: flex;
    gap: 1rem;
    margin-top: 2rem;
}

.preview-actions button {
    flex: 1;
    padding: 0.8rem;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 600;
}

.preview-actions button:first-child {
    background: #28a745;
    color: white;
}

.preview-actions button:last-child {
    background: #17a2b8;
    color: white;
}

/* Responsive Design */
@media (max-width: 768px) {
    .hero {
        flex-direction: column;
        text-align: center;
    }
    
    .hero h1 {
        font-size: 2rem;
    }
    
    .hero-buttons {
        flex-direction: column;
        width: 100%;
    }
    
    .cta-btn {
        width: 100%;
    }
    
    .form-row {
        grid-template-columns: 1fr;
    }
    
    .design-options {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .redeem-options {
        grid-template-columns: 1fr;
    }
    
    .restaurant-grid {
        grid-template-columns: 1fr;
    }
    
    .nav-menu {
        flex-direction: column;
        gap: 1rem;
    }
}

/* Success/Error Messages */
.success-message {
    background: #d4edda;
    color: #155724;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #c3e6cb;
    margin: 1rem 0;
}

.error-message {
    background: #f8d7da;
    color: #721c24;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #f5c6cb;
    margin: 1rem 0;
}

.loading {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 3px solid rgba(255,255,255,.3);
    border-radius: 50%;
    border-top-color: #fff;
    animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}'''

# Create CSS directory and save the file
import os
os.makedirs('css', exist_ok=True)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ Created css/style.css - Main stylesheet with beautiful responsive design")