from pathlib import Path
from textwrap import dedent

ROOT=Path('/mnt/data/kkr-site')

LIVE='https://kneadingkittysrescueaz.com'
LOGO='https://img1.wsimg.com/isteam/ip/bb65a8ae-daa2-4f8a-8d57-0bc05cca36c1/kkr_logo.png/:/rs=h:100,cg:true,m/qt=q:95'
HERO='https://img1.wsimg.com/isteam/stock/3974/:/'
ABOUT_IMG='https://img1.wsimg.com/isteam/stock/84969/:/cr=t:0%,l:0%,w:100%,h:100%/rs=w:400,cg:true'
DONATE_IMG='https://img1.wsimg.com/isteam/stock/93386/:/cr=t:0%,l:0%,w:100%,h:100%/rs=w:400,cg:true'
EVENT_IMG='https://img1.wsimg.com/isteam/getty/2218955784/:/cr=t:0%,l:0%,w:100%,h:100%/rs=w:1240,cg:true'
FEATURED_IMG='https://img1.wsimg.com/isteam/stock/88187/:/cr=t:0%,l:0%,w:100%,h:100%/rs=w:400,cg:true'
BONDED_IMG='https://img1.wsimg.com/isteam/ip/bb65a8ae-daa2-4f8a-8d57-0bc05cca36c1/blob-689c455.png/:/cr=t:0%,l:0%,w:100%,h:100%/rs=w:400,cg:true'
BARN_IMG='https://img1.wsimg.com/isteam/stock/30438/:/rs=w:400,cg:true,m'
MONEY_IMG='https://img1.wsimg.com/isteam/stock/108868/:/rs=w:400,cg:true,m'
THANKS_IMG='https://img1.wsimg.com/isteam/stock/Ar3G9ky/:/rs=w:400,cg:true,m'

def active(cls, key): return ' active' if cls==key else ''

def header(which='home'):
    return dedent(f'''\
    <a class="skip-link" href="#main">Skip to content</a>
    <header class="site-header">
      <div class="header-inner">
        <a class="brand" href="index.html" aria-label="Kneading Kitty's Rescue home">
          <img src="{LOGO}" data-fallback="assets/kkr-logo.png" alt="Kneading Kitty's Rescue logo">
          <span class="brand-text">Kneading Kitty's<br>Rescue</span>
        </a>
        <button class="menu-btn" aria-label="Toggle navigation" aria-expanded="false">☰</button>
        <nav class="nav" aria-label="Main navigation">
          <a class="{active(which,'home').strip()}" href="index.html">Home</a>
          <a class="{active(which,'about').strip()}" href="about.html">About Us</a>
          <div class="dropdown{active(which,'cats')}">
            <button class="dropbtn" aria-expanded="false">Our Cats</button>
            <div class="dropdown-menu">
              <a href="at-petsmart.html">At PetSmart</a>
              <a href="at-foster.html">At Foster</a>
              <a href="all-list.html">All (List View)</a>
              <a href="all-thumbnail.html">All (Thumbnail View)</a>
              <a href="featured-kitty.html">Featured Kitty</a>
              <a href="bonded-pairs.html">Bonded Pairs</a>
              <a href="barn-cats.html">Barn Cats</a>
            </div>
          </div>
          <div class="dropdown{active(which,'adopt')}">
            <button class="dropbtn" aria-expanded="false">Adopt</button>
            <div class="dropdown-menu">
              <a href="adopt.html">Adopt From Us</a>
              <a href="adopter-resources.html">Adopter Resources</a>
            </div>
          </div>
          <div class="dropdown{active(which,'donate')}">
            <button class="dropbtn" aria-expanded="false">Donate</button>
            <div class="dropdown-menu">
              <a href="donate.html">Ways To Donate</a>
              <a href="monetary-donations.html">Monetary Donations</a>
              <a href="special-thanks.html">Special Thanks</a>
            </div>
          </div>
          <a class="{active(which,'involved').strip()}" href="involved.html">Get Involved</a>
          <a class="{active(which,'intake').strip()}" href="intake.html">Intake</a>
          <a class="{active(which,'events').strip()}" href="events.html">Events</a>
        </nav>
      </div>
    </header>
    ''')

