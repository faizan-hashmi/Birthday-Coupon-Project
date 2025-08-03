# Create a comprehensive README file with setup instructions
readme_content = '''# 🎉 BirthdayTreats - Digital Birthday Coupon Platform

A fun and innovative platform that allows students to create digital birthday coupons for their friends, redeemable at college canteens and local restaurants. Built with HTML, CSS, and JavaScript for easy deployment and use.

## ✨ Features

### For Birthday Celebrants
- **Create Custom Coupons**: Set values, choose restaurants, add personal messages
- **Beautiful Designs**: 4 different coupon themes (Birthday Cake, Party Balloons, Gift Box, Celebration)
- **QR Code Generation**: Automatic QR codes for easy sharing and redemption
- **Multiple Recipients**: Send coupons to multiple friends at once
- **Flexible Values**: Set custom amounts or choose from presets (₹100-₹500)

### For Friends (Recipients)
- **Easy Redemption**: Scan QR codes or enter coupon codes manually
- **Restaurant Choice**: Use coupons at any participating restaurant
- **Mobile Friendly**: Works perfectly on smartphones
- **Instant Validation**: Real-time coupon verification

### For Vendors/Restaurants
- **Dashboard Analytics**: Track daily revenue, redemptions, and customer insights
- **QR Code Validation**: Scan customer QR codes for instant verification
- **Payment Processing**: Automatic calculation of platform fees and vendor payouts
- **Transaction History**: Complete record of all coupon redemptions
- **Demo Login Available**: Username: `demo`, Password: `demo123`

## 🏪 Participating Restaurants

- **IIT Delhi Central Canteen** - North Indian & Continental
- **DU Miranda House Cafeteria** - Snacks & Beverages  
- **Amity University Food Court** - Multi-cuisine
- **Punjabi Dhaba Near VIT** - Authentic Punjabi
- **South Indian Corner - BITS** - South Indian Specialties
- **Café Coffee Day - NIT** - Café & Snacks

## 🚀 Quick Start

### Option 1: GitHub Pages (Recommended)
1. Fork this repository
2. Go to Settings → Pages
3. Select "Deploy from branch" → "main" → "/ (root)"
4. Your site will be live at `https://yourusername.github.io/birthday-coupon-platform`

### Option 2: Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/birthday-coupon-platform.git
   cd birthday-coupon-platform
   ```

2. Open `index.html` in your web browser

3. For local server (optional):
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Python 2
   python -m SimpleHTTPServer 8000
   
   # Node.js
   npx http-server
   ```

## 📁 Project Structure

```
birthday-coupon-platform/
├── index.html              # Main user interface
├── vendor-login.html       # Vendor dashboard
├── css/
│   ├── style.css          # Main stylesheet
│   └── vendor.css         # Vendor-specific styles
├── js/
│   ├── app.js            # Main application logic
│   └── vendor.js         # Vendor dashboard functionality
├── assets/               # Images and icons (create as needed)
└── README.md            # This file
```

## 🔧 Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: CSS Grid, Flexbox, Animations
- **QR Codes**: QRCode.js library
- **Storage**: Local Storage (for demo purposes)
- **Fonts**: Google Fonts (Poppins)
- **Icons**: Font Awesome

## 💻 Usage Guide

### Creating Birthday Coupons

1. **Sign Up/Login**: Create an account or login with existing credentials
2. **Click "Create Birthday Coupon"**: Start the coupon creation process
3. **Fill Details**:
   - Enter your name and birthday date
   - Add friends' details (Name - Phone Number format)
   - Select coupon value (₹100-₹500 or custom)
   - Choose participating restaurants
   - Add a personal message
   - Select coupon design theme
4. **Review & Create**: Check details and create coupons
5. **Share**: Download or share QR codes with friends

### Redeeming Coupons

1. **Scan QR Code**: Use any smartphone camera to scan the QR code
2. **Or Enter Code**: Manually enter the 8-character coupon code
3. **Verify Details**: Check coupon value and validity
4. **Visit Restaurant**: Show the valid coupon to restaurant staff
5. **Enjoy**: Restaurant validates and you get your treat!

### Vendor Operations

1. **Login**: Use demo credentials (demo/demo123) or register
2. **Dashboard**: View daily stats, revenue, and customer insights
3. **Validate Coupons**: 
   - Scan customer QR codes
   - Or manually enter coupon codes
   - Verify coupon details and authenticity
4. **Process Payment**: 
   - Accept valid coupons
   - Enter items ordered
   - Complete transaction (2% platform fee deducted)
5. **Analytics**: Track performance and customer patterns

## 🎨 Customization

### Adding New Restaurants
Edit `js/app.js` and `js/vendor.js`:

```javascript
// Add to restaurantMenus object
'new-restaurant-id': {
    name: 'New Restaurant Name',
    items: ['Item 1 ₹price', 'Item 2 ₹price']
}
```

### Adding New Coupon Designs
1. Add new design option in HTML
2. Add corresponding CSS classes
3. Update JavaScript design selection logic

### Modifying Coupon Values
Edit the coupon value options in `index.html`:

```html
<option value="750">₹750</option>
<option value="1000">₹1000</option>
```

## 🔒 Security Features

- **Unique Coupon Codes**: 8-character alphanumeric codes
- **QR Code Verification**: Embedded coupon data in QR codes
- **Expiration Dates**: Coupons expire on specified dates
- **Single Use**: Each coupon can only be used once
- **Vendor Validation**: Multi-step verification process

## 📱 Mobile Responsive

The platform is fully responsive and works on:
- Desktop computers
- Tablets
- Smartphones (iOS and Android)
- Works in all modern browsers

## 🚧 Future Enhancements

- **Real Payment Integration**: Razorpay/Stripe integration
- **SMS/WhatsApp Sharing**: Direct coupon sharing
- **Push Notifications**: Real-time updates
- **Advanced Analytics**: Detailed insights and reports
- **Loyalty Programs**: Reward frequent users
- **Admin Panel**: Platform management interface
- **API Integration**: Backend database connectivity

## 🐛 Known Issues & Solutions

### QR Codes Not Generating
- Ensure QRCode.js library is loaded
- Check browser console for errors
- Try refreshing the page

### Coupons Not Saving
- Check if Local Storage is enabled
- Clear browser cache and try again
- Ensure JavaScript is enabled

### Mobile Display Issues
- Clear browser cache
- Try different browsers (Chrome, Safari, Firefox)
- Check internet connection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test thoroughly
5. Commit: `git commit -m 'Add feature-name'`
6. Push: `git push origin feature-name`
7. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 🙋‍♂️ Support

For support, please:
1. Check this README for common issues
2. Create an issue on GitHub
3. Contact the development team

## 🎯 Demo Credentials

### User Accounts
- Create any account with valid email for testing

### Vendor Accounts
- **Username**: `demo` | **Password**: `demo123`
- **Username**: `miranda` | **Password**: `cafe123`
- **Username**: `amity` | **Password**: `food123`

## 🌟 Acknowledgments

- Font Awesome for icons
- Google Fonts for typography
- QRCode.js for QR code generation
- All the college canteens and restaurants for inspiration

---

**Built with ❤️ for college students who want to celebrate birthdays together, even when apart!**

🎂 Happy Birthday to everyone using this platform! 🎉
'''

# Save README file
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("✅ Created README.md - Comprehensive documentation and setup guide")