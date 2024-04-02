# flask-pygbag-gamehost
Flask template to host an app that was build with the [pygbag module](https://github.com/pygame-web/pygbag)

## How to use it
1. Clone this repository 

2. Build your pygame projekt with pygbag (click [here](https://github.com/pygame-web/pygbag) for further command explaination) 
```sh
python3 -m pygbag --build main.py
```

3. Replace the [build-folder](./build/) with the folder that was builded in step 2

4. Run the flask server:
```sh
python3 app.py
```

## Edit for own usage
- Add your own routes in [app.py](./app.py) for more functionality e.g.:
    - Make usage of python libraries that are not compatible with wasm
    - Using files like images in the index.html
- Change the SSL keys:
    - to your own public and private key
    - or change the [ssl_context](./app.py#L29) to the string "adhoc" for local testing