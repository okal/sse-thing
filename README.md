## Introduction

This repo demonstrates, by means of a basic Flask application, how to implement Server Sent Events.

MDN has a great primer on the subject at https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events

The `/remote` endpoint sends a streaming response with `Content-Type: text/event-stream` sending the timestamp every second. That's it, basically.

## Usage

```shell
$ docker build .
$ docker run -it -p 5000:5000 <image ID from previous step>
* Serving Flask app "remote.py"
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Navigate to http://localhost:5000 and open the browser console.

## What I learnt

1. Remember to terminate each message with two newlines. It took me a long time to figure out that that's what I was doing wrong, since only the error handler in `static/script.js` would get called.
2. Also, I don't care enough to fix it, but the first line in the console will always be an error, simply because of Flask's built in single threaded development webserver. The browser will attempt to load the event stream while the page is still being served, which the server can't handle. Whatever 🤷🏾‍♀️

## So what's this good for?

This repo? Well, not much. Just to show you how you might go about implementing server-sent events, which are an absolute delight. They're a great built-in abstraction to long-polling, and a great alternative to websockets for some use cases. I was personally looking for a way to notify the UI upon completion of an async request made by a service backend to another service, which would then notify the originating server by means of a HTTP callback. Anyway, the details aren't important. I hope it's useful to someone looking for a simple example of how they might implement that. It could have probably fit into a gist, but those don't have directories 🤷🏾‍♀️