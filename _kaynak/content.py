# DreamVision sitesi metinleri (EN + TR). Değiştirince: python3 _kaynak/build.py
#
# Olgular uygulamayla tutarlı tutulmalı (dreamvision_flutter + DreamMapper/functions):
# tek seferlik kredi paketleri (abonelik yok), krediler süresiz, başarısız üretimde
# otomatik iade, prompt sunucuda Gemini (Vertex AI), görsel/video fal.ai, satın alma
# profili Adapty, IP yalnızca özet (hash) olarak 2 gün, ses telefonun tanıma
# servisinde işlenir. Play Console → Veri güvenliği formu da bunlarla uyumlu olmalı.

MAIL = "supportdreamvisionapp@gmail.com"
PLAY_REFUND_EN = "https://support.google.com/googleplay/answer/2479637?hl=en"
PLAY_REFUND_TR = "https://support.google.com/googleplay/answer/2479637?hl=tr"
PLAY_ORDERS = "https://play.google.com/store/account/orderhistory"

UI = {
    "en": {
        "skip": "Skip to content",
        "nav_label": "Pages",
        "footer_label": "Site links",
        "lang_label": "Language",
        "nav": {"support": "Support", "privacy": "Privacy", "terms": "Terms", "delete": "Delete Account"},
    },
    "tr": {
        "skip": "İçeriğe geç",
        "nav_label": "Sayfalar",
        "footer_label": "Site bağlantıları",
        "lang_label": "Dil",
        "nav": {"support": "Destek", "privacy": "Gizlilik", "terms": "Koşullar", "delete": "Hesap Silme"},
    },
}

# ────────────────────────────────────────────────────────────── DESTEK

SUPPORT_EN = f"""
<section class="card contact">
  <h2>Contact Support</h2>
  <p>Requests are typically answered within <strong>48 hours</strong>.</p>
  <a class="btn" href="mailto:{MAIL}">{MAIL}</a>
  <p class="muted">Emails sent via <strong>Settings → Help &amp; Support</strong> in the app include your app version automatically. To help us resolve your request promptly, please state your device model and the action during which the issue occurred.</p>
</section>

<h2 class="eyebrow" style="display:block;margin:28px 0 12px">Frequently Asked Questions</h2>

<details>
  <summary>A creation failed. Will my credits be refunded?</summary>
  <div>
    <p>Yes. If an image or video cannot be created, the credits used are <strong>refunded automatically</strong>, usually within a few minutes. If your credits are still missing after an hour, please contact us with the date and time of the attempt.</p>
  </div>
</details>

<details>
  <summary>Does the app have a subscription?</summary>
  <div>
    <p>No. DreamVision uses <strong>one-time credit packs</strong> purchased through Google Play. There is no automatic renewal, and credits do not expire.</p>
  </div>
</details>

<details>
  <summary>My purchased credits are not showing in my account</summary>
  <div>
    <ol>
      <li>Close the app completely and reopen it.</li>
      <li>Open the credits screen and tap <strong>Restore Purchases</strong>.</li>
      <li>Make sure you are signed in with the same DreamVision account and the same Google account used for the purchase.</li>
    </ol>
    <p>If the issue persists, please send us your Google Play order number. It begins with <code>GPA.</code> and can be found in your <a href="{PLAY_ORDERS}">Google Play order history</a> or in the purchase receipt email.</p>
  </div>
</details>

<details>
  <summary>Can I request a refund for a purchase?</summary>
  <div>
    <p>Payments are processed by Google Play. Within <strong>48 hours</strong> of purchase, you can submit a refund request directly to Google Play: <a href="{PLAY_REFUND_EN}">Google Play refund help</a>.</p>
    <p>After this period, or if the issue was caused by our service, please contact us with your order number and we will review your request.</p>
  </div>
</details>

<details>
  <summary>How do I redeem a promo code?</summary>
  <div>
    <p>Go to <strong>Settings → Promo Code</strong>, enter the code and tap <strong>Apply</strong>. Promotional credits are added to your account immediately.</p>
    <p>Promo codes require a registered account and cannot be used in guest mode. Each code may be redeemed once per account, and codes are not case-sensitive.</p>
  </div>
</details>

<details>
  <summary>What is the difference between guest mode and a registered account?</summary>
  <div>
    <p>With a free account (email or Google), you can save your dreams to your gallery, access them from other devices and redeem promo codes. To create an account, go to <strong>Settings → Create Account</strong>.</p>
  </div>
</details>

<details>
  <summary>Voice input does not convert my speech to text</summary>
  <div>
    <ul>
      <li>Make sure microphone access is granted to DreamVision in your device settings.</li>
      <li>Voice input uses your device's speech recognition service. Please ensure the <strong>Google</strong> app is installed and up to date.</li>
      <li>If the issue persists, you can enter your dream as text.</li>
    </ul>
  </div>
</details>

<details>
  <summary>The generated image does not reflect my dream</summary>
  <div>
    <p>AI produces the best results from detailed descriptions covering the setting, people, colors, lighting and atmosphere. Brief or general descriptions provide the model with insufficient information. We recommend describing a single scene in detail or generating the image again.</p>
  </div>
</details>

<details>
  <summary>I received a notice that my content was filtered</summary>
  <div>
    <p>DreamVision uses automated safety filters to prevent the creation of sexually explicit, violent or harmful images. If your description triggers a filter, you may try describing the dream in a more symbolic or indirect way. Filter decisions are automated and cannot be overridden manually.</p>
  </div>
</details>

<details>
  <summary>How can I report an inappropriate image or video?</summary>
  <div>
    <p>Tap the <strong>flag icon</strong> at the top of the result screen or the dream detail screen, select a reason and submit the report. All reports are reviewed, and content that violates our rules is removed.</p>
  </div>
</details>

<details>
  <summary>How can I delete my account?</summary>
  <div>
    <p>You can delete your account in the app via <strong>Settings → Delete Account</strong>. The data that is deleted and retained is described in detail on the <a href="delete-account.html">Delete Account</a> page.</p>
  </div>
</details>

<h2 class="eyebrow" style="display:block;margin:28px 0 12px">Quick Links</h2>
<div class="grid">
  <a class="tile" href="{PLAY_REFUND_EN}"><strong>Google Play Refunds</strong>Purchase refund requests.</a>
  <a class="tile" href="privacy-policy.html"><strong>Privacy Policy</strong>Principles of personal data processing.</a>
  <a class="tile" href="terms-conditions.html"><strong>Terms of Use</strong>Terms governing use of the service.</a>
  <a class="tile" href="delete-account.html"><strong>Delete Account</strong>Deletion of account and data.</a>
</div>
"""

