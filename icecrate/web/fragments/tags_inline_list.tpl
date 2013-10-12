% setdefault("tags", [])
<div class="inline-tags">
  % for taginfo, members in tags:
  <a class="tag" href="/tags/{{taginfo.get('name')}}">{{taginfo.get('name')}}</a>
  % end
</div>
