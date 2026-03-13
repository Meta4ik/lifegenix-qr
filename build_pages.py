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
          <svg class="card-icon-svg" viewBox="0 0 116.73 122.88" fill="currentColor">
            <path d="M97.49,104.69a58.38,58.38,0,0,0-28-100.63l-.39-1.95A2.36,2.36,0,0,0,66.7,0H50.54A2.37,2.37,0,0,0,48.2,2l-.29,1.92a58.38,58.38,0,0,0-28.42,101l-.68,13.82a3.59,3.59,0,0,0,0,.47,3.68,3.68,0,0,0,3.68,3.68H94.7A3.68,3.68,0,0,0,98.19,119l-.7-14.33ZM50.54,2.37H66.7l4,20c.37,1.85-1.55,3.44-3.44,3.44H50.93c-1.88,0-3.7-1.56-3.42-3.42l3-20.06ZM73,24.24a5.23,5.23,0,0,1-1.33,2.18l-.17.16a6.41,6.41,0,0,1-3,1.51h0a6.45,6.45,0,0,1-1.17.11H50.93a6.36,6.36,0,0,1-.87-.06,6.06,6.06,0,0,1-3.35-1.68,5.24,5.24,0,0,1-1.51-2.76A39.76,39.76,0,0,0,26.14,84.49L36.55,60a3.67,3.67,0,0,1,3.38-2.24h4V51.45a4.66,4.66,0,0,1,1.37-3.29l.13-.11a4.59,4.59,0,0,1,3.15-1.25H68.45a4.62,4.62,0,0,1,3.25,1.35h0a4.59,4.59,0,0,1,1.36,3.25V57.8h4.36a3.69,3.69,0,0,1,3.49,2.49L97,98.94l-6.16-14.8A39.76,39.76,0,0,0,73,24.24ZM69.37,57.8V51.41a.91.91,0,0,0-.26-.65h0a.9.9,0,0,0-.65-.27H48.58a1,1,0,0,0-.62.23l-.06.06a1,1,0,0,0-.28.68V57.8ZM23.46,102.2H23.3l-.84,17H94.53l-.84-17H23.46Zm.71-3.68H92.84l-15.42-37H39.93l-15.76,37Z" />
          </svg>
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
