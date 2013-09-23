// http://stackoverflow.com/a/4673436/152313
// First, checks if it isn't implemented yet.
if (!String.prototype.format) {
  String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}

$(document).ready(function() {
    // Transform all zxing-class links into zxing callbacks
    $(".zxing").each(function(index) {
        var path = encodeURIComponent(decodeURIComponent(this.href));
        this.href = "zxing://scan/?ret={0}".format(path);

    })
});
