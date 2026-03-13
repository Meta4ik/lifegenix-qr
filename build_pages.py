#!/usr/bin/env python3
"""
LifeGenix VIP Landing Page Generator
Generates 6 HTML pages — one per company partner.
"""

import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

COMPANIES = [
    {"slug": "strata",         "name": "STRATA",          "full": "Strata Commercial",  "code": 11,  "suffix": 93810},
    {"slug": "ypo",            "name": "YPO",              "full": "YPO",                "code": 26,  "suffix": 24592},
    {"slug": "cleanplacepros", "name": "CLEAN PLACE PROS", "full": "Clean Place Pros",   "code": 12,  "suffix": 13278},
    {"slug": "bannerhouse",    "name": "BANNER HOUSE",     "full": "Banner House",        "code": 26,  "suffix": 46048},
    {"slug": "parkhouse",      "name": "PARK HOUSE",       "full": "Park House",          "code": 33,  "suffix": 42098},
    {"slug": "edgerealty",     "name": "EDGE REALTY",      "full": "Edge Realty",         "code": 14,  "suffix": 39256},
    {"slug": "nexbank",         "name": "NEXBANK",           "full": "NexBank",              "code": 17,  "suffix": 58734},
]

def make_page(company):
    slug = company["slug"]
    name = company["name"]
    full = company["full"]
    code = company["code"]
    suffix = company["suffix"]
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
        <img src="LifeGenix_Logo_blue-1.svg" alt="LifeGenix" />
      </div>
    </header>

    <!-- HERO -->
    <section class="hero">
      <div class="vip-badge">VIP Member Exclusive</div>
      <h1>{name} <span>VIP Discounts</span></h1>
      <p>Exclusive benefits reserved for {full} members</p>
    </section>

    <div class="divider"><span class="divider-dot"></span><span class="divider-dot"></span><span class="divider-dot"></span></div>

    <!-- DISCOUNT CARDS -->
    <section class="cards-section">
      <p class="cards-label">Your Member Benefits</p>
      <div class="cards-grid">

        <div class="card">
          <span class="card-icon">🔬</span>
          <div class="card-title">Preventive Wellness &amp; Imaging</div>
          <div class="card-discount">20%</div>
          <span class="card-discount-label">Off Regular Price</span>
        </div>

        <div class="card">
          <span class="card-icon">🧬</span>
          <div class="card-title">Regenerative Services</div>
          <div class="card-discount">10%</div>
          <span class="card-discount-label">Off Regular Price</span>
        </div>

        <div class="card">
          <span class="card-icon">🩺</span>
          <div class="card-title">Non-Surgical Back Procedure</div>
          <div class="card-discount">10%</div>
          <span class="card-discount-label">Off Regular Price</span>
        </div>

      </div>
    </section>

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

    <!-- FOOTER / CODE -->
    <footer class="footer">
      <p class="footer-code-label">Your Member Code</p>
      <div class="footer-code"><span class="footer-code-prefix">#</span>{code}</div>
      <p class="footer-present">Present this page or provide your code number when calling</p>
      <p class="footer-brand">© 2025 <a href="https://lifegenix.com" target="_blank">LifeGenix.com</a> &nbsp;·&nbsp; All rights reserved</p>
    </footer>

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
    rows = ""
    for c in COMPANIES:
        fn = f"{c['slug']}-{c['suffix']}.html"
        rows += f'      <tr><td><a href="{fn}">{c["full"]}</a></td><td class="code">#{c["code"]}</td><td class="url">{fn}</td></tr>\n'

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LifeGenix VIP Pages — Index</title>
  <link rel="stylesheet" href="styles.css">
  <style>
    .index-wrap {{ max-width: 700px; margin: 60px auto; padding: 0 24px; }}
    h1 {{ font-family: 'Cormorant Garamond', serif; font-size: 36px; margin-bottom: 8px; }}
    table {{ width: 100%; border-collapse: collapse; margin-top: 32px; }}
    th {{ text-align: left; font-size: 10px; letter-spacing: 2px; text-transform: uppercase;
          color: var(--text-muted); padding: 0 0 12px; border-bottom: 1px solid rgba(37,174,212,0.2); }}
    td {{ padding: 14px 0; border-bottom: 1px solid rgba(255,255,255,0.05); vertical-align: middle; }}
    td a {{ color: var(--teal-light); text-decoration: none; font-weight: 500; }}
    td a:hover {{ text-decoration: underline; }}
    .code {{ color: var(--teal); font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 700; }}
    .url {{ color: var(--text-muted); font-size: 12px; }}
  </style>
</head>
<body>
  <div class="index-wrap">
    <div class="logo-wrap" style="margin-bottom:24px">
      <img src="LifeGenix_Logo_blue-1.svg" alt="LifeGenix" style="height:48px">
    </div>
    <h1>VIP Partner Pages</h1>
    <p style="color:var(--text-muted);font-size:14px">Internal index — do not share this page</p>
    <table>
      <thead><tr><th>Company</th><th>Code</th><th>URL</th></tr></thead>
      <tbody>
{rows}      </tbody>
    </table>
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
