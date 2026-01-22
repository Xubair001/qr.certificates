#!/usr/bin/env python3
"""
Certificate Generator with QR Codes
Generates professional HTML certificates and corresponding QR codes.
Designed to work with GitHub Pages or any static hosting.
"""

import qrcode
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Certificate:
    certificate_no: str
    participant_name: str
    id_number: str
    course: str
    company_name: str
    training_date: str
    expiry_date: str


def generate_certificate_html(cert: Certificate) -> str:
    """Generate a beautiful HTML certificate page."""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Certificate Verification - {cert.certificate_no}</title>
    <style>
        * {{margin: 0;padding: 0;box-sizing: border-box;}}
        body {{font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);min-height: 100vh;display: flex;align-items: center;justify-content: center;padding: 20px;}}
        .container {{max-width: 600px;width: 100%;}}
        .verification-badge {{background: #10b981;color: white;text-align: center;padding: 20px;border-radius: 12px 12px 0 0;box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);}}
        .badge-icon {{width: 60px;height: 60px;background: rgba(255, 255, 255, 0.2);border-radius: 50%;display: flex;align-items: center;justify-content: center;margin: 0 auto 15px;font-size: 32px;}}
        .verification-badge h1 {{font-size: 24px;margin-bottom: 5px;font-weight: 600;}}
        .verification-badge p {{font-size: 14px;opacity: 0.95;}}
        .certificate-card {{background: white;border-radius: 0 0 12px 12px;box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);overflow: hidden;}}
        .certificate-header {{background: linear-gradient(135deg, #1e3a5f, #2d5a87);color: white;padding: 30px;text-align: center;}}
        .certificate-header h2 {{font-size: 28px;margin-bottom: 8px;font-weight: 600;}}
        .certificate-header p {{font-size: 14px;opacity: 0.9;}}
        .certificate-body {{padding: 30px;}}
        .info-row {{display: flex;padding: 16px 0;border-bottom: 1px solid #e5e7eb;}}
        .info-row:last-child {{border-bottom: none;}}
        .info-label {{width: 35%;color: #6b7280;font-size: 14px;font-weight: 500;}}
        .info-value {{width: 65%;color: #1f2937;font-size: 14px;font-weight: 600;}}
        .certificate-footer {{background: #f9fafb;padding: 20px 30px;text-align: center;font-size: 12px;color: #6b7280;border-top: 1px solid #e5e7eb;}}
        .timestamp {{margin-top: 8px;font-size: 11px;opacity: 0.8;}}
        @media (max-width: 600px) {{.certificate-header h2 {{font-size: 22px;}}.info-row {{flex-direction: column;padding: 12px 0;}}.info-label {{width: 100%;margin-bottom: 4px;}}.info-value {{width: 100%;}}}}
        .pulse {{animation: pulse 2s infinite;}}
        @keyframes pulse {{0%, 100% {{transform: scale(1);}}50% {{transform: scale(1.05);}}}}
    </style>
</head>
<body>
    <div class="container">
        <div class="verification-badge">
            <div class="badge-icon pulse">✓</div>
            <h1>VERIFIED</h1>
            <p>This certificate is valid and authenticated</p>
        </div>
        <div class="certificate-card">
            <div class="certificate-header">
                <h2>Training Certificate</h2>
                <p>Official Certification of Completion</p>
            </div>
            <div class="certificate-body">
                <div class="info-row"><div class="info-label">Certificate No.</div><div class="info-value">{cert.certificate_no}</div></div>
                <div class="info-row"><div class="info-label">Participant Name</div><div class="info-value">{cert.participant_name}</div></div>
                <div class="info-row"><div class="info-label">ID Number</div><div class="info-value">{cert.id_number}</div></div>
                <div class="info-row"><div class="info-label">Course</div><div class="info-value">{cert.course}</div></div>
                <div class="info-row"><div class="info-label">Company</div><div class="info-value">{cert.company_name}</div></div>
                <div class="info-row"><div class="info-label">Training Date</div><div class="info-value">{cert.training_date}</div></div>
                <div class="info-row"><div class="info-label">Valid Until</div><div class="info-value">{cert.expiry_date}</div></div>
            </div>
            <div class="certificate-footer">
                Certificate verified successfully
                <div class="timestamp" id="timestamp"></div>
            </div>
        </div>
    </div>
    <script>
        const now = new Date();
        const formatted = now.toLocaleString('en-US', {{year: 'numeric',month: 'short',day: 'numeric',hour: '2-digit',minute: '2-digit'}});
        document.getElementById('timestamp').textContent = `Verified on ${{formatted}}`;
    </script>
</body>
</html>'''


def generate_qr_with_url(url: str, output_file: str) -> str:
    """Generate QR code that redirects to a URL."""
    print(f"Generating QR code for: {url}")

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

    print(f"✓ QR code saved to: {output_file}")
    return output_file


def create_certificate(cert: Certificate, base_url: str, output_dir: str = "certificates"):
    """
    Create both HTML certificate and QR code.

    Args:
        cert: Certificate data
        base_url: Your GitHub Pages URL (e.g., "https://username.github.io/repo-name")
        output_dir: Directory to save files
    """
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Generate HTML file
    html_filename = f"cert_{cert.certificate_no}.html"
    html_path = output_path / html_filename
    html_content = generate_certificate_html(cert)

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✓ Certificate HTML saved to: {html_path}")

    # Generate QR code with URL
    cert_url = f"{base_url}/{html_filename}"
    qr_filename = f"qr_{cert.certificate_no}.png"
    qr_path = output_path / qr_filename

    generate_qr_with_url(cert_url, str(qr_path))

    return {
        'html_file': str(html_path),
        'qr_file': str(qr_path),
        'url': cert_url
    }


def main():
    # Example certificate
    cert = Certificate(
        certificate_no="PK17058",
        participant_name="Muhammad Hasnain",
        id_number="92347591734",
        course="Security Officer",
        company_name="DECON",
        training_date="01 July 2024",
        expiry_date="30 June 2027"
    )

    # Your GitHub Pages URL
    base_url = "https://xubair001.github.io/qr.certificates/certificates"

    print("\n" + "="*50)
    print("CERTIFICATE GENERATOR")
    print("="*50 + "\n")

    if "YOUR_USERNAME" in base_url:
        print("⚠️  WARNING: Please update the base_url in the script!")
        print("   Change 'YOUR_USERNAME' to your actual GitHub username")
        print("   Format: https://username.github.io/QR_generator\n")

    result = create_certificate(cert, base_url)

    print("\n" + "="*50)
    print("GENERATED FILES")
    print("="*50)
    print(f"HTML Certificate: {result['html_file']}")
    print(f"QR Code:          {result['qr_file']}")
    print(f"URL:              {result['url']}")

    if "bit.ly" in base_url or "tinyurl" in base_url or "short.io" in base_url:
        print("\n💡 USING SHORTENED URL:")
        print("   Make sure to create this short URL at the service first!")
        print("   It should redirect to your actual GitHub Pages URL")

    print("\n" + "="*50)
    print("NEXT STEPS")
    print("="*50)
    print("1. Update base_url in this script")
    print("2. Push all files in 'certificates/' folder to your GitHub repo")
    print("3. Enable GitHub Pages in your repo settings")

    if "bit.ly" not in base_url and "tinyurl" not in base_url:
        print("\n   OPTIONAL - To hide your username in URL:")
        print("   4. Go to bit.ly or tinyurl.com")
        print("   5. Shorten your certificate URL")
        print("   6. Update base_url with shortened URL and regenerate")

    print("\n   Share the QR code PNG file")
    print("   When scanned, it will redirect to the certificate page!")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()
