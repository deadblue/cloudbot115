/**
 * @author 死线之蓝
 */

(function(){
	$('#btn_account_modal').click(function(){
		$('#modal_account').modal('show');
	});
	
	$('#btn_account_add').click(function(){
		var self = $(this);
		self.button('loading');
		var acnt = $('#txt_account').val();
		var pwd = $('#txt_password').val();
		$.post('ajax/account', {
			'action' : 'insert',
			'account' : acnt,
			'password' : pwd
		}, function(data) {
			self.button('reset');
			$('#modal_account').modal('hide');
			$('#tbl_account').tabler().appendRow({
				'account' : acnt,
				'password' : pwd,
				'last_active_time' : '-'
			});
		})
	});
})();
