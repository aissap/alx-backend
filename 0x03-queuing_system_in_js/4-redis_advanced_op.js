import redis from 'redis';

const client = redis.createClient();

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function(err) {
    console.log('Redis client not connected to the server: ' + err.message);
});

const key = 'HolbertonSchools';
const values = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
};

for (const [field, value] of Object.entries(values)) {
    client.hset(key, field, value, redis.print);
}

client.hgetall(key, (err, res) => {
    if (err) {
        console.error('Error:', err);
    } else {
        console.log(res);
    }
});