def footer():
    return dedent('''\
    <footer class="site-footer">
      <div class="footer-inner">
        <img class="footer-logo" src="https://img1.wsimg.com/isteam/ip/bb65a8ae-daa2-4f8a-8d57-0bc05cca36c1/kkr_logo.png/:/rs=h:100,cg:true,m/qt=q:95" data-fallback="assets/kkr-logo.png" alt="Kneading Kitty's Rescue">
        <div class="footer-nav"><a href="index.html">Home</a><a href="about.html">About Us</a><a href="cats.html">Our Cats</a><a href="adopt.html">Adopt</a><a href="donate.html">Donate</a><a href="involved.html">Get Involved</a><a href="intake.html">Intake</a><a href="events.html">Events</a></div>
        <p>Email: <a href="mailto:info@kneadingkittysrescueaz.com">info@kneadingkittysrescueaz.com</a></p>
        <p>Copyright © 2026 Kneading Kitty's Rescue - All Rights Reserved.</p>
      </div>
    </footer>
    <div class="cookie-banner" role="dialog" aria-label="Cookie notice">
      <h3>This website uses cookies.</h3>
      <p>Cookies may be used to understand site traffic and improve the experience. Your choice is stored only in this browser for this prototype.</p>
      <div class="cookie-actions"><button data-cookie-choice="declined">Decline Cookies</button><button class="accept" data-cookie-choice="accepted">Accept Cookies</button></div>
    </div>
    <script src="assets/script.js"></script>
    ''')

def page(title, which, body, desc='Kneading Kitty\'s Rescue — helping Arizona cats and kittens find loving forever homes.'):
    html = f'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="stylesheet" href="assets/styles.css">
</head><body>
{header(which)}
{body}
{footer()}
</body></html>'''
    return html


def titleblock(title, subtitle=''):
    s=f'<div class="page-title"><div class="inner"><h1>{title}</h1><div class="rule"></div>'
    if subtitle: s+=f'<p>{subtitle}</p>'
    return s+'</div></div>'

home = f'''
<main id="main">
<section class="hero" style="background-image:linear-gradient(rgba(0,0,0,.18),rgba(0,0,0,.22)),url('{HERO}')"><div class="hero-inner"><h1>Kneading Kitty's Rescue</h1><p>Helping Arizona's kittens and cats in need to find loving forever homes!</p></div></section>
<section class="home-actions" aria-label="Ways to connect with the rescue">
  <article class="home-action"><h2>Available Cats</h2><p>We have dozens of kitties looking for their forever homes.</p><a class="btn" href="cats.html">Search For A Kitty</a></article>
  <article class="home-action"><h2>Adopt</h2><p>Meet a kitty or begin our adoption process.</p><a class="btn" href="adopt.html">Take The Next Step</a></article>
  <article class="home-action"><h2>Donate</h2><p>We rely entirely on donations and every donation helps.</p><a class="btn" href="donate.html">Ways To Donate</a></article>
  <article class="home-action"><h2>Get Involved</h2><p>Join our team as an adoption center volunteer or foster.</p><a class="btn" href="involved.html">Ways To Help</a></article>