SUPPORT_TR = f"""
<section class="card contact">
  <h2>Destek Ekibiyle İletişim</h2>
  <p>Talepler genellikle <strong>48 saat</strong> içinde yanıtlanır.</p>
  <a class="btn" href="mailto:{MAIL}">{MAIL}</a>
  <p class="muted">Uygulama içindeki <strong>Ayarlar → Yardım ve Destek</strong> menüsü üzerinden gönderilen e-postalara uygulama sürümü otomatik olarak eklenir. Talebinizin hızla sonuçlandırılabilmesi için cihaz modelinizi ve sorunun ortaya çıktığı işlemi belirtmenizi rica ederiz.</p>
</section>

<h2 class="eyebrow" style="display:block;margin:28px 0 12px">Sıkça Sorulan Sorular</h2>

<details>
  <summary>Oluşturma işlemi başarısız oldu. Kredilerim iade edilir mi?</summary>
  <div>
    <p>Evet. Oluşturulamayan görsel veya videolar için kullanılan krediler <strong>otomatik olarak iade edilir</strong>; iade genellikle birkaç dakika içinde tamamlanır. Bir saat sonra krediler hesabınıza yansımamışsa işlemin tarih ve saatiyle birlikte bizimle iletişime geçiniz.</p>
  </div>
</details>

<details>
  <summary>Uygulamada abonelik var mı?</summary>
  <div>
    <p>Hayır. DreamVision, Google Play üzerinden satın alınan <strong>tek seferlik kredi paketleriyle</strong> çalışır. Otomatik yenileme yapılmaz ve kredilerin kullanım süresi yoktur.</p>
  </div>
</details>

<details>
  <summary>Satın aldığım krediler hesabıma yansımadı</summary>
  <div>
    <ol>
      <li>Uygulamayı tamamen kapatıp yeniden açınız.</li>
      <li>Kredi ekranını açarak <strong>Satın Almaları Geri Yükle</strong> seçeneğine dokununuz.</li>
      <li>Satın alma sırasında kullandığınız DreamVision hesabı ve Google hesabıyla giriş yaptığınızdan emin olunuz.</li>
    </ol>
    <p>Sorun devam ederse Google Play sipariş numaranızı (<code>GPA.</code> ile başlar; <a href="{PLAY_ORDERS}">Google Play sipariş geçmişinizde</a> veya satın alma makbuzu e-postasında yer alır) bize iletiniz.</p>
  </div>
</details>

<details>
  <summary>Satın alımım için iade talep edebilir miyim?</summary>
  <div>
    <p>Ödemeler Google Play tarafından işlenmektedir. Satın alma tarihinden itibaren <strong>48 saat</strong> içinde iade talebinizi doğrudan Google Play'e iletebilirsiniz: <a href="{PLAY_REFUND_TR}">Google Play iade yardım sayfası</a>.</p>
    <p>Bu süre dolduysa veya sorun hizmetimizden kaynaklandıysa, sipariş numaranızla birlikte bize başvurmanız hâlinde talebiniz incelenecektir.</p>
  </div>
</details>

<details>
  <summary>Promosyon kodu nasıl kullanılır?</summary>
  <div>
    <p><strong>Ayarlar → Promosyon Kodu</strong> menüsünden kodu giriniz ve <strong>Uygula</strong> seçeneğine dokununuz. Promosyon kredileri hesabınıza anında tanımlanır.</p>
    <p>Promosyon kodları yalnızca kayıtlı hesaplarla kullanılabilir, misafir modunda geçerli değildir. Her kod hesap başına bir kez kullanılabilir; büyük-küçük harf ayrımı yapılmaz.</p>
  </div>
</details>

<details>
  <summary>Misafir kullanımı ile kayıtlı hesap arasındaki fark nedir?</summary>
  <div>
    <p>Ücretsiz bir hesapla (e-posta veya Google) rüyalarınızı galerinize kaydedebilir, farklı cihazlardan erişebilir ve promosyon kodlarını kullanabilirsiniz. Hesap oluşturmak için <strong>Ayarlar → Hesap Oluştur</strong> menüsünü kullanınız.</p>
  </div>
</details>

<details>
  <summary>Sesli anlatım metne dönüşmüyor</summary>
  <div>
    <ul>
      <li>Cihaz ayarlarından DreamVision uygulamasına mikrofon izni verildiğini kontrol ediniz.</li>
      <li>Sesli anlatım, cihazınızın ses tanıma hizmetini kullanır. <strong>Google</strong> uygulamasının yüklü ve güncel olduğundan emin olunuz.</li>
      <li>Sorunun devam etmesi hâlinde rüyanızı metin olarak girebilirsiniz.</li>
    </ul>
  </div>
</details>

<details>
  <summary>Oluşturulan görsel rüyamı yansıtmıyor</summary>
  <div>
    <p>Yapay zekâ; mekân, kişiler, renkler, ışık ve atmosfer gibi ayrıntılar içeren anlatımlarda en iyi sonucu verir. Kısa ve genel anlatımlar modele yeterli bilgi sağlamaz. Tek bir sahneyi ayrıntılı olarak tarif etmenizi veya görseli yeniden oluşturmanızı öneririz.</p>
  </div>
</details>

<details>
  <summary>İçeriğimin filtrelendiğine dair bir uyarı aldım</summary>
  <div>
    <p>DreamVision, cinsel içerikli, şiddet içeren veya zararlı görsellerin oluşturulmasını önlemek amacıyla otomatik güvenlik filtreleri kullanır. Anlatımınızın bir filtreye takılması hâlinde rüyanızı daha sembolik veya dolaylı bir şekilde ifade edebilirsiniz. Filtre kararları otomatik olarak verilir ve manuel olarak değiştirilemez.</p>
  </div>
</details>

<details>
  <summary>Uygunsuz bir görseli veya videoyu nasıl bildirebilirim?</summary>
  <div>
    <p>Sonuç ekranının veya rüya ayrıntı ekranının üst kısmındaki <strong>bayrak simgesine</strong> dokunarak bir neden seçiniz ve bildirimi gönderiniz. Tüm bildirimler incelenir; kurallarımıza aykırı içerikler kaldırılır.</p>
  </div>
</details>

<details>
  <summary>Hesabımı nasıl silebilirim?</summary>
  <div>
    <p>Uygulama içinden <strong>Ayarlar → Hesabı Sil</strong> menüsünü kullanabilirsiniz. Silinen ve saklanan veriler <a href="delete-account-tr.html">Hesap Silme</a> sayfasında ayrıntılı olarak açıklanmıştır.</p>
  </div>
</details>

<h2 class="eyebrow" style="display:block;margin:28px 0 12px">Hızlı Erişim</h2>
<div class="grid">
  <a class="tile" href="{PLAY_REFUND_TR}"><strong>Google Play İadeleri</strong>Satın alma iadesi talebi.</a>
  <a class="tile" href="privacy-policy-tr.html"><strong>Gizlilik Politikası</strong>Kişisel verilerin işlenmesine ilişkin esaslar.</a>
  <a class="tile" href="terms-conditions-tr.html"><strong>Kullanım Koşulları</strong>Hizmetin kullanımına ilişkin şartlar.</a>
  <a class="tile" href="delete-account-tr.html"><strong>Hesap Silme</strong>Hesap ve verilerin silinmesi.</a>
</div>
"""

