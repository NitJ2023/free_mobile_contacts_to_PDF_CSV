# iPhone VCF Contacts Select & Print — GitHub Pages

This is a static website. No contact data is built into the site or uploaded to a server. The visitor's selected VCF file is read locally in their browser.

## Publish with GitHub Pages

1. Create a **public** GitHub repository (e.g. `iphone-contact-printer`).
2. Upload everything in this folder, **including the hidden `.github/workflows/pages.yml` file**, preserving the folder structure. Upload the **contents** of this directory into the repository root (not the directory itself).
3. In repository **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**.
4. Ensure the default branch is `main`; pushing to main runs the publishing workflow. You can also start it under **Actions → Publish contact printer to GitHub Pages → Run workflow**.
5. Check **Settings → Pages** for the published website URL. The URL will usually be `https://YOURNAME.github.io/REPOSITORY/`.
6. The workflow automatically creates `sitemap.xml` and a canonical URL matching your GitHub Pages address. A root-level `robots.txt` is generated for user sites and custom-domain sites only. On project sites the crawler uses the host root `robots.txt`, which is not under the project's control.
7. Sign into [Google Search Console](https://search.google.com/search-console/about), verify your website, submit its `sitemap.xml` URL, then use **URL Inspection → Request Indexing** for the homepage.
8. Optional: add a GitHub Pages **custom domain** in Settings → Pages and create a `CNAME` file with just the domain name in the repository root. Make DNS changes as instructed by GitHub. Then the workflow will generate the canonical URL/sitemap for that domain.

Example sitemap URL: `https://YOURNAME.github.io/REPOSITORY/sitemap.xml`.

**Indexing cannot be guaranteed.** Search engines decide whether and when to crawl, index, and rank a page.

## Important privacy and publishing notes

- **Do not commit any actual `.vcf` contact exports to GitHub**. Only the tool's source files belong in this repository.
- The site CSP blocks network connections from the app itself, but GitHub Pages web server logs may still include visitor request metadata.
- The app supports VCF file selection, per-number selection, A4 printing, and CSV export.
- If a custom domain is used, validate its DNS and HTTPS via GitHub Pages settings.
