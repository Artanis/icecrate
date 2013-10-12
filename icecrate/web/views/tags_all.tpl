% rebase("base", subtitle="All Tags")
% setdefault("tags", [])
<article>
  <h2>All Tags</h2>
  % if len(tags) > 0:
  <ul>
    % for taginfo, members in tags:
    <li><a href="/tags/{{taginfo.get('name')}}">{{taginfo.get('name')}}</a>&times;{{len(members)}}</li>
    % end
  </ul>
  % else:
  <p>There are no tags to see.</p>
  % end
</article>
