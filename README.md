# LifeGenix VIP Partner Pages

Exclusive VIP discount landing pages for LifeGenix.com partner companies.

## Pages & URLs

| Company | File | Code |
|---|---|---|
| STRATA | `strata-93810.html` | #11 |
| YPO | `ypo-24592.html` | #26 |
| CLEAN PLACE PROS | `cleanplacepros-13278.html` | #12 |
| BANNER HOUSE | `bannerhouse-46048.html` | #26 |
| PARK HOUSE | `parkhouse-42098.html` | #33 |
| EDGE REALTY | `edgerealty-39256.html` | #11 |

## Generating QR Codes

Once deployed, generate QR code PNGs pointing to the live URLs:

```bash
pip install qrcode[pil]
python3 generate_qr_codes.py
```

This will output one QR PNG per company (e.g. `strata-qr.png`).

## Regenerating Pages

To rebuild all HTML pages (e.g. after editing styles):

```bash
python3 build_pages.py
```

## Files

- `styles.css` — shared stylesheet (all pages use this)
- `LifeGenix_Logo_blue-1.svg` — logo (dark backgrounds)
- `LifeGenix_Logo_blue-w.svg` — logo (light backgrounds)
- `build_pages.py` — regenerates all HTML pages
- `generate_qr_codes.py` — generates QR code PNGs (run after deploy)
- `index.html` — internal index of all pages (do not share)
