jest.mock('@adobe/aio-sdk', () => ({
  Core: {
    Logger: jest.fn().mockReturnValue({
      info: jest.fn(),
      warn: jest.fn(),
      error: jest.fn(),
      debug: jest.fn()
    })
  }
}))

const action = require('../../../actions/qce-cert-lookup/index.js')

describe('qce-cert-lookup', () => {
  beforeEach(() => {
    jest.clearAllMocks()
  })

  test('returns 200 with matching certificate', async () => {
    const result = await action.main({
      LOG_LEVEL: 'info',
      name: 'Ahmet Yılmaz',
      cNo: 'QCE-2024-1001'
    })

    expect(result.statusCode).toBe(200)
    expect(result.body).toBeDefined()
    expect(result.body.status).toBe(1)
    expect(result.body.data.cNo).toBe('QCE-2024-1001')
    expect(result.body.data.englishName).toBe('Ahmet Yılmaz')
    expect(result.headers['Access-Control-Allow-Origin']).toBe('*')
  })

  test('matches name case-insensitively', async () => {
    const result = await action.main({
      name: 'ahmet yılmaz',
      cNo: 'QCE-2024-1001'
    })

    expect(result.statusCode).toBe(200)
    expect(result.body.status).toBe(1)
  })

  test('returns 200 with not-found payload for unknown cert', async () => {
    const result = await action.main({
      name: 'Ahmet Yılmaz',
      cNo: 'MISSING-000'
    })

    expect(result.statusCode).toBe(200)
    expect(result.body.status).toBe(0)
    expect(result.body.msg).toBe('Sertifika bulunamadı')
  })

  test('returns 400 when required param is missing', async () => {
    const result = await action.main({ LOG_LEVEL: 'info' })

    expect(result.statusCode).toBe(400)
    expect(result.body).toBeDefined()
    expect(result.body.error).toBeDefined()
  })

  test('returns 204 for CORS preflight', async () => {
    const result = await action.main({ __ow_method: 'OPTIONS' })

    expect(result.statusCode).toBe(204)
    expect(result.body).toBeDefined()
  })

  test('returns 500 on unexpected catalog failure', async () => {
    const main = action.createMain(() => {
      throw new Error('catalog load failed')
    })

    const result = await main({
      LOG_LEVEL: 'info',
      name: 'Ahmet Yılmaz',
      cNo: 'QCE-2024-1001'
    })

    expect(result.statusCode).toBe(500)
    expect(result.body).toBeDefined()
    expect(result.body.error).toBe('catalog load failed')
  })
})