</section>
</main>
'''
(ROOT/'index.html').write_text(page("Kneading Kitty's Rescue",'home',home),encoding='utf-8')

about = titleblock("About Kneading Kitty's Rescue") + f'''
<main id="main"><section class="section">
<div class="image-copy"><div class="media"><img class="feature-image" src="{ABOUT_IMG}" alt="Cat resting comfortably"></div><div class="copy content-block"><h2>Our Purpose</h2><p>Kneading Kitty's Rescue is a no-kill, nonprofit 501(c)(3), foster-based cat rescue and adoption organization. Cats and kittens are medically prepared for adoption with spay or neuter surgery, deworming, vaccines, FIV/FeLV testing, microchipping and veterinary checks.</p><p>The rescue's foster network provides care, comfort and socialization while adopters are screened so each kitty can be matched with a suitable forever home.</p></div></div>
<div class="content-block"><h2>Our Impact</h2><p>The rescue began helping cats in 2017, formally organized as a nonprofit in 2018, and began its PetSmart partnership in 2019.</p><div class="stat-grid">
<div class="stat"><strong>131</strong><span>Adoptions in 2018</span></div><div class="stat"><strong>84</strong><span>Adoptions in 2019</span></div><div class="stat"><strong>147</strong><span>Adoptions in 2020</span></div><div class="stat"><strong>256</strong><span>Adoptions in 2021</span></div><div class="stat"><strong>315</strong><span>Adoptions in 2022</span></div><div class="stat"><strong>502</strong><span>Adoptions in 2023</span></div><div class="stat"><strong>546</strong><span>Adoptions in 2024</span></div><div class="stat"><strong>540</strong><span>Adoptions in 2025</span></div><div class="stat"><strong>258</strong><span>Jan–Jun 2026</span></div></div></div>
<div class="grid-2"><div class="content-block"><h2>Our Location</h2><p>KKR is foster based, so most cats stay in homes across the greater Phoenix metro area. The rescue is also a PetSmart Charities partner with an adoption center in North Scottsdale where some kitties may be available for same-day adoption.</p><div class="action-row"><a class="btn" href="at-petsmart.html">PetSmart Kitties</a></div></div><div class="content-block"><h2>Our Team</h2><p>KKR is supported by roughly eighty fosters and adoption-center volunteers.</p><p><strong>Jeanne R.</strong> — President, West Valley Foster Coordinator &amp; Medical Director<br><strong>Amanda M.</strong> — Treasurer, East Valley Foster Coordinator &amp; Medical Director<br><strong>Bill S.</strong> — Secretary, Animal Rescue &amp; Veterinary Care Director</p></div></div>
<div class="callout"><strong>Tax Status:</strong> Kneading Kitty's Rescue is an IRS-recognized 501(c)(3) nonprofit based in Glendale, Arizona. EIN 82-5069525.</div>
</section></main>'''
(ROOT/'about.html').write_text(page("About Us — Kneading Kitty's Rescue",'about',about),encoding='utf-8')

cats = titleblock('Our Cats','Choose the view that best matches how you want to browse currently available KKR cats.') + f'''
<main id="main"><section class="section narrow flush-top">
<div class="grid-2">
  <div class="card"><h3>At PetSmart</h3><p>Cats currently housed at the KKR PetSmart Adoption Center in North Scottsdale.</p><a class="btn" href="at-petsmart.html">View At PetSmart</a></div>
  <div class="card"><h3>At Foster</h3><p>Cats currently living with foster families around the greater Phoenix area.</p><a class="btn" href="at-foster.html">View At Foster</a></div>
  <div class="card"><h3>All Cats</h3><p>Open the complete live KKR listing in either list or thumbnail format.</p><div class="action-row"><a class="btn secondary" href="all-list.html">List View</a><a class="btn secondary" href="all-thumbnail.html">Thumbnail View</a></div></div>
  <div class="card"><h3>Special Categories</h3><p>Learn about featured special-needs cats, bonded pairs, and barn or companion cats.</p><div class="action-row"><a class="btn text" href="featured-kitty.html">Featured Kitty</a><a class="btn text" href="bonded-pairs.html">Bonded Pairs</a><a class="btn text" href="barn-cats.html">Barn Cats</a></div></div>
