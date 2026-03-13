#!/usr/bin/env python3
"""
Run: pip install qrcode[pil]
Then: python3 generate_qr_codes.py
"""

import os
import qrcode
from qrcode.constants import ERROR_CORRECT_H

os.makedirs("qr-codes", exist_ok=True)

BASE_URL = "https://lifegenix-qr.vercel.app/"

PAGES = [
    ("strata", "strata-93810.html"),
    ("cleanplacepros", "cleanplacepros-13278.html"),
    ("edgerealty", "edgerealty-39256.html"),
    ("hiley", "hiley-74218.html"),
    ("nexbank", "nexbank-58734.html"),
    ("bannerhouse", "bannerhouse-46048.html"),
    ("parkhouse", "parkhouse-42098.html"),
    ("ypo", "ypo-24592.html"),
]

for name, page in PAGES:
    url = BASE_URL + page
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#071525", back_color="white")
    out = f"qr-codes/{name}-qr.png"
    img.save(out)
    print(f"  ✅  {out}  →  {url}")

print("\nAll QR codes saved!")