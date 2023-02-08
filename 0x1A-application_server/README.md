# 0x1A-application_server

## Concepts

- [Web server](https://intranet.alxswe.com/concepts/17)
- [Server](https://intranet.alxswe.com/concepts/67)
- [Web stack debugging](https://intranet.alxswe.com/concepts/68)


![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230208%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230208T222316Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=bb5fee625c95e7318bf9650f68f3cd6e2a3f2dee62c8c8d2df28673786316769)

## Background Concepts

Your web infrastructure is already serving web pages via `Nginx` that you installed in your [first web stack project](https://intranet.alxswe.com/rltoken/95oRNZ-zRGwLxtWECJqsWA).
While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your `Nginx` and make is serve your Airbnb clone project.

## Resources

**Read or watch:**

- [Application server vs web server](https://intranet.alxswe.com/rltoken/B9fOBzIxX_t1289WAuRzJw)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://intranet.alxswe.com/rltoken/kpG6RwmwRJHzRmGUM_ERcA) (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)
- [Running Gunicorn](https://intranet.alxswe.com/rltoken/2LF1j7xKJGYaUtD1HKgUeQ)
- [Be careful with the way Flask manages slash](https://intranet.alxswe.com/rltoken/lEg0zpkkDcLtdl3VD4ACRQ) in [route](https://intranet.alxswe.com/rltoken/Zn8fYk-U9YRm7Z5Coqqb0g) - `strict_slashes`
- [Upstart documentation](https://intranet.alxswe.com/rltoken/mcEsKqFsjJA3tHAjiMknaw)


## Tasks

### 0. Set up development with Python

Let’s serve what you built for [AirBnB clone v2 - Web framework](https://intranet.alxswe.com/rltoken/uEAW4JG-DyhtSjYNP9o1mQ) on `web-01`. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:

- Make sure that [task #3](https://intranet.alxswe.com/rltoken/ecvps9dI2mv1QUu3dn99mA) of your [SSH project](https://intranet.alxswe.com/rltoken/7-lshY-qe4ZxKabnC7pY4Q) is completed for `web-01`. The checker will connect to your servers.
- Git clone your `AirBnB_clone_v2` on your `web-01` server.
- Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port `5000`.
- Your Flask application object must be named `app` (This will allow us to run and check your code).


### 1. Set up production with Gunicorn

Now that you have your development environment set up, let’s get your production application server set up with `Gunicorn` on `web-01`, port `5000`. You’ll need to install `Gunicorn` and any libraries required by your application. Your `Flask` application object will serve as a [WSGI](https://intranet.alxswe.com/rltoken/IaAZ7A8IYGkO9Ah9uwL39Q) entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.

Requirements:

- Install `Gunicorn` and any other libraries required by your application.
- The Flask application object should be called `app`. (This will allow us to run and check your code)
- You will serve the same content from the same route as in the previous task. You can verify that it’s working by binding a `Gunicorn` instance to localhost listening on port `5000` with your application object as the entry point.
- In order to check your code, the checker will bind a `Gunicorn` instance to port `6000`, so make sure nothing is listening on that port.


### 2. Serve a page with Nginx

Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/

Requirements:

- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the process listening on port 5000.
- Include your Nginx config file as 2-app_server-nginx_config.

