import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const hashKey = 'ALX';
const hashValues = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2',
};

Object.entries(hashValues).forEach(([field, value]) => {
  client.hset(hashKey, field, value, redis.print);
});

client.hgetall(hashKey, (err, object) => {
  console.log(object);
});
