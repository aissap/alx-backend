const kue = require('kue');

const que = kue.createQueue();

const Data = {
  phoneNumber: '4153518780',
  message: 'This is the code 1234 to verify your account'
};

const job = que.createJob('push_notification_code', Data)

job.save((err) => {
    if (err) {
      console.error('Error creating job:', err);
      return;
    }
    console.log(`Notification job created: ${job.id}`);
});
job.on('complete', () => {
    console.log('Notification job completed');
    process.exit(0);
});

job.on('failed', (err) => {
    console.error('Notification job failed:', err);
    process.exit(1);
});

console.log('Job creator is running...');
