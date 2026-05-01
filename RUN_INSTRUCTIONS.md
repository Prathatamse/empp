# How to Run the Website-Export Project locally

Since your project is a static site (HTML/CSS/JS) exported from Framer, you should use a local web server to run it. Opening `index.html` directly in the browser by double-clicking it might cause issues with loading assets or forms.

Here are the three easiest ways to run your project locally:

## Method 1: Using VS Code (Easiest if you use VS Code)

1. Open the `e:\New folder\website-export` folder in Visual Studio Code.
2. Go to the Extensions tab (`Ctrl+Shift+X` or `Cmd+Shift+X`) and install the **Live Server** extension (by Ritwick Dey).
3. Once installed, right-click on the `index.html` file in the file explorer and select **"Open with Live Server"**.
4. Your default browser will open automatically, showing your site (usually at `http://127.0.0.1:5500`).

## Method 2: Using Python (If you have Python installed)

If you already have Python installed on your computer, you can use its built-in server.

1. Open your Terminal or Command Prompt.
2. Navigate to your project folder:
   ```cmd
   cd "e:\New folder\website-export"
   ```
3. Start the Python HTTP server:
   ```cmd
   python -m http.server 8000
   ```
4. Open your web browser and go to `http://localhost:8000`

## Method 3: Using Node.js (If you have Node/npm installed)

If you have Node.js installed on your computer, you can use the `serve` package.

1. Open your Terminal or Command Prompt.
2. Navigate to your project folder:
   ```cmd
   cd "e:\New folder\website-export"
   ```
3. Run the following command (press `y` if prompted to install the package):
   ```cmd
   npx serve
   ```
4. Open your web browser and go to the URL shown in the terminal (usually `http://localhost:3000`).

---

### Important Notes
- **Internet Connection Required**: This specific export uses hotlinked assets (images, fonts, styles) from the original Framer CDN. You must be connected to the internet for the site to load correctly.
- **Form Submissions**: If your contact form is not working, make sure the `action` attribute in the `<form>` tag is pointing to a valid form handling backend (like Formspree or your own API endpoint).