</div>
<div class="callout"><strong>Our Health Promise:</strong> KKR cats are spayed/neutered, dewormed, current on vaccines, tested for FIV/FeLV, microchipped and vet checked before adoption.</div>
</section></main>'''
(ROOT/'cats.html').write_text(page("Our Cats — Kneading Kitty's Rescue",'cats',cats),encoding='utf-8')


def cat_listing_page(name, live_path, message):
    body=titleblock(name)+f'''<main id="main"><section class="section narrow flush-top"><div class="content-block"><h3>Ready to meet or adopt a kitty?</h3><p>{message}</p><div class="callout"><strong>Our Health Promise:</strong> KKR cats are spayed/neutered, dewormed, current on vaccines, tested for FIV/FeLV, microchipped and vet checked before adoption.</div><div class="action-row"><a class="btn" href="{LIVE}{live_path}" target="_blank" rel="noopener">Open Live Cat Listings</a><a class="btn secondary" href="adopt.html">Take The Next Step</a></div><p style="margin-top:24px;color:#666;font-size:13px">The adoptable-cat feed is kept live on KKR's current website so availability stays current while this replacement site is being prepared for a direct RescueGroups feed connection.</p></div></section></main>'''
    return page(f"{name} — Kneading Kitty's Rescue",'cats',body)

(ROOT/'at-petsmart.html').write_text(cat_listing_page('Available Cats - At PetSmart','/at-petsmart','Visit the live list for cats currently at the PetSmart Adoption Center.'),encoding='utf-8')
(ROOT/'at-foster.html').write_text(cat_listing_page('Available Cats - At Foster Homes','/at-foster','Visit the live list for cats currently staying with KKR foster families.'),encoding='utf-8')
(ROOT/'all-list.html').write_text(cat_listing_page('Available Cats','/all-list-view-1','Browse all currently available KKR cats in list format.'),encoding='utf-8')
(ROOT/'all-thumbnail.html').write_text(cat_listing_page('Available Cats','/all-thumbnail-view-1','Browse all currently available KKR cats in thumbnail format.'),encoding='utf-8')

featured = titleblock('Featured Kitty')+f'''<main id="main"><section class="section"><div class="image-copy"><div class="media"><img class="feature-image" src="{FEATURED_IMG}" alt="Cat looking toward the camera"></div><div class="copy content-block"><p>KKR regularly accepts cats with medical, behavioral or other special needs that may require more time and resources than a typical adoption case.</p><p>This page highlights a current rescue with a special story or a need for an experienced, committed adopter.</p><div class="action-row"><a class="btn" href="{LIVE}/featured-kitty" target="_blank" rel="noopener">See Current Featured Kitty</a><a class="btn secondary" href="mailto:info@kneadingkittysrescueaz.com">Email KKR</a></div></div></div></section></main>'''
(ROOT/'featured-kitty.html').write_text(page("Featured Kitty — Kneading Kitty's Rescue",'cats',featured),encoding='utf-8')

bonded = titleblock('Bonded Pairs')+f'''<main id="main"><section class="section"><div class="image-copy"><div class="media"><img class="feature-image" src="{BONDED_IMG}" alt="Two cats curled up together"></div><div class="copy content-block"><p>Some adult cats form close emotional bonds and do best when they stay together. When KKR has a bonded pair available, both cats are placed together rather than separated.</p><p>For adopters who want two adult cats, a bonded pair can offer a ready-made companionship where the cats already rely on and comfort one another.</p><div class="action-row"><a class="btn" href="{LIVE}/bonded-pairs" target="_blank" rel="noopener">See Current Bonded Pairs</a><a class="btn secondary" href="mailto:info@kneadingkittysrescueaz.com">Join Waiting List</a></div></div></div></section></main>'''
(ROOT/'bonded-pairs.html').write_text(page("Bonded Pairs — Kneading Kitty's Rescue",'cats',bonded),encoding='utf-8')

