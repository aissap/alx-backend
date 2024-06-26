# 0x03. Queuing System in JS

## Resources
Read or watch:
- [Redis quick start](https://redis.io/topics/quickstart)
- [Redis client interface](https://redis.io/clients)
- [Redis client for Node JS](https://github.com/NodeRedis/node-redis)
- [Kue deprecated but still used in the industry](https://github.com/Automattic/kue)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to build a basic Express app interacting with a Redis server and queue

## Requirements
- All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All of your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `.js` extension

## Required Files for the Project
- `package.json`
  ```json
  {
    "name": "queue-system",
    "version": "1.0.0",
    "description": "A simple queuing system using Redis and Node.js",
    "main": "index.js",
    "scripts": {
      "start": "node index.js"
    },
    "dependencies": {
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^3.1.2"
    }
  }
