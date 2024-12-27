import redis from 'redis';

const cliPub = redis.createClient();

cliPub.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

cliPub.on('connect', () => {
  console.log('Redis client connected to the server');
});

const CHANNEL = 'ALX channel';

function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    cliPub.publish(CHANNEL, message);
  }, time);
}

publishMessage('ALX Student #1 starts course', 100);
publishMessage('ALX Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('ALX Student #3 starts course', 400);