# ────────────────────────────────────────────────────────────── GİZLİLİK

PRIVACY_EN = f"""
<section class="card summary">
  <h2>Summary</h2>
  <ul>
    <li>Your dream descriptions are processed solely to create your images and videos.</li>
    <li>The app does not display advertising, and your personal data is never sold.</li>
    <li>Voice input is converted to text on the device; audio recordings are never transmitted to us.</li>
    <li>You may delete your account and data at any time from within the app.</li>
  </ul>
</section>

<ul class="toc">
  <li><a href="#who">Data Controller</a></li><li><a href="#collect">Information Collected</a></li>
  <li><a href="#use">Purposes of Use</a></li><li><a href="#ai">AI Processing</a></li>
  <li><a href="#share">Service Providers</a></li><li><a href="#keep">Retention</a></li>
  <li><a href="#rights">Your Rights</a></li><li><a href="#children">Minors' Privacy</a></li>
</ul>

<section class="card" id="who">
  <h2>Data Controller</h2>
  <p>DreamVision is developed by <strong>Sabri ÇETİN</strong>, who is the data controller for your personal data. Contact: <a href="mailto:{MAIL}">{MAIL}</a>.</p>
</section>

<section class="card" id="collect">
  <h2>Information Collected</h2>
  <h3>Account Information</h3>
  <ul>
    <li>If you create an account: your email address, display name and a user identifier. If you sign in with Google, your name and email address are shared with us by Google.</li>
    <li>In guest mode, only an anonymous user identifier is created.</li>
  </ul>
  <h3>Dream Content</h3>
  <ul>
    <li>The dream text you type or dictate, the options you select (mood, time of day, point of view, style) and the images and videos created from them.</li>
    <li>Dreams saved to your gallery and those marked as favorites.</li>
  </ul>
  <h3>Voice Data</h3>
  <ul>
    <li>During voice input, your device's speech recognition service (typically Google) converts your speech to text. Only the resulting text is transmitted to us; audio is never received or stored.</li>
  </ul>
  <h3>Credits and Purchases</h3>
  <ul>
    <li>Your credit balance and transaction history (credits added, used and refunded).</li>
    <li>Purchase details: product, order number and date. Payments are processed by Google Play; we have no access to your card details.</li>
    <li>Promo codes you redeem.</li>
  </ul>
  <h3>App Usage and Device Information</h3>
  <ul>
    <li>In-app interactions, such as screens viewed and features used (Google Analytics for Firebase).</li>
    <li>Crash reports including device model, Android version and app version (Firebase Crashlytics).</li>
    <li>A notification token and language preference, if you enable notifications.</li>
  </ul>
  <h3>Security and Abuse Prevention</h3>
  <ul>
    <li>An irreversible hash of your IP address, retained for 2 days to prevent repeated claiming of free credits. The IP address itself is not stored.</li>
    <li>Content reports you submit: the reason, your optional note and a link to the reported image or video.</li>
  </ul>
  <p>We do not collect your location, contacts or the photos stored on your device. When you save a creation to your device, it is only written to your gallery.</p>
</section>

<section class="card" id="use">
  <h2>Purposes of Use</h2>
  <ul>
    <li>To create, display and save your images and videos.</li>
    <li>To manage your account, credits and purchases, and to verify purchases through Google Play.</li>
    <li>To send notifications you have requested, such as when your video is ready.</li>
    <li>To prevent abuse and fraud, and to review content reports.</li>
    <li>To resolve errors and improve the app.</li>
    <li>To respond to support requests and comply with legal obligations.</li>
  </ul>
  <p>The app does not display advertising, your personal data is never sold, and we do not send marketing emails.</p>
</section>

<section class="card" id="ai">
  <h2>AI Processing</h2>
  <p>To create an image or video, your dream text and selected options are sent to <strong>Google Gemini</strong> (via Google Cloud Vertex AI) to prepare an English prompt. The prompt is then sent to <strong>fal.ai</strong>, which generates the image or video. These providers process data solely for the purpose of providing this service. Your name and email address are never shared with them.</p>
  <p>Automated safety filters may block descriptions or results that are sexually explicit, violent or harmful. AI-generated results may be unexpected; any inappropriate content can be reported from within the app.</p>
</section>

<section class="card" id="share">
  <h2>Service Providers</h2>
  <p>Data is shared only with the following providers involved in delivering the DreamVision service:</p>
  <table class="table">
    <thead><tr><th>Provider</th><th>Purpose</th></tr></thead>
    <tbody>
      <tr><td><a href="https://firebase.google.com/support/privacy">Google Firebase</a></td><td>Authentication, database, file storage, server functions, notifications, analytics and crash reporting</td></tr>
      <tr><td><a href="https://cloud.google.com/terms/cloud-privacy-notice">Google Cloud Vertex AI</a></td><td>Converting dream descriptions into prompts with Gemini</td></tr>
      <tr><td><a href="https://fal.ai/privacy">fal.ai</a></td><td>Image and video generation</td></tr>
      <tr><td><a href="https://adapty.io/privacy">Adapty</a></td><td>Credit packs and purchase records</td></tr>
      <tr><td><a href="https://policies.google.com/privacy">Google Play</a></td><td>Payments and purchase verification</td></tr>
    </tbody>
  </table>
  <p>Information may also be disclosed where required by law or to protect the rights and safety of our users and others. Your data may be processed on servers located outside your country, including in the European Union and the United States.</p>
</section>

<section class="card" id="keep">
  <h2>Retention</h2>
  <p>Your account information and dreams are retained until you delete them or your account. Certain records are retained longer for legal and security reasons. Video progress records are deleted after 7 days, IP hashes after 2 days and crash reports after 90 days. Full details are available on the <a href="delete-account.html">Delete Account</a> page.</p>
</section>

<section class="card" id="rights">
  <h2>Your Rights</h2>
  <p>Depending on the legislation applicable to you (such as the EU General Data Protection Regulation or Turkey's Personal Data Protection Law No. 6698), you have the right to access, rectify, erase or obtain a copy of your personal data, and to object to its processing. You may delete your account at any time via <strong>Settings → Delete Account</strong>. Other requests may be submitted to <a href="mailto:{MAIL}">{MAIL}</a> and will be answered within 30 days.</p>
</section>

<section class="card" id="children">
  <h2>Minors' Privacy</h2>
  <p>DreamVision is intended for users aged 18 and over. It is not directed at minors, and we do not knowingly collect personal data from anyone under 18. If you believe a minor has provided us with information, please contact us and the data will be deleted.</p>
</section>

<section class="card">
  <h2>Data Security</h2>
  <p>Data is transmitted over encrypted connections. Access to data is restricted by security rules, and credit transactions are processed exclusively on our servers.</p>
</section>

<section class="card">
  <h2>Changes to This Policy</h2>
  <p>This policy may be updated as the app evolves. Updates are reflected in the date at the top of this page, and material changes are also announced within the app.</p>
</section>
"""

