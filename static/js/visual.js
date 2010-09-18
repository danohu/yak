jQuery.fn.dataTableExt.oSort['title-string-asc']  = function(a,b) {
	var x = a.match(/title="(.*?)"/)[1].toLowerCase();
	var y = b.match(/title="(.*?)"/)[1].toLowerCase();
	return ((x < y) ? -1 : ((x > y) ?  1 : 0));
};

jQuery.fn.dataTableExt.oSort['title-string-desc'] = function(a,b) {
	var x = a.match(/title="(.*?)"/)[1].toLowerCase();
	var y = b.match(/title="(.*?)"/)[1].toLowerCase();
	return ((x < y) ?  1 : ((x > y) ? -1 : 0));
};

$(document).ready(function(){
									
									$('.projectlist').dataTable({
				"bPaginate" : false,
        "bLengthChange" : false,
				"bFilter" : false,
				"bInfo" : false,
				"bAutoWidth" : false,
				"aaSorting" : [[1,"asc"]],
				"aoColumns" : [null, {"sType" : "title-string"}]
				});
	$('.projectlist').find('tr').click(function(){
			$(this).find('.todo').toggle();
			});
 //set each cell to contain the date
 $('.recurring_result').each(function(){
					  var col_html = $(this).parents('table').find('th').eq($(this).prevAll().length).html();	
						$(this).attr('date', col_html);
						});
 $('.recurring_result').click(function(){
			var data = {
			    'date' : $(this).attr('date'),
					'task_id' : $(this).parent('tr').attr('task_id'),
					'result' : $(this).parent('tr').attr('max')};
			var cell = $(this);
			$.get('/yak/do_task', data, function(d,t,r){
						//XXX: the callback doesn't work, but I can live with that
						cell.html(d);
						if(d == 'Undone'){
							cell.removeClass('recurring_done');
							cell.addClass('recurring_notdone');
						}
						else{
							cell.removeClass('recurring_notdone');
							cell.addClass('recurring_done');
						}
						});
			});
 $('.recurring_row').each(function(){
			var max = $(this).attr('max');
			$(this).find('td.recurring_result').each(function(i){
				  if($(this).html() >= max){
					   $(this).addClass('recurring_done');
						 }
					else{
					   $(this).addClass('recurring_notdone');
						 }
						 })
			});
	}); 
