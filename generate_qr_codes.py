#!/usr/bin/env python3
"""
Run: pip install qrcode[pil]
Then: python3 generate_qr_codes.py
"""

import qrcode
from qrcode.constants import ERROR_CORRECT_H

BASE_URL = "https://lifegenix-qr.vercel.app/"

PAGES = [
    ("strata", "strata-93810.html"),
    ("ypo", "ypo-24592.html"),
    ("cleanplacepros", "cleanplacepros-13278.html"),
    ("bannerhouse", "bannerhouse-46048.html"),
    ("parkhouse", "parkhouse-42098.html"),
    ("edgerealty", "edgerealty-39256.html"),
]

for name, page in PAGES:
    url = BASE_URL + page
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#071525", back_color="white")
    out = f"{name}-qr.png"
    img.save(out)
    print(f"  ✅  {out}  →  {url}")

print("\nAll QR codes saved!")