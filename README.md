# OSC Example

This is a quick example OSC server example in C++.

The transport is implemented using a simple UDP layer, the header ```upd.hpp``` provides
a thin abstraction over POSIX sockets. (It will not work on Windows!)

To test it compile:

```bash
clang++ -o udp_server -I./ -std=c++17 server.cpp udp.cpp
```

To test server on your local machine:

```bash
./udp_server
```

You can then test the using the Python client:

```bash
python3 main.py
```

The server should output:

```bash
/filter 0.568941
/multi goo 20
```

You need to just compile and run the C++ app on the Bela, as above. Then run the Python
script from a machine on the same network, but this time with:

```bash
python3 main.py -ip BELA.IP.ADDRESS.
```

Hopefully at this point the basic OSC server is running on Bela and it can be wrapped around
and stuck in a thread.
