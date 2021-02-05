# the partition() method of bytes and string objects does what it says: it partitions the input into three parts: before the separator, the separator itself, and after the separator
#
# unlike split(), partition() is *guaranteed* to return three parts (but they might be empty), so it's safe to do `before, separator, after = something.partition(",")` for instance
#
#
# `"foo,bar".partition(",")` gives the result: `('foo', ',', 'bar')`
#
# g=re.compile(r" ' (?P<username> .*? ) , (?P<os> .*? )'", re.X).search(x)
#
# datarb = (b'\'bowser,Windows\'')
# datars = datarb.decode("utf-8")
# print(datars)
# username, sep, os = datars.partition(",")
# print(username)
# print(sep)
# print(os)
# x = username.strip("''")
# y = os.strip("'")
# print(x)
# print(y)


`async with await anyio.open_file(...`

#when you do logging.info('foo: %s' % expensive), you're crafting that 'foo: <expensive>' string in memory immediately, even if you're not logging that debug message based on your debug level
#contrast to logging.info('foo: %s', expensive) -- this is much less expensive in memory, because logging will defer evaluating that string until later when the debug is actually executing