% rebase("base.tpl", subtitle=taginfo.get("name", None))
<article>
  <h2>{{taginfo.get("name")}}</h2>
  <h3>{{len(members)}} Members</h3>
  % include("items_list.tpl", items=members)
</article>
