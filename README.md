# hello-twemproxy
Taking twemproxy for a sprin

## Demo
Try the twemproxy demo
```
docker-compose up --build
```

This will start 4 local redis instances, twemproxy, and a python redis client. The client will set values and these will be sharded
across redis instances.

twemproxy also supports a hash_tag feature, which enables us to send
keys with a common substring to the same node.

However, twemproxy does not support the `scan` operation.

```
twemproxy_1  | [2021-02-14 03:59:21.488] nc_redis.c:1092 parsed unsupported command 'SCAN'
twemproxy_1  | [2021-02-14 03:59:21.488] nc_core.c:237 close c 11 '172.25.0.7:44076' on event 00FF eof 0 done 0 rb 1307 sb 204: Invalid argument
client_1     | b'1'
client_1     | b'3'
client_1     | Traceback (most recent call last):
client_1     |   File "/usr/src/app/./app.py", line 33, in <module>
client_1     |     for key in r.scan_iter(match='ock'):
client_1     |   File "/usr/local/lib/python3.9/site-packages/redis/client.py", line 2131, in scan_iter
client_1     |     cursor, data = self.scan(cursor=cursor, match=match,
client_1     |   File "/usr/local/lib/python3.9/site-packages/redis/client.py", line 2112, in scan
client_1     |     return self.execute_command('SCAN', *pieces)
client_1     |   File "/usr/local/lib/python3.9/site-packages/redis/client.py", line 901, in execute_command
client_1     |     return self.parse_response(conn, command_name, **options)
client_1     |   File "/usr/local/lib/python3.9/site-packages/redis/client.py", line 915, in parse_response
client_1     |     response = connection.read_response()
client_1     |   File "/usr/local/lib/python3.9/site-packages/redis/connection.py", line 739, in read_response
client_1     |     response = self._parser.read_response()
client_1     |   File "/usr/local/lib/python3.9/site-packages/redis/connection.py", line 324, in read_response
client_1     |     raw = self._buffer.readline()
client_1     |   File "/usr/local/lib/python3.9/site-packages/redis/connection.py", line 256, in readline
client_1     |     self._read_from_socket()
client_1     |   File "/usr/local/lib/python3.9/site-packages/redis/connection.py", line 201, in _read_from_socket
client_1     |     raise ConnectionError(SERVER_CLOSED_CONNECTION_ERROR)
client_1     | redis.exceptions.ConnectionError: Connection closed by server.
hello-twemproxy_client_1 exited with code 1
```