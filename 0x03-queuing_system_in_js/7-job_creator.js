import kue from 'kue';
import redis from 'redis';

const client = redis.createClient();
const queue = kue.createQueue({ redis: { createClientFactory: () => client } });

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

jobs.forEach((jobData, index) => {
  const job = queue.create('push_notification_code_2', jobData);

  job.on('enqueue', function (id, type) {
    console.log(`Notification job created: ${job.id}`);
  });

  job.on('complete', function () {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('failed', function (err) {
    console.log(`Notification job ${job.id} failed: ${err}`);
  });

  job.on('progress', function (progress) {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });

  job.save();
});

process.on('SIGINT', function () {
  queue.shutdown(5000, function (err) {
    console.log('Kue shutdown: ', err || 'OK');
    client.quit();
    process.exit(0);
  });
});

console.log('Job creator is running...');
