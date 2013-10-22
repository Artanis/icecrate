% setdefault("item", None)
<li>
% if item is not None:
  <div>
    <h3><a href="/items/{{item.get('upc')}}">{{item.get("name", item.get("upc"))}}</a></h3>
  </div>
% else:
  <p>Error: missing result.</p>
% end
</li>
