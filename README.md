# Free iPhone Contacts to PDF & CSV

**A free, private, browser-based tool to select, organize, print, and export contacts from a VCF (vCard) file.** No account or installation required.

**[Open the free contact printer](https://nitj2023.github.io/free_mobile_contacts_to_PDF_CSV/)**

## What does it do?

Export contacts from your iPhone as a `.vcf` file, open this tool, and choose exactly which names and phone numbers to include. Create an A4 printable contact list (or save it as a PDF using your browser's Print dialog) or download selected contacts as a CSV file for Excel and other spreadsheet applications.

### Features

- Import `.vcf` / vCard contact exports from iPhone and other compatible sources.
- View contact names and associated phone numbers, including multiple numbers per person.
- Select or deselect **individual phone numbers** or all numbers for a contact.
- Select all, deselect all, or apply selection changes only to filtered search results.
- Search by contact name, phone number, or number label.
- Sort contacts alphabetically (A–Z or Z–A).
- Print a numbered, A4-friendly list or choose **Save as PDF** in your browser.
- Export selected names and numbers to a UTF-8 CSV file.
- Use the app entirely in your browser, including offline after saving the HTML file.

## How to use

1. **Export your contacts as a VCF file.** On supported iPhone versions, open **Contacts**, go to **Lists**, touch and hold the relevant list, then choose **Export**. The exact steps may vary by iOS version.
2. Visit **[Free iPhone Contacts to PDF & CSV](https://nitj2023.github.io/free_mobile_contacts_to_PDF_CSV/)**.
3. Click **Choose VCF File** and select your exported `.vcf` file.
4. Review the contacts. Tick or untick the individual numbers you want to include. You can also use search, sort, and bulk-selection buttons.
5. Choose **Print selected / Save PDF** to open the print dialog and print or save a PDF; or choose **Download selected CSV** to create a spreadsheet-friendly file.

**Important:** Unticking a number excludes it from the printout and CSV export. It does **not** delete that number from your iPhone or modify the original VCF file.

## Privacy

The contact file is processed locally in your browser. **The app does not upload your contact list to a server**, and it does not require registration. The application's content security policy blocks network connections initiated by its scripts. As with any website, the hosting service may still receive standard requests and associated metadata when you visit the page.

**Never commit or upload your own contact `.vcf` files to this public GitHub repository.**

## Supported formats and limitations

- Input: `.vcf` (vCard) files with names and telephone numbers.
- Output: printable A4 list / PDF through the browser print dialog, or `.csv` download.
- CSV is a text-based exchange format, not a native `.xlsx` workbook.
- Contacts without phone numbers are omitted from the selectable list.
- Some unusual or vendor-specific vCard exports may not be interpreted perfectly; review the selected list before printing.
- Files are loaded into browser memory for processing; very large contact collections may take longer on older devices.

## Run locally

This is a static HTML/JavaScript application. Download `index.html` and open it in a modern browser. No server, package manager, or build dependencies are needed for the contact-printing interface.

## Deploy to GitHub Pages

This repository contains a GitHub Actions Pages workflow and a `prepare_site.py` script used to prepare canonical metadata and a sitemap for deployment.

1. Fork this repository or upload its files to a public GitHub repository.
2. In **Settings → Pages → Build and deployment**, set **Source** to **GitHub Actions**.
3. Push changes to the default branch to trigger the workflow, or run the workflow manually if configured.
4. Visit the published Pages URL after deployment completes.

### Search engine discovery

The deployment workflow prepares canonical metadata and `sitemap.xml` for the published URL. You can submit the live sitemap to [Google Search Console](https://search.google.com/search-console/about) and request indexing for the homepage. Search engines independently decide whether and when to index and rank a page; indexing is not guaranteed.

**Sitemap (after a successful deployment):** [sitemap.xml](https://nitj2023.github.io/free_mobile_contacts_to_PDF_CSV/sitemap.xml)

## FAQ

**Does the tool change or delete my iPhone contacts?**  
No. All selections affect only the printout or CSV output.

**Can I print only one of several numbers for a person?**  
Yes. Each phone number can be selected independently.

**Can I save the result as PDF?**  
Yes. Choose **Print selected / Save PDF**, then select your browser's PDF printer or **Save as PDF** option.

**Does it work with Excel?**  
The CSV export can be opened in Excel and other spreadsheet apps.

**Do I need to sign in or upload my contacts?**  
No. The VCF file is read and processed locally on your device.

## Feedback and contributions

Have a bug report or improvement suggestion? [Open an issue](https://github.com/nitj2023/free_mobile_contacts_to_PDF_CSV/issues). Contributions are welcome through pull requests.

---

**Disclaimer:** Review your exported list before sharing or printing it. Contact information may be personal data; handle it appropriately and obtain permission where required.
