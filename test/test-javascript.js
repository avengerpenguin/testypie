const http = require('http');
const https = require('https');
const axios = require('axios');
const assert = require('assert');

const agentOptions = {
    host: 'locahost',
    port: '5000',
    path: '/',
    rejectUnauthorized: false,
  }
const agent = new https.Agent(agentOptions)

function keyCounter(url) {
  return axios.get({
    url,
    responseType: 'json',
    agent,
    headers: {'User-Agent': 'Testypie Tests'},
  }).then(response => Object.keys(response.data).length);
}

describe('Example', function() {
  it('should measure length of HTTP responses', function() {

    return keyCounter('http://dbpedia.org/data/Elephant.json')
      .then(function(length) {
        assert.equal(length, 99);
      });

  });

  it('should measure length of HTTPS responses', function() {

    return keyCounter('https://reddit.com/r/python.json')
      .then(function(length) {
        assert.equal(length, 59754);
      });

  });
});
