% setdefault("items", [])
% if len(items) > 0:
<table>
  <thead>
    <tr>
      <td>SKU</td><td>Name</td><td>Quantity</td>
    </tr>
  </thead>
  <tbody>
    % for item in items:
    %   if item.get("upc", None) is not None:
    <tr>
      <td>{{item.get("upc")}}</td>
      <td><a href="/items/{{item.get('upc')}}">{{item.get("name", item.get("upc"))}}</a></td>
      <td>{{item.get("quantity", "Unknown")}}</td>
    </tr>
    %   end
    % end
  </tbody>
</table>
% else:
<p>There are no items to see.</p>
% end
