% rebase("base.tpl", subtitle="All Items")
% setdefault("items", [])
% setdefault("debug", False)
<article>
  <h2>All Items</h2>
  % include("items_list", items=items)
</article>
