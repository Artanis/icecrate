% rebase("base.tpl", subtitle="Oops! Something broke")
<article>
  <h2>Oops! Something broke.</h2>
  <p>Please visit <a href="https://github.com/Artanis/icecrate/issues">Icecrate's bug tracker</a> at GitHub and post the following error report so we can fix this:</p>
  <textarea>{{error.traceback}}</textarea>
</article>
