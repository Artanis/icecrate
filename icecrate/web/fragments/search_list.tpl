% setdefault("results", [])
<ol class="search-results">
  % for hit in results:
  %     include("search_result.tpl", item=hit)
  % end
</ol>
