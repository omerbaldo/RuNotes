$(document).ready(function() {
	var intervalFunc = function () {
		$('#notesFile').html($('#notesFile').val());
	};
	$('#notesFileButton').on('click', function () {
		$('#notesFile').click();
		setInterval(intervalFunc, 1);
		return false;
	});
});