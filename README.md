# QR Certificate Generator

Generate professional training certificates with QR codes that redirect to beautiful web pages - completely free using GitHub Pages!

## Features

- ✅ Beautiful, responsive certificate web pages
- ✅ QR codes that redirect to certificate URLs
- ✅ Free hosting with GitHub Pages
- ✅ Works on all devices
- ✅ No backend required
- ✅ Easy to customize

## Quick Start

### Step 1: Generate Certificate

1. Edit `generate_certificate.py` and update the certificate data:

```python
cert = Certificate(
    certificate_no="PK17058",
    participant_name="Muhammad Hasnain",
    id_number="92347591734",
    course="Security Officer",
    company_name="DECON",
    training_date="01 July 2024",
    expiry_date="30 June 2027"
)
```

2. Update the `base_url` with your GitHub username:

```python
base_url = "https://YOUR_GITHUB_USERNAME.github.io/QR_generator"
```

3. Run the generator:

```bash
source venv/bin/activate
python generate_certificate.py
```

This creates:
- `certificates/cert_PK17058.html` - The certificate webpage
- `certificates/qr_PK17058.png` - QR code that redirects to the page

### Step 2: Deploy to GitHub Pages (FREE)

#### Option A: Using GitHub Website

1. **Create a new GitHub repository:**
   - Go to https://github.com/new
   - Name it `QR_generator` (or any name you like)
   - Make it **Public**
   - Click "Create repository"

2. **Upload your files:**
   - Click "uploading an existing file"
   - Drag and drop ALL files from the `certificates/` folder
   - Commit the files

3. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Under "Source", select `main` branch
   - Click Save
   - Wait 1-2 minutes for deployment

4. **Get your URL:**
   - You'll see: "Your site is live at `https://username.github.io/QR_generator/`"
   - Your certificate is at: `https://username.github.io/QR_generator/cert_PK17058.html`

#### Option B: Using Git CLI

```bash
# Initialize git in your QR_generator folder
git init
git add .
git commit -m "Initial certificate setup"

# Create repo on GitHub (replace YOUR_USERNAME)
# Then push:
git remote add origin https://github.com/YOUR_USERNAME/QR_generator.git
git branch -M main
git push -u origin main

# Enable GitHub Pages in repo settings
```

### Step 3: Update QR Code with Real URL

1. Once GitHub Pages is live, update `generate_certificate.py` with your **actual URL**:

```python
base_url = "https://your-actual-username.github.io/QR_generator"
```

2. Regenerate the QR code:

```bash
python generate_certificate.py
```

3. The new QR code in `certificates/qr_PK17058.png` now points to your live page!

### Step 4: Share the QR Code

- Send `certificates/qr_PK17058.png` via WhatsApp, email, or print it
- When scanned, it redirects to the beautiful certificate page
- Works on all phones - no app needed!

## Generating Multiple Certificates

To create certificates for multiple people:

```python
# Example: Generate 3 certificates
certificates = [
    Certificate(
        certificate_no="PK17058",
        participant_name="Muhammad Hasnain",
        # ... other fields
    ),
    Certificate(
        certificate_no="PK17059",
        participant_name="Ahmed Ali",
        # ... other fields
    ),
    Certificate(
        certificate_no="PK17060",
        participant_name="Fatima Khan",
        # ... other fields
    ),
]

for cert in certificates:
    create_certificate(cert, base_url)
```

## Customization

### Change Colors

Edit the CSS in `generate_certificate.py`:

```python
# Find this line and change colors:
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

# Popular alternatives:
# Blue gradient: #4e54c8 0%, #8f94fb 100%
# Green gradient: #56ab2f 0%, #a8e063 100%
# Orange gradient: #f46b45 0%, #eea849 100%
```

### Change Verification Badge Color

```python
# Find this line:
.verification-badge {{background: #10b981;

# Change to:
# Red: #ef4444
# Blue: #3b82f6
# Purple: #8b5cf6
```

## Troubleshooting

### QR Code Not Redirecting

1. Make sure GitHub Pages is enabled and deployed
2. Check that the URL in `base_url` matches your actual GitHub Pages URL
3. Test the URL directly in a browser first

### Certificate Not Loading

1. Verify the HTML file is in the root of your GitHub Pages repo
2. Check that the filename in the QR matches the uploaded file
3. Ensure the repository is public

### QR Code Won't Scan

1. Print at least 2x2 inches for best results
2. Ensure good lighting when scanning
3. Try a QR scanner app if phone camera doesn't work

## Cost

**100% FREE**
- GitHub Pages: Free
- QR Code Generation: Free
- No credit card required
- No time limits

## Requirements

- Python 3.8+
- qrcode library
- GitHub account (free)

## License

Free to use for personal and commercial projects.

## Support

If you have questions or need help, open an issue on GitHub!