PRIVACY_TR = f"""
<section class="card summary">
  <h2>Özet</h2>
  <ul>
    <li>Rüya metinleri yalnızca görsel ve video oluşturmak amacıyla işlenir.</li>
    <li>Uygulamada reklam gösterilmez ve kişisel verileriniz satılmaz.</li>
    <li>Sesli anlatım cihazda metne dönüştürülür; ses kayıtları tarafımıza iletilmez.</li>
    <li>Hesabınızı ve verilerinizi dilediğiniz zaman uygulama üzerinden silebilirsiniz.</li>
  </ul>
</section>

<ul class="toc">
  <li><a href="#who">Veri Sorumlusu</a></li><li><a href="#collect">Toplanan Bilgiler</a></li>
  <li><a href="#use">Kullanım Amaçları</a></li><li><a href="#ai">Yapay Zekâ</a></li>
  <li><a href="#share">Hizmet Sağlayıcılar</a></li><li><a href="#keep">Saklama Süreleri</a></li>
  <li><a href="#rights">Haklarınız</a></li><li><a href="#children">Reşit Olmayanlar</a></li>
</ul>

<section class="card" id="who">
  <h2>Veri Sorumlusu</h2>
  <p>DreamVision, <strong>Sabri ÇETİN</strong> tarafından geliştirilmektedir. Kişisel verileriniz bakımından veri sorumlusu Sabri ÇETİN'dir. İletişim: <a href="mailto:{MAIL}">{MAIL}</a>.</p>
</section>

<section class="card" id="collect">
  <h2>Toplanan Bilgiler</h2>
  <h3>Hesap Bilgileri</h3>
  <ul>
    <li>Kayıtlı hesaplarda e-posta adresi, görünen ad ve kullanıcı kimliği. Google ile girişte ad ve e-posta adresi Google tarafından iletilir.</li>
    <li>Misafir modunda yalnızca anonim bir kullanıcı kimliği oluşturulur.</li>
  </ul>
  <h3>Rüya İçerikleri</h3>
  <ul>
    <li>Yazılı veya sesli olarak girilen rüya metni, seçilen ayarlar (ruh hâli, zaman, bakış açısı, stil) ve oluşturulan görsel ile videolar.</li>
    <li>Galeriye kaydedilen ve favori olarak işaretlenen rüyalar.</li>
  </ul>
  <h3>Ses Verisi</h3>
  <ul>
    <li>Sesli anlatım, cihazın ses tanıma hizmeti (genellikle Google) tarafından metne dönüştürülür. Tarafımıza yalnızca metin iletilir; ses kaydı alınmaz ve saklanmaz.</li>
  </ul>
  <h3>Krediler ve Satın Almalar</h3>
  <ul>
    <li>Kredi bakiyesi ve işlem geçmişi (eklenen, kullanılan ve iade edilen krediler).</li>
    <li>Satın alma bilgileri: ürün, sipariş numarası ve tarih. Ödemeler Google Play tarafından işlenir; kart bilgilerine erişimimiz yoktur.</li>
    <li>Kullanılan promosyon kodları.</li>
  </ul>
  <h3>Uygulama Kullanımı ve Cihaz Bilgileri</h3>
  <ul>
    <li>Açılan ekranlar ve kullanılan özellikler gibi uygulama içi etkileşimler (Google Analytics for Firebase).</li>
    <li>Cihaz modeli, Android sürümü ve uygulama sürümünü içeren hata raporları (Firebase Crashlytics).</li>
    <li>Bildirimlere izin verilmesi hâlinde bildirim anahtarı ve dil tercihi.</li>
  </ul>
  <h3>Güvenlik ve Kötüye Kullanımın Önlenmesi</h3>
  <ul>
    <li>IP adresinin geri döndürülemez özeti (hash): ücretsiz kredilerin mükerrer alınmasını önlemek amacıyla 2 gün saklanır. IP adresinin kendisi saklanmaz.</li>
    <li>İçerik bildirimleri: bildirim nedeni, isteğe bağlı açıklama ve bildirilen içeriğin bağlantısı.</li>
  </ul>
  <p>Konum, rehber ve cihazdaki fotoğraflar toplanmaz. Cihaza kaydedilen içerikler yalnızca galeriye yazılır.</p>
</section>

<section class="card" id="use">
  <h2>Kullanım Amaçları</h2>
  <ul>
    <li>Görsel ve videoların oluşturulması, görüntülenmesi ve kaydedilmesi.</li>
    <li>Hesap, kredi ve satın alma işlemlerinin yönetilmesi; satın almaların Google Play aracılığıyla doğrulanması.</li>
    <li>Talep edilen bildirimlerin (örneğin videonun hazır olduğuna dair bildirim) gönderilmesi.</li>
    <li>Kötüye kullanımın ve dolandırıcılığın önlenmesi, içerik bildirimlerinin incelenmesi.</li>
    <li>Hataların giderilmesi ve uygulamanın geliştirilmesi.</li>
    <li>Destek taleplerinin yanıtlanması ve yasal yükümlülüklerin yerine getirilmesi.</li>
  </ul>
  <p>Uygulamada reklam gösterilmez, kişisel verileriniz satılmaz ve pazarlama amaçlı e-posta gönderilmez.</p>
</section>

<section class="card" id="ai">
  <h2>Yapay Zekâ ile İşleme</h2>
  <p>Rüya metni ve seçilen ayarlar, İngilizce bir istem (prompt) hazırlanması amacıyla Google Cloud Vertex AI üzerinden <strong>Google Gemini</strong>'ye iletilir. Hazırlanan istem, görsel veya videoyu oluşturan <strong>fal.ai</strong>'a gönderilir. Bu sağlayıcılar verileri yalnızca hizmetin sunulması amacıyla işler; ad ve e-posta adresi bu sağlayıcılarla paylaşılmaz.</p>
  <p>Otomatik güvenlik filtreleri cinsel içerikli, şiddet içeren veya zararlı anlatımları ve sonuçları engelleyebilir. Uygunsuz bulunan içerikler uygulama üzerinden bildirilebilir.</p>
</section>

<section class="card" id="share">
  <h2>Hizmet Sağlayıcılar</h2>
  <p>Veriler yalnızca hizmetin sunulmasında görev alan aşağıdaki sağlayıcılarla paylaşılır:</p>
  <table class="table">
    <thead><tr><th>Sağlayıcı</th><th>Amaç</th></tr></thead>
    <tbody>
      <tr><td><a href="https://firebase.google.com/support/privacy">Google Firebase</a></td><td>Kimlik doğrulama, veritabanı, dosya depolama, sunucu işlevleri, bildirimler, analiz ve hata raporlama</td></tr>
      <tr><td><a href="https://cloud.google.com/terms/cloud-privacy-notice">Google Cloud Vertex AI</a></td><td>Gemini ile rüya anlatımının isteme dönüştürülmesi</td></tr>
      <tr><td><a href="https://fal.ai/privacy">fal.ai</a></td><td>Görsel ve video oluşturma</td></tr>
      <tr><td><a href="https://adapty.io/privacy">Adapty</a></td><td>Kredi paketleri ve satın alma kayıtları</td></tr>
      <tr><td><a href="https://policies.google.com/privacy">Google Play</a></td><td>Ödeme işlemleri ve satın alma doğrulaması</td></tr>
    </tbody>
  </table>
  <p>Yasal zorunluluk hâlinde veya kullanıcıların ve üçüncü kişilerin hak ve güvenliğinin korunması amacıyla bilgiler yetkili mercilerle paylaşılabilir. Veriler, Avrupa Birliği ve Amerika Birleşik Devletleri dahil olmak üzere yurt dışındaki sunucularda işlenebilir.</p>
</section>

<section class="card" id="keep">
  <h2>Saklama Süreleri</h2>
  <p>Hesap bilgileri ve rüyalar, kullanıcı tarafından silinene kadar saklanır. Bazı kayıtlar yasal yükümlülükler ve güvenlik gerekçeleriyle daha uzun süre muhafaza edilir. Video ilerleme kayıtları 7 gün, IP özetleri 2 gün, hata raporları 90 gün sonra silinir. Ayrıntılar <a href="delete-account-tr.html">Hesap Silme</a> sayfasında yer almaktadır.</p>
</section>

<section class="card" id="rights">
  <h2>Haklarınız</h2>
  <p>Tâbi olduğunuz mevzuat (6698 sayılı Kişisel Verilerin Korunması Kanunu veya Avrupa Birliği Genel Veri Koruma Tüzüğü) kapsamında kişisel verilerinize erişme, bunların düzeltilmesini, silinmesini veya aktarılmasını talep etme ve işlenmesine itiraz etme haklarına sahipsiniz. Hesabınızı <strong>Ayarlar → Hesabı Sil</strong> menüsünden dilediğiniz zaman silebilirsiniz. Diğer talepler <a href="mailto:{MAIL}">{MAIL}</a> adresine iletilebilir ve en geç 30 gün içinde yanıtlanır.</p>
</section>

<section class="card" id="children">
  <h2>Reşit Olmayanların Gizliliği</h2>
  <p>DreamVision 18 yaş ve üzeri kullanıcılara yöneliktir. 18 yaşından küçüklere ait veriler bilerek toplanmaz. Böyle bir durumun tespiti hâlinde bizimle iletişime geçiniz; ilgili veriler silinir.</p>
</section>

<section class="card">
  <h2>Veri Güvenliği</h2>
  <p>Veriler şifreli bağlantılar üzerinden iletilir, erişim güvenlik kurallarıyla sınırlandırılır ve kredi işlemleri yalnızca sunucu tarafında gerçekleştirilir.</p>
</section>

<section class="card">
  <h2>Politika Değişiklikleri</h2>
  <p>Bu politika gerektiğinde güncellenebilir. Güncelleme tarihi sayfanın üst kısmında belirtilir; önemli değişiklikler ayrıca uygulama içinde duyurulur.</p>
</section>
"""

