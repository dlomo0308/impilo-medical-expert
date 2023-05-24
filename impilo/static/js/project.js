$(document).ready(() => {
  // Get references to the necessary elements
  const symptomsSelect = $('#symptoms-select');
  const symptomList = $('#symptom-list');
  const selectedSymptomsField = $('#selected-symptoms-field');
  const diagnoseBtn = $('#diagnose-btn');
  const selectedSymptoms = [];

  // Add an event listener to the symptoms select element
  symptomsSelect.on('change', () => {
    // Get the selected option and symptom
    const selectedOption = symptomsSelect.find('option:selected');
    const selectedSymptom = selectedOption.val();

    // disable the selected symptom from the list
    if (selectedSymptoms.includes(selectedSymptom)) {
      alert('You have already selected this symptom.');
      selectedOption.prop('selected', false);
      return;
    }
    // Check if the maximum number of symptoms has been selected
    if (selectedSymptoms.length >= 5) {
      alert('You have already selected the maximum number of symptoms.');
      selectedOption.prop('selected', false);
      return;
    }

    // Add the selected symptom to the list
    selectedSymptoms.push(selectedSymptom);
    const symptomListItem = $('<li>').text(selectedSymptom).addClass('selected');
    const closeIcon = $('<span>').addClass('close-icon text-danger').attr('aria-hidden', 'true').html('&times;');
    symptomListItem.append(closeIcon);
    symptomList.append(symptomListItem);

    // Add an event listener to the close icon to remove the selected symptom
    closeIcon.on('click', () => {
      removeSelectedSymptom(selectedSymptom, symptomListItem);
    });

    // Update the selected symptoms field with the updated list of symptoms
    selectedSymptomsField.val(JSON.stringify(selectedSymptoms));

    // Disable the diagnose button if the number of selected symptoms is invalid
    if (selectedSymptoms.length === 0 || selectedSymptoms.length > 5) {
      diagnoseBtn.attr('disabled', '');
    } else {
      diagnoseBtn.removeAttr('disabled');
    }
  });

  // Add an event listener to the diagnosis form to validate the selected symptoms
  const form = $('#diagnosis-form');
  form.on('submit', (event) => {
    const selectedSymptoms = JSON.parse(selectedSymptomsField.val());
    if (selectedSymptoms.length < 3) {
      event.preventDefault();
      alert('Please select at least three symptom.');
    } else if (selectedSymptoms.length > 5) {
      event.preventDefault();
      alert('You have selected too many symptoms.');
    }
  });

  // Disable the "Select Symptoms" option
  symptomsSelect.find('option:first-child').prop('disabled', true);

  // Define a function to remove a selected symptom
  function removeSelectedSymptom(symptom, listItem) {
    const symptomIndex = selectedSymptoms.indexOf(symptom);
    if (symptomIndex > -1) {
      selectedSymptoms.splice(symptomIndex, 1);
      listItem.remove();
      // Disable the diagnose button if the number of selected symptoms is invalid
      if (selectedSymptoms.length === 0 || selectedSymptoms.length > 5) {
        diagnoseBtn.attr('disabled', '');
      } else {
        diagnoseBtn.removeAttr('disabled');
      }
    }
    // Update the selected symptoms field with the updated list of symptoms
    selectedSymptomsField.val(JSON.stringify(selectedSymptoms));
  }
});