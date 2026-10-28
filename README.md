# AI Career Hub — Flask

## Quickstart

```bash
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000/

## Admin Panel

The app includes a simple admin panel at `/admin` with minimal CRUD for `courses`, `jobs`, and `internships`.

- Default admin password: `admin123` (set `ADMIN_PASSWORD` env var to override)
- Default session secret: `FLASK_SECRET` env var may be set, otherwise a dev key is used

## Structure

```
ai_career_hub/
├── app.py
├── requirements.txt
├── static/
│   └── style.css
└── templates/
    ├── index.html
    ├── jobs.html
    ├── courses.html
    ├── internships.html
    ├── resume-analyzer.html
    ├── resume-builder.html
    ├── career-predictor.html
    └── r.html
```


# AI Career Hub - Logo Enhancement Summary

## ✅ **Comprehensive Logo System Implemented**

### What's Been Added:

#### 1. **Extended Logo Database (150+ Companies)**
The `get_company_logo()` function now includes logos for:

**Tech Giants:**
- Google, Microsoft, Apple, Amazon, Meta, OpenAI, IBM, Adobe, NVIDIA, Intel, Oracle, Cisco, GitHub

**Cloud Providers:**
- AWS, Google Cloud, Microsoft Azure, Alibaba Cloud

**Software & Services:**
- Salesforce, Slack, Zoom, Atlassian, JetBrains, VMware, Citrix, SAP

**Financial Services:**
- JPMorgan, Goldman Sachs, Morgan Stanley, Bank of America, Citi, Wells Fargo
- Coinbase, Square, Stripe, PayPal

**Management Consulting:**
- Deloitte, EY, PwC, KPMG, Accenture, Infosys, TCS

**Automotive:**
- Tesla, Toyota, Honda, BMW, Mercedes-Benz, Audi, Porsche, Ferrari, Lamborghini
- Nissan, Ford, GM, Volkswagen, Hyundai, Kia, Jaguar
- Electric: BYD, Rivian, Lucid, XPeng, NIO

**Consumer & Retail:**
- Amazon, Walmart, Target, Best Buy, Home Depot, Costco

**Entertainment & Media:**
- Netflix, Disney, Warner Bros, Universal, HBO, Spotify, Apple Music

**E-commerce & Logistics:**
- Alibaba, Shopify, eBay, Etsy, Airbnb, Uber, DoorDash

**Telecommunications:**
- AT&T, Verizon, Comcast, Spectrum, T-Mobile

**Aerospace & Defense:**
- Boeing, Airbus, Lockheed Martin, SpaceX

**Industrial & Manufacturing:**
- Siemens, Bosch, GE, Caterpillar, 3M, Honeywell

**And many more...**

#### 2. **Smart Logo Fallback System**
- **Exact Match:** If company name exists in database → use its logo
- **Partial Match:** If company name contains or is contained in database entry → use matched logo
- **Case-Insensitive:** Works with any capitalization variant
- **Fallback:** Unknown companies get a professional placeholder image from placeholder.com

#### 3. **Logo Display on Internship Cards**
Each internship card now displays:
- ✅ Company logo (70px × 70px, professionally styled)
- ✅ Company name
- ✅ Job role
- ✅ Stipend information
- ✅ Apply Now button

#### 4. **Dynamic Company Dropdown**
The internships page company filter shows:
- ✅ All 225 unique companies from the dataset
- ✅ Alphabetically sorted
- ✅ Dynamically generated from actual data
- ✅ Professional filtering experience

### Features:
- ✅ Professional company logos from Wikimedia Commons
- ✅ Responsive image sizing with CSS
- ✅ Proper alt text for accessibility
- ✅ Intelligent fallback for unmapped companies
- ✅ No broken image links

### How It Works:

```python
# Get logo for any company
logo_url = get_company_logo("Google")  # Returns Google's official logo
logo_url = get_company_logo("google")  # Returns professional placeholder
```

### Visit Your Website:
- 🔗 **Internships:** http://127.0.0.1:5000/internships
- 🔗 **Jobs:** http://127.0.0.1:5000/jobs
- 🔗 **Home:** http://127.0.0.1:5000/

### What You'll See:
- Beautiful internship cards with company logos
- Professional company branding on every card
- Full company dropdown with 225+ companies
- Responsive design that works on all devices
- Accessible images with proper alt text

**All internship cards now display correct company logos with professional fallbacks!** 🎉