barn = titleblock('Barn Cats')+f'''<main id="main"><section class="section"><div class="image-copy"><div class="media"><img class="feature-image" src="{BARN_IMG}" alt="Barn setting"></div><div class="copy content-block"><p>Some rescued adult cats do not become comfortable enough with people to thrive as indoor house pets. When return to their original colony is not possible, KKR may place them as barn or companion cats after veterinary care.</p><p>An appropriate property provides secure shelter, fresh water and supplemental food while allowing the cat to live with more independence.</p><div class="action-row"><a class="btn" href="{LIVE}/barn-cats" target="_blank" rel="noopener">See Current Barn Cats</a><a class="btn secondary" href="mailto:info@kneadingkittysrescueaz.com">Ask About Barn Cats</a></div></div></div></section></main>'''
(ROOT/'barn-cats.html').write_text(page("Barn Cats — Kneading Kitty's Rescue",'cats',barn),encoding='utf-8')

adopt = titleblock('Adopting From Us')+f'''<main id="main"><section class="section">
<div class="grid-3"><div class="card soft"><h3>From Foster</h3><p>Many KKR cats live in foster homes around greater Phoenix. Approved applicants can coordinate a meet-and-greet with the foster.</p><a class="btn text" href="at-foster.html">See Foster Cats</a></div><div class="card soft"><h3>At PetSmart</h3><p>Up to about a dozen cats may be available at the North Scottsdale PetSmart Adoption Center for walk-in adoption.</p><a class="btn text" href="at-petsmart.html">See PetSmart Cats</a></div><div class="card soft"><h3>Adoption Events</h3><p>KKR holds special adoption events periodically throughout the year.</p><a class="btn text" href="events.html">See Events</a></div></div>
<div class="content-block"><h2>Adopting At PetSmart</h2><div class="steps"><div class="step"><div class="step-num">Step 1</div><h3>Visit</h3><p>Find a kitty listed at PetSmart and go to the Adoption Center to meet them. KKR does not hold or reserve cats based only on an online application, email or phone call.</p><a class="btn text" href="{LIVE}/atfoster-adoption-app" target="_blank" rel="noopener">Optional Online Application</a></div><div class="step"><div class="step-num">Step 2</div><h3>Meet &amp; Apply</h3><p>Meet the kitty and work with an Adoption Coordinator to complete an application if one is not already on file. The coordinator will discuss your background and fit.</p></div><div class="step"><div class="step-num">Step 3</div><h3>Complete Adoption</h3><p>If approved, pay the adoption fee and complete the adoption agreement at the Adoption Center.</p></div></div></div>
<div class="content-block"><h2>Adopting From Foster</h2><div class="steps"><div class="step"><div class="step-num">Step 1</div><h3>Apply</h3><p>Submit the online adoption application for a foster-based kitty. Application review may take 24–48 hours.</p><a class="btn text" href="{LIVE}/atfoster-adoption-app" target="_blank" rel="noopener">Adoption Application</a></div><div class="step"><div class="step-num">Step 2</div><h3>Meet</h3><p>If approved, KKR helps coordinate a time and place for you to meet the kitty and foster. Most fosters have work and family schedules, so flexibility helps.</p></div><div class="step"><div class="step-num">Step 3</div><h3>Adopt</h3><p>After the meeting, complete payment and the adoption agreement with the foster present.</p><a class="btn text" href="{LIVE}/adoption-agreement" target="_blank" rel="noopener">Adoption Agreement</a></div></div></div>
</section></main>'''
(ROOT/'adopt.html').write_text(page("Adopt From Us — Kneading Kitty's Rescue",'adopt',adopt),encoding='utf-8')

