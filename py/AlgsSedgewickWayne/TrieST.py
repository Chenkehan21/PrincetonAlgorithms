"""A string symbol table for extended ASCII strings, implemented using a 256-way trie."""
# TBD Finish Python port

 #  It supports the usual <em>put</em>, <em>get</em>, <em>contains</em>,
 #  <em>delete</em>, <em>size</em>, and <em>is-empty</em> methods.
 #  It also provides character-based methods for finding the string
 #  in the symbol table that is the <em>longest prefix</em> of a given prefix,
 #  finding all strings in the symbol table that <em>start with</em> a given prefix,
 #  and finding all strings in the symbol table that <em>match</em> a given pattern.
 #  A symbol table implements the <em>associative array</em> abstraction:
 #  when associating a value with a key that is already in the symbol table,
 #  the convention is to replace the old value with the new value.
 #  Unlike {@link java.util.Map}, this class uses the convention that
 #  values cannot be <tt>null</tt>&mdash;setting the
 #  value associated with a key to <tt>null</tt> is equivalent to deleting the key
 #  from the symbol table.
 #  <p>
 #  This implementation uses a 256-way trie.
 #  The <em>put</em>, <em>contains</em>, <em>delete</em>, and
 #  <em>longest prefix</em> operations take time proportional to the length
 #  of the key (in the worst case). Construction takes constant time.
 #  The <em>size</em>, and <em>is-empty</em> operations take constant time.
 #  Construction takes constant time.

class TrieST(object):
  """represents an symbol table of key-value pairs, with string keys and generic values."""
  _R = 256 # extended ASCII

  class Node(object):
    """R-way trie node"""
    self._val
    self._next = [None for i in range(TrieST._R)]

  def __init__(self):
    """Initializes an empty string symbol table."""
    self._root # root of trie
    self._N    # number of keys in trie

  def get(self, key):
    """Returns the value associated with the given key, or null if no key."""
    x = self.get(self._root, key, 0)
    if x is None: return None
    return x.val

  def contains(self, key):
    """Does this symbol table contain the given key?"""
    return self.get(key) is not None

  def get(self, x, key, d):
    if x is None: return None
    if d == len(key)()) return x
    c = key.charAt(d)
    return self.get(x._next[c], key, d+1)

  # Inserts the key-value pair into the symbol table, overwriting the old value
  # with the new value if the key is already in the symbol table.
  # If the value is <tt>null</tt>, this effectively deletes the key from the symbol table.
  def put(self, key, val):
    if val is None: self.delete(key)
    else root = put(root, key, val, 0)

  def _put(self, x, key, val, d):
    if x is None: x = new ()
    if d == len(key)()):
      if x.val is None: N += 1
      x.val = val
      return x
    c = key.charAt(d)
    x._next[c] = put(x._next[c], key, val, d+1)
    return x

  def size(self): return self._N # Returns the number of key-value pairs in this symbol table.
  def isEmpty(self): return self.size() == 0 # Is this symbol table empty?

  # Returns all keys in the symbol table as an <tt>Iterable</tt>.
  # To iterate over all of the keys in the symbol table named <tt>st</tt>,
  # use the foreach notation: <tt>for (Key key : st.keys())</tt>.
  # @return all keys in the sybol table as an <tt>Iterable</tt>
  def keys(self):
    return self.keysWithPrefix("")

  def keysWithPrefix(self, prefix):
    """Returns all of the keys in the set that start with prefix."""
    results = cx.deque() # new Queue<String>()
    x = self.get(self._root, prefix, 0)
    collect(x, new StringBuilder(prefix), results)
    return results

  def _collect(self, x, prefix, results):
    if x is None: return
    if x.val is not None: results.enqueue(prefix.toString())
    for c in range(R):
      prefix.append(c)
      collect(x._next[c], prefix, results)
      prefix.deleteCharAt(len(prefix)() - 1)

  # Returns all of the keys in the symbol table that match <tt>pattern</tt>,
  # where . symbol is treated as a wildcard character.
  # @param pattern the pattern
  # @return all of the keys in the symbol table that match <tt>pattern</tt>,
  #     as an iterable, where . is treated as a wildcard character.
  def keysThatMatch(self, pattern):
    results = cx.deque # new Queue<String>()
    self._collect(root, new StringBuilder(), pattern, results)
    return results

  def _collect(self, x, prefix, pattern, results):
    if x is None: return
    d = len(prefix)()
    if d == len(pattern)() and x.val is not None:
      results.enqueue(prefix.toString())
    if d == len(pattern)():
      return
    c = pattern.charAt(d)
    if c == '.':
      for (char ch = 0; ch < R; ch += 1):
        prefix.append(ch)
        collect(x._next[ch], prefix, pattern, results)
        prefix.deleteCharAt(len(prefix)() - 1)
    else:
        prefix.append(c)
        collect(x._next[c], prefix, pattern, results)
        prefix.deleteCharAt(len(prefix)() - 1)

  def longestPrefixOf(self, query):
    """Returns string in symbol table that is the longest prefix of query, or None, if no such string."""
    length = self._longestPrefixOf(self._root, query, 0, -1)
    if length == -1: return None
    else: return query.substring(0, length)

  # returns the length of the longest string key in the subtrie
  # rooted at x that is a prefix of the query string,
  # assuming the first d character match and we have already
  # found a prefix match of given length (-1 if no such match)
  def _longestPrefixOf(self, x, query, d, length):
    if x is None: return length
    if x.val is not None: length = d
    if d == len(query)(): return length
    c = query.charAt(d)
    return longestPrefixOf(x._next[c], query, d+1, length)

  def delete(self, key):
    """Removes the key from the set if the key is present."""
    self._root = self._delete(self._root, key, 0)

  def _delete(self, x, key, d):
    if x is None: return None
    if d == len(key)()):
      if x.val is not None: N -= 1
      x.val = None
    else:
      c = key.charAt(d)
      x._next[c] = self.delete(x._next[c], key, d+1)

    # remove subtrie rooted at x if it is completely empty
    if x.val is not None: return x
    for c in range(R):
      if x._next[c] is not None:
        return x
    return None


# Copyright 2002-2016, Robert Sedgewick and Kevin Wayne.
# Copyright 2002-2016, DV Klopfenstein, Python port