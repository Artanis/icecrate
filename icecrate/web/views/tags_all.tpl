% rebase("base", subtitle="All Tags")
% setdefault("tags", [])
<article>
  <h2>All Tags</h2>
  % if len(tags) > 0:
  <ul>
    % for tag in tags:
    <li><a href="/tags/{{tag}}">{{tag}}</a></li>
    % end
  </ul>
  % else:
  <p>There are no tags to see.</p>
  % end
</article>