adopter = titleblock('New Kitty Adopter Resources')+f'''<main id="main"><section class="section narrow flush-top">
<div class="content-block"><h2>Have Questions Or Need Help?</h2><p>Recent adopters should receive an adoption packet along with available vaccination and spay/neuter documentation. If something is missing, contact KKR at <a href="mailto:info@kneadingkittysrescueaz.com">info@kneadingkittysrescueaz.com</a>.</p></div>
<div class="content-block"><h2>Post-Adoption Illness?</h2><p>Travel, a new home, new people, other animals, and changes in food or litter can all be stressful for a newly adopted cat. Mild short-term signs can occur during adjustment, but adopters should contact a veterinarian or KKR when they are concerned.</p><p>KKR may also be able to advise on common rescue-related issues through its medical team.</p></div>
<div class="content-block"><h2>Microchip Registry</h2><p>KKR typically transfers a new pet's microchip registration to the adopter several weeks after adoption. Keep KKR updated if your contact information changes before that transfer is completed.</p></div>
<div class="content-block"><h2>Veterinarian Information &amp; Documents</h2><p>The live KKR adopter-resources page contains the current veterinarian list and downloadable guidance on preparing your home, shy cats, introductions, clawing, litter box issues and other common questions.</p><div class="action-row"><a class="btn" href="{LIVE}/adopter-resources" target="_blank" rel="noopener">Open Full Adopter Resources</a></div></div>
</section></main>'''
(ROOT/'adopter-resources.html').write_text(page("Adopter Resources — Kneading Kitty's Rescue",'adopt',adopter),encoding='utf-8')

involved = titleblock('We Need Volunteers And Fosters')+f'''<main id="main"><section class="section">
<div class="grid-2"><div class="content-block"><h2>Adoption Center Volunteers</h2><p>KKR's PetSmart Adoption Center is open seven days a week and staffed by rescue volunteers. Shifts are generally two hours on a recurring weekly schedule, with a six-month commitment requested.</p><ul><li>Provide food, fresh water, clean litter and bedding.</li><li>Play with, pet and socialize the cats.</li><li>Help with meet-and-greets and adopter questions.</li><li>Support applications, adoption paperwork and fees.</li><li>Clean and restock the center.</li></ul><p>Volunteers must be at least 10; volunteers under 18 must be accompanied by a parent.</p><a class="btn" href="{LIVE}/volunteer-application-1" target="_blank" rel="noopener">Volunteer Application</a></div>
<div class="content-block"><h2>Fosters</h2><p>Foster families are essential to KKR. The rescue especially needs people comfortable raising litters, but adult-cat fosters are also important.</p><ul><li>Care for foster cats as part of your household.</li><li>Communicate with foster and medical coordinators.</li><li>Provide reliable transportation to clinics, events and the adoption center when needed.</li><li>Live within the greater Phoenix metro area.</li></ul><p>KKR provides mentoring, approved veterinary care, food and litter, and other supplies when donations or funding allow. West Valley wellness clinics are regularly held Thursday evenings, with a flexible East Valley schedule.</p><a class="btn" href="{LIVE}/foster-application" target="_blank" rel="noopener">Foster Application</a></div></div>
<div class="callout"><strong>Other ways to help:</strong> If you have a specific professional skill or service to offer, email <a href="mailto:info@kneadingkittysrescueaz.com">info@kneadingkittysrescueaz.com</a>.</div>
</section></main>'''
(ROOT/'involved.html').write_text(page("Get Involved — Kneading Kitty's Rescue",'involved',involved),encoding='utf-8')

