const kue = require('kue');
const redis = require('redis');

const client = redis.createClient();
const queue = kue.createQueue({
  prefix: 'q',
  redis: {
    createClientFactory: () => client
  }
});

function sendNotification (phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', function (job, done) {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

queue.on('error', function (err) {
  console.log('Kue Error:', err);
});

process.once('SIGTERM', function (sig) {
  queue.shutdown(5000, function (err) {
    console.log('Kue shutdown:', err || 'OK');
    client.quit();
    process.exit(0);
  });
});

console.log('Job processor is running...');
