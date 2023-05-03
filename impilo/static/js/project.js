$(document).ready(function() {
    // Get a reference to the selected symptoms paragraph element
    var selectedSymptoms = $('#selected-symptoms');

    // Listen for changes to the symptoms checkboxes
    $('input[name="symptoms[]"]').on('change', function() {
        // Get an array of the currently selected symptoms
        var selectedSymptomsArray = $('input[name="symptoms[]"]:checked').map(function() {
            return $(this).val();
        }).get();

        // Update the selected symptoms paragraph with the currently selected symptoms
        if (selectedSymptomsArray.length > 0) {
            selectedSymptoms.text('Selected symptoms: ' + selectedSymptomsArray.join(', '));
        } else {
            selectedSymptoms.empty();
        }
    });

    // Listen for clicks on the diagnose button
    $('#diagnose-button').on('click', function() {
        // Get the selected symptoms and send them to the server using AJAX
        var selectedSymptoms = $('input[name="symptoms[]"]:checked').map(function() {
            return $(this).val();
        }).get();

        $.ajax({
            url: '{% url "process_symptoms" %}',
            type: 'POST',
            data: {'symptoms[]': selectedSymptoms},
            dataType: 'json',
            success: function(response) {
                console.log(response.selected_symptoms);
            },
            error: function(xhr, status, error) {
                console.log('Error:', error);
            }
        });
    });
});