# ────────────────────────────────────────────────────────────── KOŞULLAR

TERMS_EN = f"""
<section class="card">
  <p>These Terms of Use govern the use of the <strong>DreamVision</strong> app developed by <strong>Sabri ÇETİN</strong> ("we"). By using the app, you agree to these terms. The principles of personal data processing are set out in the <a href="privacy-policy.html">Privacy Policy</a>.</p>
</section>

<section class="card">
  <h2>1. Scope of the Service</h2>
  <p>DreamVision converts the dreams users describe into images and videos using artificial intelligence. Features may change over time, and certain features (such as video creation) may be temporarily unavailable.</p>
</section>

<section class="card">
  <h2>2. User Accounts</h2>
  <ul>
    <li>The app may be used as a guest or with a free account (email or Google).</li>
    <li>You must be at least 18 years of age to use DreamVision.</li>
    <li>You are responsible for maintaining the security of your account and device.</li>
  </ul>
</section>

<section class="card">
  <h2>3. Credits and Purchases</h2>
  <ul>
    <li>Creating an image or video requires credits. The number of credits required is displayed before each creation.</li>
    <li>Credits are offered as <strong>one-time purchases</strong> through Google Play. There are no subscriptions or automatic renewals.</li>
    <li>Credits do not expire, have no cash value, are non-transferable and are forfeited upon account deletion.</li>
    <li>Credits used for a failed creation are refunded automatically.</li>
    <li>Refunds of purchases are subject to Google Play's refund policy. For issues caused by our service, please contact us.</li>
    <li>Prices and credit costs may change; current prices are always displayed in the app before any purchase or creation.</li>
  </ul>
</section>

<section class="card">
  <h2>4. Starter Credits and Promo Codes</h2>
  <ul>
    <li>Starter credits and promo codes may be modified or discontinued without prior notice.</li>
    <li>Promo codes require a registered account, may be redeemed once per account, may be subject to an expiry date or usage limit, and have no cash value.</li>
    <li>Credits obtained through abuse (for example, by creating multiple fraudulent accounts) may be revoked.</li>
  </ul>
</section>

<section class="card">
  <h2>5. Acceptable Use</h2>
  <p>DreamVision may not be used to create, request or share content that:</p>
  <ul>
    <li>is sexually explicit, or sexualizes minors in any way;</li>
    <li>promotes violence, hatred, harassment or discrimination;</li>
    <li>impersonates a real person in a misleading manner, or discloses another person's private information;</li>
    <li>infringes the rights of others, such as copyrights or trademarks;</li>
    <li>is otherwise unlawful.</li>
  </ul>
  <p>Attempting to circumvent safety filters or usage limits, misusing the service with automated tools, or interfering with its operation is also prohibited. Content violating these rules may be removed, and the associated accounts may be suspended or terminated.</p>
</section>

<section class="card">
  <h2>6. AI-Generated Content</h2>
  <ul>
    <li>Images and videos are generated by AI and may be unexpected, inaccurate or different from what you envisioned.</li>
    <li>Automated safety filters may block certain descriptions or results.</li>
    <li>Inappropriate content can be reported using the flag icon in the app. Reports are reviewed, and content that violates these terms is removed.</li>
  </ul>
</section>

<section class="card">
  <h2>7. User Content</h2>
  <p>You retain the rights to your dream texts. You may use and share the images and videos you create in accordance with these terms and applicable law. You grant us permission to store and process your content solely for the purpose of providing the service to you (for example, to create, display and save it).</p>
</section>

<section class="card">
  <h2>8. Intellectual Property</h2>
  <p>All rights to the app, its design, the DreamVision name and the Dream Cloud character are owned by us. Copying, modifying, reverse-engineering or reselling the app is prohibited.</p>
</section>

<section class="card">
  <h2>9. Third-Party Services</h2>
  <p>DreamVision relies on services such as Google Firebase, Google Cloud, Google Play, fal.ai and Adapty, each governed by its own terms. These services are listed in the <a href="privacy-policy.html#share">Privacy Policy</a>.</p>
</section>

<section class="card">
  <h2>10. Availability and Limitation of Liability</h2>
  <ul>
    <li>Most features require an internet connection. Any mobile data charges from your carrier are your responsibility.</li>
    <li>While we make every reasonable effort to keep DreamVision running smoothly, we do not guarantee that the service will always be available or error-free. The app is provided "as is".</li>
    <li>To the extent permitted by law, we accept no liability for indirect losses arising from the use of the app.</li>
  </ul>
</section>

<section class="card">
  <h2>11. Updates and Discontinuation</h2>
  <p>Updates may be released, and some may be required to continue using the app. The app may be discontinued; in that case, users will be notified in advance wherever possible.</p>
</section>

<section class="card">
  <h2>12. Changes to These Terms</h2>
  <p>These terms may be updated. Updates are reflected in the date at the top of this page, and material changes are also announced within the app. Continued use of the app constitutes acceptance of the updated terms.</p>
</section>

<section class="card contact">
  <h2>Contact</h2>
  <p>For questions regarding these Terms of Use:</p>
  <a class="btn" href="mailto:{MAIL}">{MAIL}</a>
</section>
"""

