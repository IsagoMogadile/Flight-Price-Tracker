## Known Limitations

- **One-way only, single route.** Hardcoded to JNB → CPT. Round-trip support would mean handling a second calendar for the return date — a problem for future me.
- **No error handling.** If a selector breaks, the whole script crashes instead of failing gracefully. Fine for a one-off scrape, not fine for anything running unattended.
- **Fragile by nature.** This works because it depends on lift.co.za's exact HTML structure staying the same. If they redesign their date picker, this breaks. That's just the tax you pay for not having an API.

## Lessons Learned (a.k.a. Things That Broke Me)

- **The invisible overlay of doom.** Every click kept timing out with `<div id="overlay"> intercepts pointer events` — turns out it was a cookie consent banner sitting silently on top of the entire page. Nothing in the error message says "cookie banner," it just says "good luck." Fixed by clicking Accept before touching anything else.
- **DevTools lies by omission.** Collapsed elements show as `⋯` in the inspector, which looks like there's nothing there. There's always something there. Had to manually expand elements more than once to find what I actually needed.
- **Text ≠ text.** Tried matching a dropdown item by airport code (`JNB`) — except the dropdown displays full city names ("Johannesburg (OR Tambo)"), not codes. The element also wasn't even the one I was targeting; the clickable text lived in a nested `<div>`, not the `<li>` I was clicking on. Two separate wrong assumptions stacked on top of each other.
- **Headless mode debugs nothing.** Running invisibly is great for speed, terrible for figuring out *why* something's failing. Switching to `headless=False` with `slow_mo` and taking screenshots mid-run was the only way to actually see what was blocking me.
- **Silent failures are the worst failures.** At one point the script ran with zero output and zero errors — because it never actually called the function it defined. No crash, no clue, just silence.