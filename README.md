# Testypie

A test helper service that autogenerates your fixtures by recording real HTTP
requests in order to replay them.

The main advantage is that it is agnostic to what underlying HTTP library you
are using (or even what programming language you are using).

It works as a distinct proxy but can also be used as a library in Python tests,
e.g. combined with [HTTPretty](https://github.com/gabrielfalcao/HTTPretty).

## Usage

Say you have a unit test in Node.js

To run standalone (suitable for testing in any language):

```bash
$ pip install testypie
$ testypie
 * Serving Flask app "testypie" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Then run your