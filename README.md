# Toeled

Natro Plesk + GitHub push ile canlıya alınan site.

## Plesk Git (push → canlı)

1. Plesk → **Git** → **Add Repository**
2. Remote: `https://github.com/Mchdozr/toeled.git`
3. Branch: `main`
4. Deployment path: `httpdocs` (document root)
5. **Enable additional deployment actions** gerekmez; repo kökü doğrudan site dosyalarıdır.
6. Push sonrası Plesk otomatik çeksin diye **Auto deployment** açık olsun.

Private repo ise Plesk’e GitHub deploy key veya HTTPS kullanıcı/token ekle.

## Yerel

```bash
git add -A
git commit -m "mesaj"
git push origin main
```
