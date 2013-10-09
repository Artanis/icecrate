% rebase("base", subtitle=q)
% setdefault("items", [])
<article>
  <h2>Search Results</h2>
  <p>You searched for "{{q}}"!</p>
  <p>There are no actual search results. This page is a stub for the planned search feature, and currently echoes your search terms back to you.</p>
  % if len(items) > 0:
  <ol>
    % for item in items:
    %     include("search_result.tpl", item=item)
    % end
  </ol>
  % end
</article>
