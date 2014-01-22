Shovel-server
=============
Access your shovel tasks through an API.

This has been moved out of the main `shovel` repo and into its own for clarity
and better encapsulation. As such, this repo is currently pretty scant, but can
grow with interest. __It's also unclear what its compatibility with the latest
version of shovel is.__

Browser
-------
Shovel-server is a small [`bottle`](http://bottlepy.org/docs/dev/) server,
designed to make all your shovel tasks accessible from a browser. At some
point, I'd like to make it accessible as an API as well, returning JSON blobs
instead of HTML output when requested. That said, it's not a high priority --
if it's something you're after, let me know!

You can access the browser utility by starting up the `shovel-server` utility
from the same directory where you'd normally run your shovel tasks. You may 
optionally supply the `--port` option to specify the port on which you'd like
it to listen, and `--verbose` for additional output:

    # From the directory where your shovel tasks are
    shovel-server

By default, the `shovel-server` listens on port 3000, and you can access many
of the same utilities you would from the command line. For instance, help is
available through the [/help](http://localhost:3000/help) endpoint. Help for
a specific function is available by providing the name of the task (or group)
as a query parameter. To get more help on task `foo.bar`, you'd visit
[/help?foo.bar](http://localhost:3000/help?foo.bar), etc.

Tasks are executed by visiting the `/<task-name>` end-point, and the query 
parameters are what gets provided to the function. Query parameters without
values are considered to be positional, and query parameters with values are
considered to be keyword arguments. For example, the following are equivalent:

    # Accessing through the HTTP interface
    curl http://localhost:3000/foo.bar?hello&and&how&are=you
    # Accessing through the command-line utility
    shovel foo.bar hello and how --are=you
    # Executing the original python function
    ...
    >>> bar('hello', 'and', 'how', are='you')

In this way, we can support conventional arguments, variable arguments, and
keyword arguments. That said, there is a slight difference in the invocation
from the command-line and through the browser. In the command-line tool, 
keyword arguments without values are interpreted as flags, where in the url,
that is not the case. For example, in the following invocation, both 'a' and
'b' would be passed as 'True' into the function, but there is no equivalent
in the URL form:

    shovel foo.bar --a --b

A convenient feature of the shovel server is that it checks the last-modified
time of the input shovel files, and reimports any definitions that have been
updated since it last checked. So if you save your shovel files, the changes
will be reflected in the web app.
