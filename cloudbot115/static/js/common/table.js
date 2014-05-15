/**
 * table操作器
 * @required: jquery.js
 * @author 死线之蓝
 */

(function(obj) {
	var Tabler = function(tbl) {
		var table = tbl;
		var tbody = tbl.find('tbody');

		this.appendRow = function(data) {
			var row = tbody.find('tr:last').clone();
			var cells = row.children('td').each(function(index) {
				var cell = $(this);
				colName = cell.attr('data-column');
				if(colName) {
					cell.text(data[colName]);
				}
			});
			tbody.append(row);
		}
	};

	obj.fn.extend({
		tabler : function() {
			var tblr = this.data('_tabler');
			if(!tblr) {
				tblr = new Tabler(this);
				this.data('_tabler', tblr);
			}
			return tblr;
		}
	});
})(jQuery);
