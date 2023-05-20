$("#diagnosis-form").submit(function(event) {
    event.preventDefault();
    var selectedSymptoms = [];
    $("input[name='symptoms']:checked").each(function() {
      selectedSymptoms.push($(this).val());
    });
    $.ajax({
      type: "POST",
      url: "/diagnosiz/",
      data: {
        selected_symptoms: JSON.stringify(selectedSymptoms),
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      },
      dataType: "json",
      success: function(response) {
        console.log(response);
        var predictedDisease = response.predicted_disease;
        console.log(predictedDisease);
        $("#diagnosis-result").text("The predicted disease is: " + predictedDisease);
      },
      error: function(xhr, textStatus, errorThrown) {
        console.log("Error: " + errorThrown);
      }
    });
  });


  

// $(document).ready(() => {
//   const symptomsSelect = $('#symptoms-select');
//   const symptomList = $('#symptom-list');
//   const selectedSymptomsField = $('#selected-symptoms-field');
//   const diagnoseBtn = $('#diagnose-btn');
//   const selectedSymptoms = [];

//   symptomsSelect.on('change', () => {
//     const selectedOption = symptomsSelect.find('option:selected');
//     const selectedSymptom = selectedOption.val();
//     if (selectedSymptoms.length >= 5) {
//       alert('You have already selected the maximum number of symptoms.');
//       selectedOption.prop('selected', false);
//       return;
//     }
//     selectedSymptoms.push(selectedSymptom);

//     const symptomListItem = $('<li>').text(selectedSymptom);
//     const closeIcon = $('<span>').addClass('close-icon text-danger').attr('aria-hidden', 'true').html('&times;');
//     symptomListItem.append(closeIcon);
//     symptomList.append(symptomListItem);

//     // Add an event listener to the close icon to remove the selected symptom
//     closeIcon.on('click', () => {
//       removeSelectedSymptom(selectedSymptom, symptomListItem);
//     });

//     selectedSymptomsField.val(JSON.stringify(selectedSymptoms));

//     if (selectedSymptoms.length === 0 || selectedSymptoms.length > 5) {
//       diagnoseBtn.attr('disabled', '');
//     } else {
//       diagnoseBtn.removeAttr('disabled');
//     }
//   });

//   const form = $('#diagnosis-form');
//   form.on('submit', (event) => {
//     event.preventDefault();
//     const selectedSymptoms = JSON.parse(selectedSymptomsField.val());
//     if (selectedSymptoms.length === 0) {
//       alert('Please select at least one symptom.');
//       return;
//     } else if (selectedSymptoms.length > 5) {
//       alert('You have selected too many symptoms.');
//       return;
//     }

//     $.ajax({
//       url: '/diagnose/',
//       type: 'POST',
//       contentType: 'application/json',
//       data: JSON.stringify({ selected_symptoms: selectedSymptoms }),
//       success: function(response) {
//         // Redirect to the results page with the diagnosis and selected symptoms as URL parameters
//         window.location.href = '/results?diagnosis=' + response.diagnosis.join(',') + '&selected_symptoms=' + encodeURIComponent(JSON.stringify(response.selected_symptoms));
//       },
//       error: function(xhr, status, error) {
//         console.error('Error:', error);
//         alert('An error occurred while diagnosing the disease.');
//       }
//     });
//   });

//   symptomsSelect.find('option:first-child').prop('disabled', true); // Disable the "Select Symptoms" option

//   function removeSelectedSymptom(symptom, listItem) {
//     const symptomIndex = selectedSymptoms.indexOf(symptom);
//     if (symptomIndex > -1) {
//       selectedSymptoms.splice(symptomIndex, 1);
//       listItem.remove();
//       if (selectedSymptoms.length === 0 || selectedSymptoms.length > 5) {
//         diagnoseBtn.attr('disabled', '');
//       } else {
//         diagnoseBtn.removeAttr('disabled');
//       }
//     }
//     selectedSymptomsField.val(JSON.stringify(selectedSymptoms));
//   }
// });








