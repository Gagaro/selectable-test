$(document).ready(
    function () {
	$('#id_autocomplete').on("autocompleteopen", function(event, ui) {
	    console.log('autocompleteopen');
	});
	$('#id_autocomplete').on("djselectableopen", function(event, ui) {
	    console.log('djselectableopen');
	});
    }
);