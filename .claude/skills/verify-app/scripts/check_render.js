// Render check for the Streamlit dashboard. Usage: node check_render.js [url]
// Read-only: opens the page, waits for metric cards, counts exceptions. No shell, no writes.
const { chromium } = require('playwright');

const url = process.argv[2] || 'http://localhost:8501';

(async () => {
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage();
    await page.goto(url);
    await page.waitForSelector('[data-testid="stMetric"]', { timeout: 30000 });
    const metrics = await page.locator('[data-testid="stMetric"]').count();
    const exceptions = await page.locator('[data-testid="stException"]').count();
    console.log(`metrics: ${metrics}, exceptions: ${exceptions}`);
    process.exitCode = exceptions > 0 ? 1 : 0;
  } catch (err) {
    console.error(`render check failed: ${err.message}`);
    process.exitCode = 1;
  } finally {
    await browser.close();
  }
})();
