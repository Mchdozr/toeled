const { main } = require('../actions/qce-cert-lookup')

async function run () {
  const name = process.argv[2] || 'Ahmet Yılmaz'
  const cNo = process.argv[3] || 'QCE-2024-1001'
  const result = await main({ name, cNo, LOG_LEVEL: 'info' })
  process.stdout.write(`${JSON.stringify(result, null, 2)}\n`)
  process.exitCode = result.statusCode === 200 && result.body.status === 1 ? 0 : 1
}

run().catch((error) => {
  process.stderr.write(`${error.message}\n`)
  process.exitCode = 1
})
