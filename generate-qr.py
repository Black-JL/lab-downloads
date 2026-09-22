#!/usr/bin/env python3
"""
Generate the QR code that students scan to reach the lab downloads site.

Usage:
    python3 generate-qr.py [URL]

If no URL is given, uses the default placeholder.
Output: qr-code.png in the same directory as this script.
"""
import sys
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from pathlib import Path

DEFAULT_URL = "https://black-jl.github.io/lab-downloads/"

def main():
    url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer(),
        color_mask=SolidFillColorMask(
            front_color=(31, 58, 95),
            back_color=(255, 255, 255),
        ),
    )

    out = Path(__file__).parent / "qr-code.png"
    img.save(out)
    print(f"QR code saved to: {out}")
    print(f"URL encoded: {url}")
    print(f"Size: {img.size[0]}x{img.size[1]}px")
    print()
    print("To regenerate with a different URL:")
    print(f"    python3 {Path(__file__).name} https://your-actual-url.example/")

if __name__ == "__main__":
    main()
