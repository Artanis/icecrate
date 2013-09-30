% setdefault("items", [])
% if len(items) > 0:
<form method="POST" action="/items">
  <table>
    <thead>
      <tr>
        <td></td><td>SKU</td><td>Name</td><td>Quantity</td>
      </tr>
    </thead>
    <tbody>
      % for item in items:
      %   if item.get("upc", None) is not None:
      <tr>
        <td><input type="checkbox" name="items" value="{{item.get('upc')}}"></td>
        <td>{{item.get("upc")}}</td>
        <td><a href="/items/{{item.get('upc')}}">{{item.get("name", item.get("upc"))}}</a></td>
        <td>{{item.get("quantity", "Unknown")}}</td>
      </tr>
      %   end
      % end
    </tbody>
  </table>
  <input type="submit" name="action" value="Delete Selected">
</form>
% else:
<p>There are no items to see.</p>
% end
