import redis from 'redis';

const cliScr = redis.createClient();

cliScr.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

cliScr.on('connect', () => {
  console.log('Redis client connected to the server');
});

const CHANNEL = 'ALXchannel';

cliScr.subscribe(CHANNEL);

cliScr.on('message', (channel, message) => {
  if (channel === CHANNEL) console.log(message);
  if (message === 'KILL_SERVER') {
    cliScr.unsubscribe(CHANNEL);
    cliScr.quit();
  }
});
