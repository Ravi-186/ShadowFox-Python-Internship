"""
ShadowFox Python Internship - Task 2
Web Scraper using BeautifulSoup
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
from datetime import datetime


# ============================================
# Configuration
# ============================================
URL = "https://www.shadowfox.org.in/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


# ============================================
# 1. Fetch Webpage
# ============================================
def fetch_webpage(url):
    """
    Downloads the webpage content.
    Handles connection errors, timeouts, and HTTP errors.
    """
    try:
        print(f"Fetching: {url}")
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        print(f"✅ Success! Status Code: {response.status_code}")
        return response.text

    except requests.exceptions.Timeout:
        print("❌ Error: Request timed out.")
    except requests.exceptions.ConnectionError:
        print("❌ Error: Failed to connect to the website.")
    except requests.exceptions.HTTPError as err:
        print(f"❌ HTTP Error: {err}")
    except Exception as err:
        print(f"❌ Unexpected Error: {err}")

    return None


# ============================================
# 2. Extract Data from HTML
# ============================================
def extract_data(html):
    """
    Extracts:
    - Headings (h1, h2, h3, h4)
    - Links
    - Paragraphs
    """
    soup = BeautifulSoup(html, "html.parser")

    # ----- Extract Headings -----
    headings = []
    for tag in soup.find_all(["h1", "h2", "h3", "h4"]):
        text = tag.get_text(strip=True)
        if text:
            headings.append({
                "tag": tag.name,
                "text": text
            })

    # ----- Extract Links -----
    links = []
    seen = set()

    for a in soup.find_all("a", href=True):
        text = a.get_text(strip=True)
        href = a["href"].strip()

        if not href or href.startswith("#"):
            continue

        # Convert relative URL to absolute URL
        if href.startswith("/"):
            href = "https://www.shadowfox.org.in" + href

        if href not in seen:
            seen.add(href)
            links.append({
                "text": text if text else "(no text)",
                "url": href
            })

    # ----- Extract Paragraphs -----
    paragraphs = []
    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        if len(text) > 40:  # ignore very short texts
            paragraphs.append(text)

    return headings, links, paragraphs


# ============================================
# 3. Save Data
# ============================================
def save_csv(data, filename, fields):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)
    print(f"✅ CSV Saved → {filename}")


def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"✅ JSON Saved → {filename}")


# ============================================
# 4. Main Function
# ============================================
def main():
    print("=" * 55)
    print("        SHADOWFOX WEB SCRAPER")
    print("=" * 55)

    # Step 1: Fetch the page
    html = fetch_webpage(URL)
    if not html:
        print("Scraping failed.")
        return

    # Step 2: Extract data
    headings, links, paragraphs = extract_data(html)

    print(f"\n📊 Extracted Data Summary:")
    print(f"   Headings   : {len(headings)}")
    print(f"   Links      : {len(links)}")
    print(f"   Paragraphs : {len(paragraphs)}")

    # Show sample output
    print("\n--- Sample Headings ---")
    for h in headings[:5]:
        print(f"[{h['tag']}] {h['text']}")

    print("\n--- Sample Links ---")
    for link in links[:5]:
        print(f"{link['text'][:35]:<35} → {link['url']}")

    # Step 3: Save files
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    save_csv(headings, f"shadowfox_headings_{timestamp}.csv", ["tag", "text"])
    save_csv(links, f"shadowfox_links_{timestamp}.csv", ["text", "url"])

    full_report = {
        "website": URL,
        "scraped_at": datetime.now().isoformat(),
        "summary": {
            "headings": len(headings),
            "links": len(links),
            "paragraphs": len(paragraphs)
        },
        "headings": headings,
        "links": links,
        "paragraphs": paragraphs
    }

    save_json(full_report, f"shadowfox_report_{timestamp}.json")

    print("\n" + "=" * 55)
    print("Scraping Completed Successfully!")
    print("=" * 55)


# ============================================
# Run the Program
# ============================================
if __name__ == "__main__":
    main()