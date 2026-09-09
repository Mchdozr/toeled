# Toeled App Builder — QCE sertifika API

Statik sitedeki `/qce-cert-lookup/` PHP backend’e bağlıydı; bu klasör Adobe Runtime web action’ı olarak aynı sorgunun yerine geçer.

## Yerel test

```bash
cd app-builder
npm install
npm test
npm run lookup -- "Ahmet Yılmaz" QCE-2024-1001
```

Örnek kayıtlar: `Ahmet Yılmaz` / `QCE-2024-1001`, `Elif Kaya` / `QCE-2025-2210`, `Mehmet Demir` / `QCE-2023-0777`.

Deploy edilmeden sayfa aynı kataloğu `/app-builder/actions/qce-cert-lookup/certificates.json` üzerinden okur.

## Adobe’a yayınlama

```bash
aio login
aio console org select <orgId>
aio app use --no-input
aio app deploy
```

Çıkan web action URL’sini `qce-cert-lookup/index.html` içindeki `TOELED_CERT_LOOKUP_URL` değerine yaz.
