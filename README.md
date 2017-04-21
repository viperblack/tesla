# Tesla
Opens, decrypts, and manages saved email messages.  Retrives the message inside a file exported by Outlook (file.msg).

Note: this project assumes only one encrypted block in the message.  If there is more than one encrypted block, than it will not work. 

Environment preparation:

```
$ pip3 install virtualenv
$ cd tesla
$ virtualenv tesla
$ source tesla/bin/activate
$ pip3 install olefile
```

Usage:

```
$ chmod +x tesla.py
$ tesla.py file.msg
```

or

```python
>>> import tesla
>>> msg = tesla.Message('file.msg')
>>> print(msg.get_pgp_msg())
```


# License
This project is licensed under a MIT license.  See the [msg-extractor](https://github.com/mattgwwalker/msg-extractor) to read its licensing --currently it is GPL.
