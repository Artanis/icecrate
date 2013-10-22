% rebase("base", subtitle=q)
% setdefault("results", [])
<article>
  <h2>Search Results</h2>
  % if len(results) > 0:
  % include("search_list.tpl", results=results)
  % else:
  <p>There were no documents matching your search for "{{q}}"</p>
  % end
</article>
