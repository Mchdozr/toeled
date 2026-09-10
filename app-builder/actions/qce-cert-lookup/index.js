const { Core } = require('@adobe/aio-sdk')
const { stringParameters, checkMissingRequestInputs } = require('../utils')

const CORS_HEADERS = {
  'Content-Type': 'application/json',
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Allow-Methods': 'POST, OPTIONS'
}

function defaultLoadCertificates () {
  return require('./certificates.json')
}

function normalize (value) {
  return String(value || '').trim().toLocaleLowerCase('tr-TR')
}

function respond (statusCode, body) {
  return {
    statusCode,
    headers: CORS_HEADERS,
    body
  }
}

function createMain (loadCertificates = defaultLoadCertificates) {
  return async function main (params = {}) {
    const logger = Core.Logger('qce-cert-lookup', { level: params.LOG_LEVEL || 'info' })

    try {
      if (String(params.__ow_method || '').toLowerCase() === 'options') {
        return respond(204, {})
      }

      logger.info('Action invoked')
      logger.debug(stringParameters(params))

      const missing = checkMissingRequestInputs(params, ['name', 'cNo'])
      if (missing) {
        return respond(400, { status: 0, error: missing, msg: missing })
      }

      const certificates = loadCertificates()
      const name = normalize(params.name)
      const cNo = String(params.cNo).trim()
      const match = certificates.find((row) =>
        normalize(row.englishName) === name && String(row.cNo).trim() === cNo
      )

      if (!match) {
        logger.info('Certificate not found')
        return respond(200, { status: 0, msg: 'Sertifika bulunamadı' })
      }

      logger.info('Certificate found')
      return respond(200, { status: 1, data: match })
    } catch (error) {
      logger.error(error.message)
      return respond(500, { status: 0, error: error.message, msg: 'Sertifika sorgusu başarısız' })
    }
  }
}

exports.createMain = createMain
exports.main = createMain()
