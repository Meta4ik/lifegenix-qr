#!/usr/bin/env python3
"""
LifeGenix VIP Landing Page Generator
Generates 6 HTML pages — one per company partner.
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

COMPANIES = [
    {"slug": "strata",         "name": "STRATA",          "full": "Strata Commercial",  "code": 11,  "suffix": 93810, "imaging": 20},
    {"slug": "ypo",            "name": "YPO",              "full": "YPO",                "code": 26,  "suffix": 24592, "imaging": 25},
    {"slug": "cleanplacepros", "name": "CLEAN PLACE PROS", "full": "Clean Place Pros",   "code": 12,  "suffix": 13278, "imaging": 20},
    {"slug": "bannerhouse",    "name": "BANNER HOUSE",     "full": "Banner House",        "code": 26,  "suffix": 46048, "imaging": 25},
    {"slug": "parkhouse",      "name": "PARK HOUSE",       "full": "Park House",          "code": 33,  "suffix": 42098, "imaging": 25},
    {"slug": "edgerealty",     "name": "EDGE REALTY",      "full": "Edge Realty",         "code": 14,  "suffix": 39256, "imaging": 20},
    {"slug": "nexbank",         "name": "NEXBANK",           "full": "NexBank",              "code": 17,  "suffix": 58734, "imaging": 20},
]

def make_page(company):
    slug = company["slug"]
    name = company["name"]
    full = company["full"]
    code = company["code"]
    suffix = company["suffix"]
    imaging = company["imaging"]
    filename = f"{slug}-{suffix}.html"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{full} VIP Discounts — LifeGenix</title>
  <meta name="robots" content="noindex, nofollow">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="page-wrapper">

    <!-- HEADER -->
    <header class="header">
      <div class="logo-wrap">
        <img src="LifeGenix_Logo_blue-w.svg" alt="LifeGenix" />
      </div>
    </header>

    <!-- HERO -->
    <section class="hero">
      <div class="vip-badge">VIP Member Exclusive</div>
      <h1>{name}<br><span>VIP Discounts</span></h1>
      <p>Exclusive benefits reserved for {full} members</p>
    </section>

    <div class="divider"><span class="divider-dot"></span><span class="divider-dot"></span><span class="divider-dot"></span></div>

    <!-- DISCOUNT CARDS -->
    <section class="cards-section">
      <p class="cards-label">Your Member Benefits</p>
      <div class="cards-grid">

        <div class="card">
          <svg class="card-icon-svg" viewBox="0 0 1200 1200" fill="currentColor">
            <path d="m0.27734 703.61h758.54v71.102h-758.54z"/>
            <path d="m595.64 554.14c0-49.727 40.32-89.977 89.977-89.977 49.609 0 90.035 40.246 90.035 89.977 0 49.57-40.43 90-90.035 90-49.656 0-89.977-40.426-89.977-90z"/>
            <path d="m480.6 461.02h-301.39l-179.21 27.43v155.57l90.445 0.046875c-7.1758-11.617-11.52-25.176-11.52-39.758 0-42 34.141-76.129 76.129-76.129h165.06l133.79-27.961 7.4141 35.531-137.46 28.715-168.82 0.007812c-22.008 0-39.828 17.82-39.828 39.84 0 21.805 17.543 39.48 39.312 39.758l326.8 0.035157c50.52-0.39453 91.078-41.113 91.078-91.441 0-50.566-40.906-91.641-91.797-91.641z"/>
            <path d="m636.56 965.59c201.07 0 364.04-163 364.04-364.07 0-201.09-162.97-364.07-364.04-364.07-131.44 0-246.28 69.949-310.29 174.39h152.46c42.996-36.012 98.293-57.742 158.76-57.742 136.62 0 247.39 110.79 247.39 247.41 0 136.67-110.77 247.45-247.39 247.45-38.773 0-75.289-9.1797-107.95-25.055l-180.74-0.003907c66.562 86.039 170.55 141.67 287.76 141.67z"/>
            <path d="m636.56 36.57c-249.12 0-460.3 161.8-534.67 385.97l69.434-10.812 112.66 0.035157c67.621-125.42 200.14-210.68 352.58-210.68 221.16 0 400.4 179.3 400.4 400.44 0 221.17-179.26 400.43-400.4 400.43-138.85 0-261.12-70.754-332.94-178.11h-184.11c86.566 199.75 285.45 339.59 517.04 339.59 311.18-0.003906 563.45-252.24 563.45-563.43 0-311.16-252.27-563.44-563.44-563.44zm127.85 128.14c-2.0391 8.1367-9.2891 13.559-17.305 13.559-1.4414 0-2.9141-0.15625-4.3438-0.55078-68.746-17.148-141.77-17.148-210.59 0-9.5625 2.5547-19.262-3.4336-21.66-12.996-2.3867-9.5625 3.4336-19.262 13.043-21.648 74.449-18.59 153.42-18.59 227.86 0 9.5703 2.375 15.391 12.059 13 21.637z"/>
          </svg>
          <div class="card-title">Preventive Wellness &amp; Imaging</div>
          <div class="card-discount">{imaging}%</div>
          <span class="card-discount-label">Off Regular Price</span>
        </div>

        <div class="card">
          <span class="card-icon">🧬</span>
          <div class="card-title">Regenerative Services</div>
          <div class="card-discount">10%</div>
          <span class="card-discount-label">Off Regular Price</span>
        </div>

        <div class="card">
          <svg class="card-icon-svg" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12,2L12,2c-0.6,0-1,0.4-1,1s0.4,1,1,1s1-0.4,1-1S12.6,2,12,2z M12,5L12,5c-0.6,0-1,0.4-1,1s0.4,1,1,1s1-0.4,1-1S12.6,5,12,5z M12,8L12,8c-1.1,0-2,0.9-2,2s0.9,2,2,2s2-0.9,2-2S13.1,8,12,8z M12,13L12,13c-1.1,0-2,0.9-2,2s0.9,2,2,2s2-0.9,2-2S13.1,13,12,13z M12,18L12,18c-1.1,0-2,0.9-2,2s0.9,2,2,2s2-0.9,2-2S13.1,18,12,18z M8,10L8,10c0,0.6,0.4,1,1,1h6c0.6,0,1-0.4,1-1s-0.4-1-1-1H9C8.4,9,8,9.4,8,10z M7,15L7,15c0,0.6,0.4,1,1,1h8c0.6,0,1-0.4,1-1s-0.4-1-1-1H8C7.4,14,7,14.4,7,15z M8,20L8,20c0,0.6,0.4,1,1,1h6c0.6,0,1-0.4,1-1s-0.4-1-1-1H9C8.4,19,8,19.4,8,20z"/>
          </svg>
          <div class="card-title">Non-Surgical Back Procedure</div>
          <div class="card-discount">10%</div>
          <span class="card-discount-label">Off Regular Price</span>
        </div>

      </div>
    </section>

    <!-- CTA + CODE ROW -->
    <div class="bottom-row">

      <!-- CTA -->
      <section class="cta-section">
        <h2>Schedule Your Appointment</h2>
        <p>Call us to book and mention your member code to unlock your discounts</p>
        <a href="tel:9722363333" class="cta-phone">
          <span class="phone-icon">📞</span>
          972-236-3333
        </a>
        <p class="cta-note">Provide your member code <strong style="color:var(--teal)">#{code}</strong> when scheduling</p>
      </section>

      <!-- MEMBER CODE -->
      <footer class="footer">
        <p class="footer-code-label">Your Member Code</p>
        <div class="footer-code"><span class="footer-code-prefix">#</span>{code}</div>
        <p class="footer-present">Present this page or provide your code number when calling</p>
      </footer>

    </div>

    <div class="bottom-brand">
      <p class="footer-brand">© 2026 <a href="https://lifegenix.com" target="_blank">LifeGenix.com</a> &nbsp;·&nbsp; All rights reserved</p>
    </div>

  </div>
</body>
</html>"""

    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w") as f:
        f.write(html)
    print(f"  ✅  {filename}  (Code #{code})")
    return filename

