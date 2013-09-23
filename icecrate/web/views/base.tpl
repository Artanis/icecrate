<!DOCTYPE html>
% setdefault("subtitle", None)
% appname = "Icecrate"
% pagetitle = appname
% if subtitle is not None:
%     pagetitle = subtitle + " &mdash; " + appname
% end
<html>
  <head>
    <title>{{!pagetitle}}</title>
    <link rel="stylesheet" type="text/css" href="/static/reset.css">
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <script type="text/javascript" src="//ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>
    <script type="text/javascript" src="/static/xzing.js"></script>
    <meta name="viewport" content="width=device-width, maximum-scale=1, minimum-scale=1" />
  </head>
  <body id="home">
    <div class="wrapper">
      <header>
        <h1 class="logo"><a href="/">{{appname}}</a></h1>
        <a class="to_nav" href="#primary_nav">Menu</a>
      </header>
      <div id="content">
        {{!base}}
      </div>
      <nav id="primary_nav">
        <ul>
          <li><a class="zxing" href="/items/{CODE}">Scan</a></li>
          <li><a href="/items">All Items</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="/help">Help</a></li>
          <li class="to_top"><a href="#home">Top</a></li>
        </ul>
      </nav>
      <footer>
        <p>Icecrate &copy; 2013, Erik Youngren</p>
        <p><a href="https://github.com/Artanis/icecrate">Icecrate</a> is a simple inventory system written in <a href="http://www.python.org/">Python 3</a> using <a href="http://bottlepy.org/">bottle.py</a>. Icecrate is licensed under the <a rel="license" href="https://github.com/Artanis/icecrate/blob/master/LICENSE">BSD 2-clause license</a>.</p>
      </footer>
    </div>
  </body>
</html>
