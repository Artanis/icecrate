% rebase("base.tpl", subtitle="Help")
<article>
  <h2>I can't scan anything</h2>
  <p><em>When I try to scan a barcode, the webpage is not available</em></p>
  <p>This web application requires a barcode scanning application supporting the <a href="https://code.google.com/p/zxing/wiki/ScanningFromWebPages">ZXing protocol for interacting with web pages</a>. Attempting to use one of these links without one of these apps installed will tell you the webpage is not available. This is because ZXing barcode apps listen for this kind of link, and launch automatically; without them, however, your browser tries to find a webpage, which doesn't exist.</p>
  <p><strong>To fix this</strong>, you will need to install a compatible barcode app. On Android, you can use the <a href="https://play.google.com/store/apps/details?id=com.google.zxing.client.android">ZXing Barcode Scanner</a>. On iPhone, use <a href="https://itunes.apple.com/us/app/barcodes-scanner/id417257150">Barcodes Scanner</a>.</p>
  <p>Once you've installed one of these apps, please <a class="zxing" href="?code={CODE}#success">use this link to test it</a>.</p>
  % if upc is not None:
  <p id="success">It looks like the test was a success. You scanned {{upc}}.</p>
  % end
</article>