def make_qr_generator():
    """Write the QR code generator script (requires qrcode + Pillow)."""
    lines = ['#!/usr/bin/env python3', '"""', 'Run: pip install qrcode[pil]', 'Then: python3 generate_qr_codes.py', '"""', '', 'import os', 'import qrcode', 'from qrcode.constants import ERROR_CORRECT_H', '', 'os.makedirs("qr-codes", exist_ok=True)', '', 'BASE_URL = "https://lifegenix-qr.vercel.app/"', '', 'PAGES = [']
    for c in COMPANIES:
        lines.append(f'    ("{c["slug"]}", "{c["slug"]}-{c["suffix"]}.html"),')
    lines += [']', '', 'for name, page in PAGES:', '    url = BASE_URL + page', '    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=10, border=4)', '    qr.add_data(url)', '    qr.make(fit=True)', '    img = qr.make_image(fill_color="#071525", back_color="white")', '    out = f"qr-codes/{name}-qr.png"', '    img.save(out)', '    print(f"  ✅  {out}  →  {url}")', '', 'print("\\nAll QR codes saved!")']
    path = os.path.join(OUTPUT_DIR, "generate_qr_codes.py")
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"  📄  generate_qr_codes.py written")

def make_index():
    cards = ""
    for c in COMPANIES:
        fn = f"{c['slug']}-{c['suffix']}.html"
        cards += f"""
      <div class="partner-card">
        <div class="partner-qr">
          <img src="qr-codes/{c['slug']}-qr.png" alt="{c['full']} QR Code">
        </div>
        <div class="partner-body">
          <div class="partner-name">{c['full']}</div>
          <div class="partner-code"><span>#</span>{c['code']}</div>
          <a href="{fn}" class="partner-link">Open page</a>
        </div>
      </div>
"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LifeGenix VIP Pages — Index</title>
  <meta name="robots" content="noindex, nofollow">
  <link rel="stylesheet" href="styles.css">
  <style>
    .index-wrap {{
      max-width: 960px;
      margin: 0 auto;
      padding: 48px 24px 80px;
      position: relative;
      z-index: 1;
    }}
    .index-header {{ text-align: center; margin-bottom: 48px; animation: fadeDown 0.7s ease both; }}
    .index-header .logo-wrap {{ margin-bottom: 20px; }}
    .index-header h1 {{ font-family: 'Syne', sans-serif; font-size: clamp(28px, 5vw, 40px); font-weight: 700; margin-bottom: 6px; }}
    .index-header p {{ font-size: 13px; color: var(--text-muted); letter-spacing: 1px; }}
    .partner-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; }}
    .partner-card {{ background: rgba(255,255,255,0.03); border: 1px solid rgba(37,174,212,0.18); border-radius: 20px; overflow: hidden; display: flex; flex-direction: column; transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease; animation: fadeUp 0.6s ease both; position: relative; }}
    .partner-card::before {{ content: ''; position: absolute; inset: 0; background: radial-gradient(ellipse 80% 50% at 50% 0%, rgba(37,174,212,0.07) 0%, transparent 70%); pointer-events: none; }}
    .partner-card:hover {{ transform: translateY(-4px); border-color: rgba(37,174,212,0.45); box-shadow: 0 16px 40px rgba(37,174,212,0.12); }}
    .partner-qr {{ background: white; display: flex; align-items: center; justify-content: center; padding: 20px; }}
    .partner-qr img {{ width: 100%; max-width: 180px; height: auto; display: block; border-radius: 4px; }}
    .partner-body {{ padding: 20px 20px 22px; display: flex; flex-direction: column; gap: 4px; flex: 1; }}
    .partner-name {{ font-family: 'Syne', sans-serif; font-size: 15px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: var(--offwhite); }}
    .partner-code {{ font-family: 'Syne', sans-serif; font-size: 28px; font-weight: 700; color: var(--teal); letter-spacing: -0.5px; line-height: 1.1; text-shadow: 0 0 20px rgba(37,174,212,0.4); }}
    .partner-code span {{ font-size: 14px; font-weight: 400; opacity: 0.5; letter-spacing: 0; }}
    .partner-link {{ display: inline-flex; align-items: center; gap: 6px; margin-top: 12px; font-size: 12px; font-weight: 600; letter-spacing: 1.5px; text-transform: uppercase; color: var(--teal-light); text-decoration: none; opacity: 0.8; transition: opacity 0.2s ease; }}
    .partner-link:hover {{ opacity: 1; text-decoration: underline; }}
    .partner-link::after {{ content: '→'; font-size: 14px; }}
  </style>
</head>
<body>
  <div class="index-wrap">
    <div class="index-header">
      <div class="logo-wrap">
        <img src="LifeGenix_Logo_blue-w.svg" alt="LifeGenix" style="height:52px">
      </div>
      <h1>VIP Partner Pages</h1>
      <p style="color:#e05555;">Internal index — do not share this page</p>
    </div>
    <div class="partner-grid">
{cards}    </div>
  </div>
</body>
</html>"""
    path = os.path.join(OUTPUT_DIR, "index.html")
    with open(path, "w") as f:
        f.write(html)
    print(f"  📋  index.html written")

if __name__ == "__main__":
    print("\n🏥  LifeGenix VIP Page Generator\n")
    print("── Landing Pages ──────────────────────")
    filenames = [make_page(c) for c in COMPANIES]
    print("\n── Support Files ──────────────────────")
    make_qr_generator()
    make_index()
    print("\n── URL Summary ────────────────────────")
    for c, fn in zip(COMPANIES, filenames):
        print(f"  {c['name']:<18} → https://lifegenix.com/{fn}")
    print("\n✅  Done! Upload the whole folder to GitHub.\n")
    print("   To generate QR PNG files, run:")
    print("   pip install qrcode[pil] && python3 generate_qr_codes.py\n")
