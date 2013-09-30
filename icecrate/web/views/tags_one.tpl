% rebase("base.tpl", subtitle=tag.get("name", None))
<article>
  <h2>{{tag.get("name")}}</h2>
  <h3>Members</h3>
  % include("items_list.tpl", items=members)
</article>
