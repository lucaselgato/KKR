# Kneading Kitty's Rescue website recreation

This folder is a static, responsive recreation of the current KKR website design and information architecture, prepared from the live site as of September 30, 2026.

## What is included

- Responsive header and mobile navigation
- Desktop dropdown menus matching the live site's current information architecture
- Home, About Us, Our Cats, adoption, adopter resources, donations, volunteer/foster, intake and events pages
- Special cat category pages (Featured Kitty, Bonded Pairs and Barn Cats)
- Current KKR typography direction: League Spartan for headings/navigation and Montserrat for body copy
- Current brand palette direction: white / near-black / light gray with KKR blue accents
- KKR logo fallback asset in `assets/kkr-logo.png`
- Lightweight cookie preference banner
- Real links to KKR's current applications/forms and PayPal donation page

## Important dependency: adoptable-cat feed

The current live KKR site appears to render its adoptable-cat listings dynamically. In this build, the cat-list pages link to the existing live feed so availability does not become stale. Before switching domains, connect those pages directly to KKR's RescueGroups feed/API or another approved pet-listing widget.

## Images

Several page images use the same public `img1.wsimg.com` assets referenced by the current KKR website. The official live KKR logo is also referenced first, with the local `assets/kkr-logo.png` file as a fallback.

## Preview locally

Open `index.html` directly, or run a local web server from this folder:

    python -m http.server 8000

Then visit `http://localhost:8000`.

## Recommended launch checklist

1. Replace the temporary live-list links with a direct RescueGroups integration.
2. Confirm all application/form destinations are still current.
3. Confirm PayPal hosted button IDs and donation flows.
4. Download/host KKR-owned images locally to remove dependence on GoDaddy's image CDN.
5. Add analytics only after selecting the desired privacy/cookie approach.
6. Test desktop, tablet and phone layouts before DNS/domain cutover.
