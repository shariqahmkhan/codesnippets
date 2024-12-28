# FLASK
When running Flask, the host parameter specified in app.run() within app.py takes effect only if you are directly running the script (python app.py). 
If you're using flask run, the app.run() parameters in app.py are ignored because flask run is controlled by the Flask CLI, which defaults to 127.0.0.1.

Solution: Use --host=0.0.0.0 with flask run, as the CLI parameters override the settings in your script:

### Problem

Problem:
Flask app does not run inside docker

Solution:
By default, flask run binds to 127.0.0.1 (localhost), which makes the server inaccessible from outside the container. 
Docker runs containers in an isolated network, so binding to 127.0.0.1 only allows connections from within the container itself.

Solution:
You need to bind the Flask app to 0.0.0.0, which allows it to accept connections from any network interface.

Add the --host=0.0.0.0 flag:

CMD ["flask", "run", "--host=0.0.0.0"]
