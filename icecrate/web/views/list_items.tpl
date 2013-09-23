% rebase("base.tpl", subtitle="All Items")
% setdefault("items", [])
% setdefault("debug", False)
<article>
  <h2>All Items</h2>
  % if len(items) > 0:
  <table>
    <thead>
      <tr><th></th><th>Item Name</th><th>Quantity</th></tr>
    </thead>
    <tbody>
      % for item in items:
        % if item.get("upc", None) is not None:
          <tr>
            <td><input type="checkbox" /></td>
            <td><a href="/items/{{item.get('upc')}}">{{item.get('name', item.get("upc"))}}</a></td>
            <td>{{item.get("quantity", 0)}}</td>
          </tr>
          % if debug == True:
          <tr><td></td><td colspan="2">{{str(item)}}</td></tr>
          % end
        % end
      % end
    </tbody>
  </table>
  % else:
    <p>There are no items to see.</p>
  % end
</article>
