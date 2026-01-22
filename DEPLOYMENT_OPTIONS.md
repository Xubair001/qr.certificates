# Deployment Options - Hide Your Username

Want to hide your GitHub username from the certificate URL? Here are 3 free options:

---

## Option 1: URL Shortener (EASIEST - 5 minutes)

Creates URLs like: `https://bit.ly/3xK9mNp` instead of showing your username.

### Step-by-Step:

**1. Deploy to GitHub Pages first (with your username)**
```python
# In generate_certificate.py
base_url = "https://YOUR_USERNAME.github.io/QR_generator"
```

Run:
```bash
python generate_certificate.py
```

**2. Deploy to GitHub Pages**
- Upload `certificates/` folder to GitHub
- Enable Pages in settings
- Wait 2 minutes for deployment

**3. Get your certificate URL**
```
https://YOUR_USERNAME.github.io/QR_generator/cert_PK17058.html
```

**4. Create shortened URL**

Go to any URL shortener:
- **bit.ly** (https://bitly.com) - Sign up free
  - Paste your certificate URL
  - Customize the ending (optional): `bit.ly/cert-pk17058`
  - Get shortened URL: `https://bit.ly/abc123xyz`

- **tinyurl.com** (https://tinyurl.com) - No signup needed
  - Paste URL
  - Customize (optional)
  - Get: `https://tinyurl.com/randomcode`

- **short.io** (https://short.io) - Free tier available

**5. Update script with shortened URL**
```python
# In generate_certificate.py line 137
base_url = "https://bit.ly/abc123xyz"  # Your actual shortened URL
```

**6. Regenerate QR code**
```bash
python generate_certificate.py
```

**7. Done!**
Now `certificates/qr_PK17058.png` contains a QR that redirects to the short URL, which redirects to your certificate.

### Pros:
✅ Super easy
✅ Takes 5 minutes
✅ Completely free
✅ Can customize the short link
✅ Can track clicks (on bit.ly)
✅ Can change destination later without regenerating QR

### Cons:
❌ Adds an extra redirect
❌ Depends on third-party service

---

## Option 2: Netlify (Random Subdomain - 10 minutes)

Creates URLs like: `https://abc123def.netlify.app` automatically.

### Step-by-Step:

**1. Sign up for Netlify**
- Go to https://netlify.com
- Sign up with GitHub (free)

**2. Deploy your site**
- Click "Add new site" → "Import an existing project"
- Choose "Deploy manually"
- Drag and drop your `certificates/` folder
- Wait 1 minute

**3. Get your random URL**
Netlify automatically gives you: `https://random-name-123.netlify.app`

**4. Update your script**
```python
base_url = "https://random-name-123.netlify.app"
```

**5. Regenerate QR**
```bash
python generate_certificate.py
```

**6. Re-deploy to Netlify**
- Drag and drop updated `certificates/` folder again
- Done!

### Pros:
✅ Random subdomain (no username shown)
✅ Fast hosting
✅ Automatic HTTPS
✅ Custom domains supported (if you buy one later)

### Cons:
❌ Requires signup
❌ Need to redeploy when adding certificates

---

## Option 3: Vercel (Similar to Netlify)

Creates URLs like: `https://qr-generator-xyz789.vercel.app`

### Step-by-Step:

**1. Sign up**
- Go to https://vercel.com
- Sign up with GitHub (free)

**2. Deploy**
- Click "Add New" → "Project"
- Import your GitHub repository
- Or use "Deploy without Git" for drag-and-drop
- Deploy the `certificates/` folder

**3. Get URL**
Vercel gives you: `https://project-name-random.vercel.app`

**4. Update script and regenerate**
```python
base_url = "https://project-name-random.vercel.app"
```

### Pros/Cons:
Same as Netlify

---

## Option 4: Custom Domain (if you want)

If you want something like `https://certificates.com/pk17058`:

**Free options:**
- Freenom (free domains: .tk, .ml, .ga)
- Use with GitHub Pages, Netlify, or Vercel

**Paid options:**
- Namecheap, GoDaddy (~$10/year)
- Connect to any hosting platform above

---

## Comparison Table

| Method | Example URL | Setup Time | Free | Hide Username |
|--------|-------------|------------|------|---------------|
| **GitHub Pages** | username.github.io | 5 min | ✅ | ❌ |
| **URL Shortener** | bit.ly/abc123 | 5 min | ✅ | ✅ |
| **Netlify** | random-abc.netlify.app | 10 min | ✅ | ✅ |
| **Vercel** | project-xyz.vercel.app | 10 min | ✅ | ✅ |
| **Custom Domain** | yourcerts.com | 30 min | ❌ | ✅ |

---

## Recommended Approach

### For Quick & Easy:
1. Deploy to GitHub Pages
2. Use bit.ly to shorten URLs
3. Takes 5 minutes total

### For Professional:
1. Use Netlify or Vercel
2. Gets random subdomain automatically
3. Takes 10 minutes

### For Multiple Certificates:
1. Use Netlify/Vercel (easier to manage)
2. Or use bit.ly with bulk URL shortening

---

## Example Workflow (URL Shortener)

```bash
# 1. Generate with GitHub Pages URL
base_url = "https://myusername.github.io/QR_generator"
python generate_certificate.py

# 2. Deploy to GitHub Pages
git push origin main

# 3. Go to bit.ly and shorten:
# https://myusername.github.io/QR_generator/cert_PK17058.html
# → https://bit.ly/cert-pk17058

# 4. Update script
base_url = "https://bit.ly/cert-verify"

# 5. Regenerate QR
python generate_certificate.py

# 6. Share the new QR code!
```

---

## Security Note

URL shorteners and custom domains hide your username but:
- Anyone can still visit the URL
- Certificates are public
- Add password protection if needed (Netlify/Vercel support this)

---

## Need Help?

Choose based on your priority:
- **Speed**: Option 1 (URL Shortener)
- **Professional look**: Option 2 (Netlify)
- **Simplicity**: Option 1 (URL Shortener)
- **Future flexibility**: Option 2 or 3 (Netlify/Vercel)
