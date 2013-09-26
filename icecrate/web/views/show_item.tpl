% rebase("base.tpl", subtitle=(item.get('name', upc)))
% setdefault("in_db", False)
<article>
  <h2>{{item.get('name', upc)}}</h2>
  <form method="POST" action="/items/{{upc}}">
    <input type="text" name="name" id="item_name" placeholder="Name" value="{{item.get('name', '')}}" tabindex="1">
    <br/>
    <input type="text" id="tags" name="tags" placeholder="Descriptive tags" value="{{item.get('tags', '')}}" tabindex="2">
    <br/>
    <input type="number" value="{{item.get('quantity', 0)}}" name="quantity" id="quantity" autofocus="autofocus" tabindex="3">
    <br/>
    <input type="submit" value="{{'Update' if in_db else 'Save'}}" tabindex="4">
    <!-- <input type="submit" value="Delete"/> -->
  </form>
</article>