intake = titleblock('Intake and Rescue')+f'''<main id="main"><section class="section narrow flush-top">
<div class="notice"><strong>Current Intake Notice</strong><br>KKR's foster homes are very full. New intake depends on foster availability, your ability to foster, Last Litter eligibility, or whether the cat is being returned after a prior KKR adoption.</div>
<div class="content-block"><h2>Adoption Returns</h2><p>KKR will accept a cat previously adopted from the rescue, but advance notice is needed to arrange foster placement. Please allow up to 48 hours for a response.</p><a class="btn" href="{LIVE}/return-request" target="_blank" rel="noopener">Adoption Return</a></div>
<div class="content-block"><h2>Last Litter Program</h2><p>For an unexpectedly pregnant cat or a recent unplanned litter, the owner may act as a temporary one-time foster until the kittens are old enough to separate. KKR then arranges spay/neuter, vaccines and microchips, returns the mother, and takes the kittens into the adoption program. The program is offered at no required cost to qualifying participants.</p><a class="btn" href="{LIVE}/last-litter" target="_blank" rel="noopener">Last Litter Program</a></div>
<div class="content-block"><h2>Rescue Request</h2><p>Stray or feral cat and kitten requests are reviewed based on foster capacity, location and urgency. KKR may assist directly or refer you to another resource.</p><a class="btn" href="{LIVE}/intake-request" target="_blank" rel="noopener">Rescue Request</a></div>
<div class="content-block"><h2>Rehoming Request</h2><p>People who need help rehoming a cat they or a family member own can submit a request for review. Response times may be up to 48 hours.</p><a class="btn" href="{LIVE}/rehome-request" target="_blank" rel="noopener">Rehoming Request</a></div>
<div class="grid-2"><div class="content-block"><h2>Other No-Kill Rescues</h2><div class="links"><a href="https://livingthedreamrescue.com" target="_blank" rel="noopener">Living The Dream</a><a href="https://www.savingonelife.org" target="_blank" rel="noopener">Saving One Life</a><a href="https://www.facebook.com" target="_blank" rel="noopener">Friends of Felines</a></div></div><div class="content-block"><h2>TNR &amp; Trapping</h2><div class="links"><a href="https://adlaz.org" target="_blank" rel="noopener">Animal Defense League of Arizona</a><a href="https://www.sassycatstnr.org" target="_blank" rel="noopener">Sassy Cats of Arizona</a><a href="https://www.thefoundationforhomelesscats.org" target="_blank" rel="noopener">The Foundation for Homeless Cats</a><a href="https://azhartt.org" target="_blank" rel="noopener">HARTT</a></div></div></div>
<div class="content-block"><h2>Animal Sanctuaries</h2><div class="links"><a href="https://www.whiskerssanctuary.com" target="_blank" rel="noopener">Whiskers N Wishes Sanctuary</a><a href="https://www.heartsthatpurr.org" target="_blank" rel="noopener">Hearts That Purr</a><a href="https://felinesanctuary.org" target="_blank" rel="noopener">Saint Francis Feline Sanctuary</a><a href="https://www.hermitagecatshelter.org" target="_blank" rel="noopener">Hermitage Cat Shelter &amp; Sanctuary</a></div></div>
</section></main>'''
(ROOT/'intake.html').write_text(page("Intake — Kneading Kitty's Rescue",'intake',intake),encoding='utf-8')

donate = titleblock('Donation Options')+f'''<main id="main"><section class="section">
<div class="image-copy"><div class="media"><img class="feature-image" src="{DONATE_IMG}" alt="Cat-themed donation image"></div><div class="copy content-block"><h2>Monetary</h2><p>KKR accepts major credit and debit cards and PayPal. One-time, recurring, on-behalf-of, memorial and adoption-fee options are available through the rescue's donation pages.</p><div class="action-row"><a class="btn" href="monetary-donations.html">Monetary Donations</a><a class="btn secondary" href="https://www.paypal.com/donate/?hosted_button_id=4DC5U9JJYAD4W" target="_blank" rel="noopener">Donate Now</a></div></div></div>
<div class="grid-2"><div class="content-block"><h2>PetSmart Wishlist</h2><p>KKR's PetSmart partnership supports rescue operations, and the foster program maintains a wishlist for food, litter and other supplies.</p><a class="btn" href="https://www.myregistry.com/organization/kneading-kitty-s-rescue-glendale-az/4733012/giftlist" target="_blank" rel="noopener">Open PetSmart Wishlist</a></div><div class="content-block"><h2>Amazon Wishlist</h2><p>KKR also maintains an Amazon wishlist for items needed by foster families.</p><a class="btn" href="{LIVE}/ways-to-donate" target="_blank" rel="noopener">Open Current Wishlist Link</a></div></div>
<div class="content-block"><h2>Pet Care Items &amp; Supplies</h2><p>Small clean beds, carriers and bowls may be accepted, along with new toys and litter supplies, food, and clearly labeled nonperishable medication. Large bedding, cat furniture, large crates and exercise pens should be coordinated by email because storage is limited.</p></div>
<div class="grid-3"><div class="card soft"><h3>Employer Giving</h3><p>If your employer participates in YourCause or another matching program, your gift may be matched.</p></div><div class="card soft"><h3>Corporate Donations</h3><p>Businesses interested in supporting KKR can contact the rescue to coordinate with the donation team.</p></div><div class="card soft"><h3>Qualified Charitable Distribution</h3><p>Eligible donors may be able to direct an IRA required minimum distribution to KKR. Consult your tax adviser about your situation.</p></div></div>
<div class="callout"><strong>Tax Status:</strong> Kneading Kitty's Rescue is an IRS-recognized 501(c)(3) nonprofit based in Glendale, Arizona. EIN 82-5069525.</div>
</section></main>'''
(ROOT/'donate.html').write_text(page("Ways To Donate — Kneading Kitty's Rescue",'donate',donate),encoding='utf-8')

