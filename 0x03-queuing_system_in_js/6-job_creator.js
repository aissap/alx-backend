import kue from 'kue';
import redis from 'redis';

const client = redis.createClient();

const queue = kue.createQueue({ redis: { createClientFactory: () => client } });

const jobData = {
  phoneNumber: '1234567890',
  message: 'Notification message here'
};

const job = queue.create('push_notification_code', jobData);

// Handle job creation success
job.on('enqueue', function (id, type) {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', function () {
  console.log('Notification job completed');
  process.exit(0); // Exit after job completion
});

job.on('failed', function () {
  console.log('Notification job failed');
  process.exit(1); // Exit after job failure
});

job.save();

process.on('SIGINT', function () {
  queue.shutdown(5000, function (err) {
    console.log('Kue shutdown: ', err || 'OK');
    client.quit();
    process.exit(0);
  });
});
