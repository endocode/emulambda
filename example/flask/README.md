# flask server for emulambda

## Getting started

Change to the directory `example/flask`, and run the flask server.

```
$ cd example/flask
$ FLASK_APP=flask_event.py flask run
```

### event mode

On the other console, run emulambda with event mode

```
$ emulambda -v flask_event.lambda_handler ./flask_event.json
```


### stream mode

On the other console, run emulambda with stream mode

```
$ emulambda -s -v flask_event.lambda_handler ./flask_stream.ldjson
```
