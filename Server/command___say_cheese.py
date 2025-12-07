#py command__say_cheese.py ./ -o project_bitmap.png


import os
import math
import argparse
import random
from typing import List
from PIL import Image


def collect_python_files(root: str) -> List[str]:
    """Return a list of all .py files under root (recursively)."""
    py_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        for name in filenames:
            if name.lower().endswith(".py"):
                py_files.append(os.path.join(dirpath, name))
    return py_files


def read_all_code(files: List[str]) -> str:
    """Read and concatenate all python files into a single string."""
    contents = []
    for path in files:
        try:
            with open(path, "r", encoding="utf-8", errors="replace") as f:
                contents.append(f.read())
                contents.append("\n")  # separator (optional)
        except Exception as e:
            print(f"Warning: could not read {path}: {e}")
    return "".join(contents)


def string_to_bitmap_data(s: str):
    """
    Convert a string to (width, height, pixels) where
    pixels is a flat list of grayscale values 0-255.
    """
    n = len(s)
    if n == 0:
        raise ValueError("No characters to encode (no .py files or all empty).")

    # Make it roughly square
    width = int(math.ceil(math.sqrt(n)))
    height = int(math.ceil(n / width))

    pixels = []
    for ch in s:
        # Map character to 0-255 grayscale
        v = random.randint(1,255)#ord(ch) % 256 #dont want to leak the code lol
        pixels.append(v)

    # Pad any remaining pixels with 0 (black)
    total_pixels = width * height
    if len(pixels) < total_pixels:
        pixels.extend([0] * (total_pixels - len(pixels)))

    return width, height, pixels


def save_bitmap(width: int, height: int, pixels, output_path: str):
    """Create and save a grayscale bitmap image from pixels."""
    img = Image.new("L", (width, height))  # "L" = 8-bit grayscale
    img.putdata(pixels)
    img.save(output_path)
    print(f"Saved image: {output_path}")
    print(f"Dimensions: {width} x {height} pixels")


def main():
    parser = argparse.ArgumentParser(
        description="Turn all .py files in a project into a bitmap image "
                    "where each pixel represents one character."
    )
    parser.add_argument("project_root", help="Path to project root directory")
    parser.add_argument(
        "-o", "--output",
        default="project_code_bitmap.png",
        help="Output image file (default: project_code_bitmap.png)"
    )
    args = parser.parse_args()

    root = os.path.abspath(args.project_root)
    print(f"Scanning for .py files in: {root}")

    files = collect_python_files(root)
    if not files:
        print("No .py files found. Exiting.")
        return

    print(f"Found {len(files)} Python files.")
    code = read_all_code(files)
    print(f"Total characters: {len(code)}")

    width, height, pixels = string_to_bitmap_data(code)
    save_bitmap(width, height, pixels, args.output)


if __name__ == "__main__":
    main()