# tcp_PyChat v1.0.0.
[![Build Status](https://travis-ci.com/RolEYder/tcp_PyChat.svg?branch=master)](https://travis-ci.com/RolEYder/tcp_PyChat)

<img src="/docs/tcp_Pychat.gif" width="1000" height="500"/>



**tcp_Pychat** is a [IRC Server](https://es.wikipedia.org/wiki/Internet_Relay_Chat) that implement a MongoDB as storage writing on Python.



# Releases!

  - Initial release
  










### Stack

Here the development-stack that we used to build this IRC Server:

* [Python](https://www.python.org/) - Python is a programming language that lets you work quickly and integrate systems more effectively.
* [PyMongo](https://pymongo.readthedocs.io/en/stable/) - PyMongo is a Python distribution containing tools for working with [MongoDB](https://www.mongodb.com/cloud/atlas/lp/try2?utm_source=google&utm_campaign=gs_footprint_row_search_brand_atlas_desktop&utm_term=mongo%20database&utm_medium=cpc_paid_search&utm_ad=e&gclid=CjwKCAjw2uf2BRBpEiwA31VZj43lEO-cVRPZ1yNC0FpH40PDKuMkYTC2koMFwwN4C3lx0VxejYuGLRoCVH4QAvD_BwE), and is the recommended way to work with MongoDB from Python.
* [Socket](https://docs.python.org/3/library/socket.html) - This module provides access to the BSD socket interface. It is available on all modern Unix systems, Windows, MacOS, and probably additional platforms.




### Quicky installation

**tcp_PyChat** requires [Python](https://www.python.org/) v3.5+ to run.

Install the all componets needed to run **tcp_PyChat**.
Open your favorite Terminal and run these commands.

```sh
$ git clone https://github.com/RolEYder/tcp_PyChat.git
$ cd pychat
$ pip3 install -r requirements.txt
$ python3 pychat_server.py -ip 127.0.0.1 -p 4444
$ python3 pychat_client.py -ip 127.0.0.1 -p 4444
```





### Usage

**tcp_PyChat** use [TCP](https://en.wikipedia.org/wiki/Transmission_Control_Protocol) connections throught python module socket.



To run the `SERVER` type:
```sh
$ python3 pychat_server.py -ip 127.0.0.1 -p 4444
```
where `-ip` is the ip connect IP address server and `-p` is the connect port. 

To run the `CLIENT` type:
```sh
$ python3 pychat_client.py -ip 127.0.0.1 -p 4444
```
where `-ip` is the ip connect IP address client and `-p` is the connect port. 









### Author

 - Rogger G. D. (rolEYder) 
 -> Medium [rolEYder](https://medium.com/@rolEYder)
 

License
----

MIT





