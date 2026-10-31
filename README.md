# iPhone Contact Printer

A small Windows desktop utility for opening an iPhone `.vcf` (vCard) contacts export, listing names and phone numbers, and printing the list.

## Run on Windows

1. Unzip the project folder if you downloaded the ZIP.
2. Double-click **Run Contact Printer.bat**.
3. Choose the `.vcf` file, review the contacts, then click **Print...**. Use the print-preview window to print on paper or choose **Microsoft Print to PDF**.

The app uses Windows PowerShell and Windows Forms already included with Windows 10/11. It does not require Python, an installer, an account, or an internet connection. The `.bat` launcher starts PowerShell in a separate STA window mode needed for the desktop interface.

## Privacy

The selected file is read locally on your PC. The app does not upload, transmit, or save contact data. Closing the app clears the list from the app window; use **Clear list** to remove it sooner.

## Files

- `ContactPrinter.ps1` — the application source.
- `Run Contact Printer.bat` — double-click launcher.

A compiled `.exe` is not included. This version runs directly with built-in Windows PowerShell, so it needs no separate runtime installation. The source is provided for review or modification.