money = titleblock('Monetary Donations')+f'''<main id="main"><section class="section"><div class="image-copy"><div class="media"><img class="feature-image" src="{MONEY_IMG}" alt="Close-up of a cat"></div><div class="copy content-block"><p>Use a major credit or debit card or PayPal to support Kneading Kitty's Rescue.</p><div class="links"><a href="https://www.paypal.com/donate/?hosted_button_id=4DC5U9JJYAD4W" target="_blank" rel="noopener">Donate Now — one-time or recurring</a><a href="{LIVE}/monetary-donations" target="_blank" rel="noopener">Donate On Behalf Of</a><a href="{LIVE}/monetary-donations" target="_blank" rel="noopener">Donate In Memory Of</a><a href="https://www.paypal.com/donate/?hosted_button_id=4DC5U9JJYAD4W" target="_blank" rel="noopener">Pay Adoption Fee</a></div></div></div><div class="callout"><strong>Thank you.</strong> Donations help KKR continue caring for kittens and cats throughout the greater Phoenix area.</div></section></main>'''
(ROOT/'monetary-donations.html').write_text(page("Monetary Donations — Kneading Kitty's Rescue",'donate',money),encoding='utf-8')

thanks = titleblock('A Special Thank You...')+f'''<main id="main"><section class="section"><div class="image-copy"><div class="media"><img class="feature-image" src="{THANKS_IMG}" alt="Thank-you message"></div><div class="copy content-block"><p>Kneading Kitty's Rescue is sustained by the people who foster, volunteer, donate and adopt. The rescue also depends on community organizations, veterinary partners and donors whose support helps KKR continue saving cats.</p><p>For the current list of featured partners and supporters, open KKR's live acknowledgements page.</p><a class="btn" href="{LIVE}/special-thanks" target="_blank" rel="noopener">See Special Thanks</a></div></div></section></main>'''
(ROOT/'special-thanks.html').write_text(page("Special Thanks — Kneading Kitty's Rescue",'donate',thanks),encoding='utf-8')

events = titleblock('Upcoming Adoption Events')+f'''<main id="main"><section class="section"><article class="event-card"><img src="{EVENT_IMG}" alt="Cat at an adoption event"><div class="event-copy"><div class="kicker">Upcoming</div><h2>Fall Adoption Event</h2><p><strong>Saturday October 24 &amp; Sunday October 25</strong><br>10:00 AM–5:00 PM</p><p>PetSmart<br>16257 N Scottsdale Rd<br>Scottsdale, Arizona 85260</p><p>Visit KKR on Facebook for the latest event details and updates.</p><div class="action-row"><a class="btn" href="https://www.facebook.com/kneadingkittysrescue" target="_blank" rel="noopener">KKR Facebook</a></div></div></article></section></main>'''
(ROOT/'events.html').write_text(page("Events — Kneading Kitty's Rescue",'events',events),encoding='utf-8')

readme=dedent(f'''\
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
''')
(ROOT/'README.md').write_text(readme,encoding='utf-8')

# Remove obsolete empty partial if present
try:
    (ROOT/'_header.html').unlink()
except FileNotFoundError:
    pass

print('Wrote', len(list(ROOT.glob('*.html'))), 'HTML pages')
