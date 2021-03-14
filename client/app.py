from redis import StrictRedis
import string

r = StrictRedis(host='twemproxy', port=26379, db=0)

for c in string.ascii_lowercase:
    r.set(c, 'bar')

# hash_tag feature uses string between {} as hash key
# these keys will land on the same node
r.set('foo', 'bar')
r.set('{foo}d', 'bar')
r.set('love{foo}l', 'bar')
r.set('{foo}', 'bar')

# set is good
r.set('bar', 'stool')
r.set('{bar}d', 'stool')
r.set('love{bar}l', 'stool')
r.set('re{bar}', 'stool')

# setex is good
r.setex(name='s{ock}', time=3600, value=1)
r.setex(name='ock', time=3600, value=2)
r.setex(name='sm{ock}', time=3600, value=3)
r.setex(name='d{ock}ing', time=3600, value=3)

# get is good
print(r.get(name='s{ock}'))
print(r.get(name='sm{ock}'))

# # scan is not supported by twemproxy
# for key in r.scan_iter(match='ock'):
#     print(key)

# try set
value_set='{ock}_set'
r.sadd(value_set, 'ock')
r.sadd(value_set, 's{ock}')
r.sadd(value_set, 'sm{ock}')
r.sadd(value_set, 'd{ock}ing')
print(r.smembers(value_set))