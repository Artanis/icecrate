% rebase("base.tpl", subtitle=(item.get('name', upc)))
<article>
  <h2>{{item.get('item_name', upc)}}</h2>
  <form method="POST" action="/items/{{upc}}">
    <input type="text" name="name" id="item_name" placeholder="Name" value="{{item.get('name', '')}}">
    <br/>
    <input type="text" id="tags" name="tags" placeholder="Descriptive tags" value="{{item.get('tags', '')}}">
    <br/>
    <input type="number" value="{{item.get('quantity', 0)}}" name="quantity" id="quantity" autofocus="autofocus" />
    <br/>
    <input type="submit" value="{{'Update' if in_db else 'Save'}}" />
    <!-- <input type="submit" value="Delete"/> -->
  </form>
</article>
