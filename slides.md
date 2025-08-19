---
marp: true
# Presentation metadata
title: "AcmeApp: Product Documentation Overview"
author: "Technical Writer"
theme: acme-dark
paginate: true
footer: "Page $page / $total — 23f1001207@ds.study.iitm.ac.in"
math: katex
size: 16:9
---

<style>
/* ------------------------------
   Custom Marp Theme: acme-dark
   Save together with the deck for VC-friendly portability
   ------------------------------ */
@theme acme-dark {
  /* Typography */
  --header-font: ui-sans-serif, Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;
  --body-font: ui-sans-serif, Inter, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial;

  /* Palette */
  --bg: #0b1020;           /* deep space */
  --fg: #e6edf3;           /* soft foreground */
  --muted: #9aa4b2;        /* secondary text */
  --accent: #6ee7b7;       /* mint accent */
  --accent-2: #93c5fd;     /* blue accent */

  /* Base */
  section {
    background: var(--bg);
    color: var(--fg);
    font-family: var(--body-font);
    letter-spacing: 0.1px;
  }
  h1, h2, h3 {
    font-family: var(--header-font);
    color: var(--accent);
    line-height: 1.1;
  }
  a { color: var(--accent-2); }
  code { background: rgba(255,255,255,0.04); padding: 0.15em 0.35em; border-radius: 6px; }
  pre code { background: rgba(255,255,255,0.06); border-radius: 10px; padding: 0.9em 1em; display: block; }
  blockquote { color: var(--muted); border-left: 0.22em solid var(--accent); padding-left: 0.8em; }
  footer { color: var(--muted); }
}

/* Utility slide classes */
section.lead h1 { font-size: 2.4em; }
section.compact ul { font-size: 0.95em; }
</style>

<!-- _class: lead -->
# AcmeApp — Product Documentation Overview

**Technical Writer**  
23f1001207@ds.study.iitm.ac.in

> A concise, version-controlled documentation deck built with **Marp**.

---

<!-- 
  Background image slide. To keep this repo-friendly,
  store your image at assets/hero.jpg
  The overlay is readable thanks to the theme colors.
-->
![bg opacity:0.15](assets/hero.jpg)

# Why Marp for Docs?

- Plain **Markdown** ➜ superb for version control & diffs
- Same source ➜ export **HTML / PDF / PPTX** via Marp CLI
- **Custom themes**, **math**, and **directives** for polish

---

## Project Structure (suggested)

```text
.
├─ slides.md               # This file
├─ assets/
│  ├─ hero.jpg             # Background image used above
│  └─ logo.svg             # Optional logo
├─ package.json            # Scripts for conversion (optional)
└─ README.md               # How to build
```

---

## Build & Export (CLI)

```bash
# Install once
npm i -D @marp-team/marp-cli

# Export to HTML
npx marp slides.md --html --theme-set ./slides.md

# Export to PDF (needs Chrome/Chromium)
npx marp slides.md --pdf --allow-local-files --theme-set ./slides.md

# Export to PPTX
npx marp slides.md --pptx --theme-set ./slides.md
```

> Tip: `--theme-set ./slides.md` lets Marp discover the in-file custom theme.

---

## Document Conventions

- **Headings** map to sections; one slide per H1/HR boundary
- **Notes**: Use HTML comments for speaker-only guidance
- **Directives**: Configure per-slide behavior inline
  - Example: `<!-- _class: compact -->` to tighten layout

---

<!-- _class: compact -->
## Key Directives Used

- `theme: acme-dark` — custom theme declared in this file
- `paginate: true` — page numbers are enabled
- `footer: "Page $page / $total — 23f1001207@ds.study.iitm.ac.in"`
- `math: katex` — enables LaTeX-style equations
- `![bg](...)` — background images per slide
- `<!-- _class: ... -->` — apply utility class styling

---

## Algorithmic Complexity (Math example)

For a balanced divide-and-conquer routine (like mergesort):

$$
T(n) = 2\,T\!\left(\frac{n}{2}\right) + \Theta(n)
$$

By the Master Theorem:

$$
T(n) = \Theta(n\,\log n)
$$

Inline math: \(O(n^2)\), \(\Omega(\log n)\), \(\Theta(n)\).

---

## API Surface (Snippet)

```ts
/** Create a user */
export async function createUser(input: CreateUserDto): Promise<User> {
  // Validate
  if (!input.email) throw new Error("email required");
  // Persist
  return db.user.create({ data: input });
}
```

---

## Version Control Tips

- Keep **one source file** per deck (like `slides.md`)
- Co-locate assets in `assets/` with short, semantic names
- Use **small, reviewable commits** (content vs. theme vs. assets)
- Add `marp` build scripts to CI (export HTML/PDF as artifacts)

---

## Credits & Contact

- Theme & deck authored by **Technical Writer**
- Contact: **23f1001207@ds.study.iitm.ac.in**
- Built with **Marp**

Thanks!
