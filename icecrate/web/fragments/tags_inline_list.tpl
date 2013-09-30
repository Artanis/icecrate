% setdefault("tags", [])
<div class="inline-tags">
  % for tag in tags:
  <a class="tag" href="/tags/{{tag.get('name')}}">{{tag.get('name')}}</a>
  % end
</div>