TERMS_TR = f"""
<section class="card">
  <p>Bu Kullanım Koşulları, <strong>Sabri ÇETİN</strong> ("biz") tarafından geliştirilen <strong>DreamVision</strong> uygulamasının kullanım şartlarını belirler. Uygulamayı kullanarak bu koşulları kabul etmiş sayılırsınız. Kişisel verilerin işlenmesine ilişkin esaslar <a href="privacy-policy-tr.html">Gizlilik Politikası</a>'nda yer almaktadır.</p>
</section>

<section class="card">
  <h2>1. Hizmetin Kapsamı</h2>
  <p>DreamVision, kullanıcıların anlattığı rüyaları yapay zekâ ile görsel ve videoya dönüştürür. Özellikler zaman içinde değişebilir; bazı özellikler (örneğin video oluşturma) geçici olarak kullanıma kapatılabilir.</p>
</section>

<section class="card">
  <h2>2. Kullanıcı Hesabı</h2>
  <ul>
    <li>Uygulama misafir olarak veya ücretsiz bir hesapla (e-posta ya da Google) kullanılabilir.</li>
    <li>DreamVision'ı kullanabilmek için en az 18 yaşında olmanız gerekir.</li>
    <li>Hesap ve cihaz güvenliğinin sağlanması kullanıcının sorumluluğundadır.</li>
  </ul>
</section>

<section class="card">
  <h2>3. Krediler ve Satın Almalar</h2>
  <ul>
    <li>Görsel ve video oluşturma işlemleri kredi gerektirir; gerekli kredi miktarı işlem öncesinde gösterilir.</li>
    <li>Krediler Google Play üzerinden <strong>tek seferlik satın alma</strong> yoluyla sunulur. Abonelik veya otomatik yenileme bulunmamaktadır.</li>
    <li>Kredilerin kullanım süresi yoktur; nakit değeri taşımaz, başka bir hesaba devredilemez ve hesabın silinmesi hâlinde geçerliliğini yitirir.</li>
    <li>Başarısız olan oluşturma işlemlerinde kullanılan krediler otomatik olarak iade edilir.</li>
    <li>Satın alma iadeleri Google Play iade politikasına tâbidir. Hizmetten kaynaklanan sorunlar için bizimle iletişime geçebilirsiniz.</li>
    <li>Fiyatlar ve kredi maliyetleri değişebilir; güncel bilgiler işlem öncesinde uygulamada gösterilir.</li>
  </ul>
</section>

<section class="card">
  <h2>4. Başlangıç Kredileri ve Promosyon Kodları</h2>
  <ul>
    <li>Başlangıç kredileri ve promosyon kodları, önceden bildirim yapılmaksızın değiştirilebilir veya sona erdirilebilir.</li>
    <li>Promosyon kodları yalnızca kayıtlı hesaplarla ve hesap başına bir kez kullanılabilir; son kullanma tarihine veya kullanım sınırına tâbi olabilir ve nakit değeri taşımaz.</li>
    <li>Kötüye kullanım yoluyla (örneğin çok sayıda sahte hesap oluşturularak) elde edilen krediler geri alınabilir.</li>
  </ul>
</section>

<section class="card">
  <h2>5. Kullanım Kuralları</h2>
  <p>DreamVision aşağıdaki nitelikteki içeriklerin oluşturulması, talep edilmesi veya paylaşılması amacıyla kullanılamaz:</p>
  <ul>
    <li>cinsel içerikli olan veya çocukları herhangi bir şekilde cinselleştiren içerikler;</li>
    <li>şiddeti, nefreti, tacizi veya ayrımcılığı teşvik eden içerikler;</li>
    <li>gerçek bir kişiyi yanıltıcı biçimde taklit eden veya üçüncü kişilerin özel bilgilerini içeren içerikler;</li>
    <li>telif hakkı veya marka gibi üçüncü kişilerin haklarını ihlal eden içerikler;</li>
    <li>yürürlükteki mevzuata aykırı diğer tüm içerikler.</li>
  </ul>
  <p>Güvenlik filtrelerinin veya kullanım sınırlarının aşılmaya çalışılması, hizmetin otomatik araçlarla kötüye kullanılması ve işleyişine müdahale edilmesi de yasaktır. Bu kurallara aykırı içerikler kaldırılabilir; ilgili hesaplar askıya alınabilir veya kapatılabilir.</p>
</section>

<section class="card">
  <h2>6. Yapay Zekâ ile Oluşturulan İçerikler</h2>
  <ul>
    <li>Görsel ve videolar yapay zekâ tarafından oluşturulur; sonuçlar beklenenden farklı veya hatalı olabilir.</li>
    <li>Otomatik güvenlik filtreleri bazı anlatımları veya sonuçları engelleyebilir.</li>
    <li>Uygunsuz içerikler uygulamadaki bayrak simgesiyle bildirilebilir. Bildirimler incelenir; bu koşullara aykırı içerikler kaldırılır.</li>
  </ul>
</section>

<section class="card">
  <h2>7. Kullanıcı İçeriği</h2>
  <p>Rüya metinlerine ilişkin haklar kullanıcıya aittir. Oluşturulan görsel ve videolar bu koşullara ve yürürlükteki mevzuata uygun olarak kullanılabilir ve paylaşılabilir. Kullanıcı, içeriklerinin yalnızca hizmetin sunulması amacıyla (oluşturma, görüntüleme ve kaydetme) saklanmasına ve işlenmesine izin vermiş sayılır.</p>
</section>

<section class="card">
  <h2>8. Fikri Mülkiyet Hakları</h2>
  <p>Uygulama, tasarımı, DreamVision adı ve Rüya Bulutu karakteri üzerindeki tüm haklar tarafımıza aittir. Uygulamanın kopyalanması, değiştirilmesi, tersine mühendislik işlemine tâbi tutulması veya yeniden satılması yasaktır.</p>
</section>

<section class="card">
  <h2>9. Üçüncü Taraf Hizmetler</h2>
  <p>DreamVision; Google Firebase, Google Cloud, Google Play, fal.ai ve Adapty gibi kendi kullanım koşullarına sahip hizmetlerden yararlanır. Söz konusu hizmetler <a href="privacy-policy-tr.html#share">Gizlilik Politikası</a>'nda listelenmiştir.</p>
</section>

<section class="card">
  <h2>10. Hizmetin Sürekliliği ve Sorumluluğun Sınırlandırılması</h2>
  <ul>
    <li>Özelliklerin büyük bölümü internet bağlantısı gerektirir; mobil veri ücretleri kullanıcıya aittir.</li>
    <li>Hizmetin kesintisiz sunulması için gerekli özen gösterilmekle birlikte, her zaman erişilebilir veya hatasız olacağı garanti edilmez. Uygulama "olduğu gibi" sunulmaktadır.</li>
    <li>Yürürlükteki mevzuatın izin verdiği ölçüde, uygulamanın kullanımından doğabilecek dolaylı zararlardan sorumluluk kabul edilmez.</li>
  </ul>
</section>

<section class="card">
  <h2>11. Güncellemeler ve Hizmetin Sona Ermesi</h2>
  <p>Uygulamaya güncellemeler yayımlanabilir; bazı güncellemelerin yüklenmesi kullanıma devam edilebilmesi için zorunlu olabilir. Hizmetin sona erdirilmesi hâlinde mümkün olduğunca önceden bilgilendirme yapılır.</p>
</section>

<section class="card">
  <h2>12. Koşullarda Yapılacak Değişiklikler</h2>
  <p>Bu koşullar gerektiğinde güncellenebilir. Güncelleme tarihi sayfanın üst kısmında belirtilir; önemli değişiklikler ayrıca uygulama içinde duyurulur. Uygulamanın kullanımına devam edilmesi, güncel koşulların kabulü anlamına gelir.</p>
</section>

<section class="card contact">
  <h2>İletişim</h2>
  <p>Kullanım Koşulları hakkındaki sorularınız için:</p>
  <a class="btn" href="mailto:{MAIL}">{MAIL}</a>
</section>
"""

