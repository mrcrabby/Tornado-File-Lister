Tornado File Lister is a simple async HTTP file server that makes use of some of the key features of the [Tornado Web Framework] (http://www.tornadoweb.org/).

First, make sure your have Tornado installed.

To run the file lister, simply unzip/untar and deploy to the desired directory.

* Then open a shell and:
	<pre><code>python server.py</code></pre>
* If you'd like to run the server on a port other than 8888:
	<pre><code>python server.py --port=XXXX</code></pre>
	
- - -

The file lister can also be run behind a static file server like [nginx](http://www.nginx.org) for extreme optimization. See the [Tornado Documentation](http://www.tornadoweb.org/documentation#running-tornado-in-production) for more details.


-Hunter