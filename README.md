## Known Limitations (Stuff I Didn't Have Time For)
 
- **One route, one direction, no takebacks.** It's hardcoded to JNB → CPT, one-way only. Round trips would mean fighting a second calendar for the return date, and honestly, I'd only just made peace with the first one.
- **Zero error handling.** If literally one selector on lift.co.za so much as sneezes, the whole script face-plants. Totally fine for "run it once and grab the data." Absolutely not fine for leaving it running unattended and trusting it not to fall over.
- **Held together by vibes and CSS selectors.** This whole thing works because it's precisely tuned to lift.co.za's current HTML. The moment their dev team redesigns the date picker, this scraper dies instantly and without warning.
## Lessons Learned (Things That Broke Me)
 
- **The invisible overlay of doom.** Every single click timed out with some cryptic "intercepts pointer events" error. Turns out it was just a cookie banner, quietly sitting on top of the entire page like a bouncer nobody told me about. The error message doesn't say "hey, cookie popup." It just says "good luck." Clicking Accept first fixed everything.
- **DevTools has trust issues.** Collapsed elements show up as `⋯`, which looks a lot like "there's nothing here" — and is, in fact, lying. There's always something in there. Learned to expand everything before assuming it was empty.
- **Text ≠ text, apparently.** I tried matching a dropdown item by the airport code "JNB." Cute idea. Didn't work, because the dropdown shows full city names like "Johannesburg (OR Tambo)," not codes. Also, I was clicking the wrong element entirely — the actual text was hiding in a nested `<div>`, not the `<li>` I thought I was targeting. Two wrong assumptions, stacked on top of each other.
- **Headless mode is a great way to debug nothing.** Running invisibly is fast, sure, but it's also the equivalent of debugging with your eyes closed. Switching to `headless=False` with `slow_mo` was the only way to actually see what was blocking me instead of guessing.