# ────────────────────────────────────────────────────────────── HESAP SİLME

DELETE_EN = f"""
<section class="card">
  <p>App: <strong>DreamVision</strong> · Developer: <strong>Sabri ÇETİN</strong></p>
</section>

<section class="card">
  <h2>Deleting Your Account in the App</h2>
  <ol>
    <li>Open DreamVision and sign in.</li>
    <li>Go to <strong>Settings</strong>.</li>
    <li>Tap <strong>Delete Account</strong> and confirm.</li>
  </ol>
  <p>Your account and data are deleted immediately, as described below.</p>
</section>

<section class="card">
  <h2>Requesting Deletion by Email</h2>
  <p>If the app is no longer installed on your device, please send an email to <a href="mailto:{MAIL}?subject=Delete%20my%20DreamVision%20account">{MAIL}</a> <strong>from the email address of your account</strong> with the subject “Delete my DreamVision account”. We will delete your account within <strong>30 days</strong> and confirm by email.</p>
  <p>In guest mode, dreams are not saved; the only record is an anonymous credit balance that is not associated with your identity.</p>
</section>

<section class="card">
  <h2>Data That Is Deleted</h2>
  <ul>
    <li>Your account (email address, display name, sign-in)</li>
    <li>All your dream images and videos, and the dream texts you wrote</li>
    <li>Your credit balance and transaction history</li>
    <li>Your purchase profile at our payment provider (Adapty) — automatically</li>
    <li>Device keys used to send you notifications</li>
  </ul>
  <p>Any remaining credits are forfeited upon account deletion and cannot be refunded or restored.</p>
</section>

<section class="card">
  <h2>Data That Is Retained, and Retention Periods</h2>
  <ul>
    <li><strong>Purchase records</strong> (order number, product, number of credits, date and your user ID): kept as long as required for tax and accounting obligations, refunds and fraud prevention.</li>
    <li><strong>Abuse-prevention record</strong> (whether starter credits were granted and how many free creations were used, without any content): kept so that free credits cannot be claimed repeatedly.</li>
    <li><strong>Promo code records</strong> (which codes your account used): retained to prevent a code from being redeemed more than once.</li>
    <li><strong>Video creation records</strong> (temporary records used to show progress while a video is being made; they include the dream text sent for the video): deleted automatically <strong>7 days</strong> after creation. Your saved videos are not affected.</li>
    <li><strong>Crash reports</strong> (Firebase Crashlytics): deleted automatically by Google after 90 days.</li>
  </ul>
</section>

<section class="card contact">
  <h2>Contact</h2>
  <p>For questions regarding your data:</p>
  <a class="btn" href="mailto:{MAIL}">{MAIL}</a>
</section>
"""

