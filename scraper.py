import time
from playwright.sync_api import sync_playwright

AIRPORT_NAMES = {
    "JNB": "Johannesburg",
    "CPT": "Cape Town",
    "DUR": "Durban",
}

def scrape_lift(origin, dest):
    origin_name = AIRPORT_NAMES.get(origin, origin)
    dest_name = AIRPORT_NAMES.get(dest, dest)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.lift.co.za/")
        page.wait_for_timeout(3000)

        # lets dismiss the cookie stuff
        page.click("button[data-action='select']")

       # always select 1 way trip
        page.click("#type_OW")

        # From destinationn
        page.click("#flightFrom")
        page.fill("#flightFrom", origin_name)
        page.wait_for_selector("#eac-container-flightFrom li", timeout=5000)
        page.click(f"#eac-container-flightFrom div.eac-item:has-text('{origin_name}')")

        # To destination
        page.click("#flightTo")
        page.fill("#flightTo", dest_name)
        page.wait_for_selector("#eac-container-flightTo li", timeout=5000)
        page.click(f"#eac-container-flightTo div.eac-item:has-text('{dest_name}')")

        # click and open the callender
        page.click("#flightDepart")
        page.wait_for_selector("a[data-daynumber]", timeout=8000)

        # Grab everything 
        day_cells = page.query_selector_all("a[data-daynumber]")

        results = []
        for cell in day_cells:
            day = cell.get_attribute("data-daynumber")
            month = cell.get_attribute("data-monthnumber")
            year = cell.get_attribute("data-year")
            price_el = cell.query_selector("span")
            price_text = price_el.inner_text() if price_el else None
            if price_text and "R" in price_text:
                results.append({
                    "date": f"{year}-{month}-{day}",
                    "price": price_text
                })

        browser.close()
        return results


if __name__ == "__main__":
    result = scrape_lift("JNB", "CPT")
    print(result)