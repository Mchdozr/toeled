(function (window) {
  var FALLBACK_CATALOG = '/app-builder/actions/qce-cert-lookup/certificates.json';

  function normalize (value) {
    return String(value || '').trim().toLocaleLowerCase('tr-TR');
  }

  function lookupInCatalog (certificates, name, cNo) {
    var match = (certificates || []).find(function (row) {
      return normalize(row.englishName) === normalize(name) && String(row.cNo).trim() === String(cNo).trim();
    });
    if (match) {
      return { status: 1, data: match };
    }
    return { status: 0, msg: 'Sertifika bulunamadı' };
  }

  function lookup (name, cNo) {
    var url = window.TOELED_CERT_LOOKUP_URL;
    if (url) {
      return fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name, cNo: cNo })
      }).then(function (res) {
        return res.json();
      });
    }

    return fetch(FALLBACK_CATALOG, { cache: 'no-store' })
      .then(function (res) {
        if (!res.ok) {
          throw new Error('Katalog yüklenemedi');
        }
        return res.json();
      })
      .then(function (certificates) {
        return lookupInCatalog(certificates, name, cNo);
      });
  }

  window.ToeledCertLookup = { lookup: lookup };
})(window);