DELETE_TR = f"""
<section class="card">
  <p>Uygulama: <strong>DreamVision</strong> · Geliştirici: <strong>Sabri ÇETİN</strong></p>
</section>

<section class="card">
  <h2>Uygulama Üzerinden Silme</h2>
  <ol>
    <li>DreamVision uygulamasını açarak giriş yapınız.</li>
    <li><strong>Ayarlar</strong> menüsüne gidiniz.</li>
    <li><strong>Hesabı Sil</strong> seçeneğine dokunarak işlemi onaylayınız.</li>
  </ol>
  <p>Hesabınız ve verileriniz aşağıda belirtildiği şekilde derhâl silinir.</p>
</section>

<section class="card">
  <h2>E-posta ile Silme Talebi</h2>
  <p>Uygulamanın cihazınızda yüklü olmaması hâlinde, <strong>hesabınıza kayıtlı e-posta adresinden</strong> “DreamVision hesabımı sil” konulu bir e-postayı <a href="mailto:{MAIL}?subject=DreamVision%20hesab%C4%B1m%C4%B1%20sil">{MAIL}</a> adresine gönderebilirsiniz. Hesabınız en geç <strong>30 gün</strong> içinde silinir ve işlem e-posta ile teyit edilir.</p>
  <p>Misafir olarak kullanımda rüyalar kaydedilmez; yalnızca kimliğinizle ilişkilendirilmemiş anonim bir kredi bakiyesi kaydı bulunur.</p>
</section>

<section class="card">
  <h2>Silinen Veriler</h2>
  <ul>
    <li>Hesap bilgileriniz (e-posta adresi, görünen ad, giriş bilgileri)</li>
    <li>Tüm rüya görselleriniz ve videolarınız ile rüya metinleriniz</li>
    <li>Kredi bakiyeniz ve işlem geçmişiniz</li>
    <li>Ödeme altyapımızdaki (Adapty) satın alma profiliniz (otomatik olarak)</li>
    <li>Bildirim gönderimi için kullanılan cihaz anahtarlarınız</li>
  </ul>
  <p>Hesap silindiğinde kalan krediler geçerliliğini yitirir; iade edilmez ve geri yüklenemez.</p>
</section>

<section class="card">
  <h2>Saklanan Veriler ve Saklama Süreleri</h2>
  <ul>
    <li><strong>Satın alma kayıtları</strong> (sipariş numarası, ürün, kredi miktarı, tarih ve kullanıcı kimliği): vergi ve muhasebe yükümlülükleri, iade işlemleri ve dolandırıcılığın önlenmesi için gerekli süre boyunca saklanır.</li>
    <li><strong>Kötüye kullanımı önleme kaydı</strong> (başlangıç kredisinin tanımlanıp tanımlanmadığı ve kullanılan ücretsiz oluşturma sayısı; içerik barındırmaz): ücretsiz kredilerin mükerrer alınmasını önlemek amacıyla saklanır.</li>
    <li><strong>Promosyon kodu kayıtları</strong> (hesabınızın kullandığı kodlar): bir kodun birden fazla kez kullanılmasını önlemek amacıyla saklanır.</li>
    <li><strong>Video oluşturma kayıtları</strong> (ilerleme durumunu göstermek için tutulan ve rüya metnini içeren geçici kayıtlar): oluşturulduktan <strong>7 gün</strong> sonra otomatik olarak silinir. Kaydedilen videolar bundan etkilenmez.</li>
    <li><strong>Hata raporları</strong> (Firebase Crashlytics): Google tarafından 90 gün sonra otomatik olarak silinir.</li>
  </ul>
</section>

<section class="card contact">
  <h2>İletişim</h2>
  <p>Verilerinize ilişkin sorularınız için:</p>
  <a class="btn" href="mailto:{MAIL}">{MAIL}</a>
</section>
"""

UPDATED_EN = "Last updated: November 7, 2026"
UPDATED_TR = "Son güncelleme: 7 Kasım 2026"

PAGES = {
    "support": {
        "en": {"title": "Support", "eyebrow": "Support", "h1": "How can we help?",
               "lead": "Answers to frequently asked questions and direct contact with the DreamVision support team.",
               "description": "DreamVision support: credits, purchases, refunds, promo codes and account help.",
               "body": SUPPORT_EN},
        "tr": {"title": "Destek", "eyebrow": "Destek", "h1": "Size nasıl yardımcı olabiliriz?",
               "lead": "Sıkça sorulan soruların yanıtları ve DreamVision destek ekibiyle doğrudan iletişim.",
               "description": "DreamVision destek: krediler, satın almalar, iadeler, promosyon kodları ve hesap yardımı.",
               "body": SUPPORT_TR},
    },
    "privacy": {
        "en": {"title": "Privacy Policy", "eyebrow": "Privacy", "h1": "Privacy Policy",
               "lead": "How DreamVision collects, uses and protects your personal data.",
               "description": "How the DreamVision Android app collects, uses and protects your data.",
               "updated": UPDATED_EN, "body": PRIVACY_EN},
        "tr": {"title": "Gizlilik Politikası", "eyebrow": "Gizlilik", "h1": "Gizlilik Politikası",
               "lead": "DreamVision'ın kişisel verilerinizi nasıl topladığı, kullandığı ve koruduğu.",
               "description": "DreamVision Android uygulamasının kişisel verileri nasıl topladığı, kullandığı ve koruduğu.",
               "updated": UPDATED_TR, "body": PRIVACY_TR},
    },
    "terms": {
        "en": {"title": "Terms of Use", "eyebrow": "Terms", "h1": "Terms of Use",
               "lead": "The terms governing the use of DreamVision, its credits and the content you create.",
               "description": "Terms of use for the DreamVision Android app: credits, purchases and content rules.",
               "updated": UPDATED_EN, "body": TERMS_EN},
        "tr": {"title": "Kullanım Koşulları", "eyebrow": "Koşullar", "h1": "Kullanım Koşulları",
               "lead": "DreamVision'ın, kredilerin ve oluşturduğunuz içeriklerin kullanımına ilişkin koşullar.",
               "description": "DreamVision Android uygulamasının kullanım koşulları: krediler, satın almalar ve içerik kuralları.",
               "updated": UPDATED_TR, "body": TERMS_TR},
    },
    "delete": {
        "en": {"title": "Delete Account", "eyebrow": "Account & Data", "h1": "Account Deletion",
               "lead": "How to delete your DreamVision account and what happens to your data.",
               "description": "How to delete your DreamVision account and data, what is deleted and what is kept.",
               "updated": UPDATED_EN, "body": DELETE_EN},
        "tr": {"title": "Hesap Silme", "eyebrow": "Hesap ve Veriler", "h1": "Hesap Silme",
               "lead": "DreamVision hesabınızı nasıl silebileceğiniz ve verilerinize ne olacağı.",
               "description": "DreamVision hesabınızı ve verilerinizi nasıl silebileceğiniz; silinen ve saklanan veriler.",
               "updated": UPDATED_TR, "body": DELETE_TR},
    },
}
