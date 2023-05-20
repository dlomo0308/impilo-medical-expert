$(document).ready(() => {
  const symptomsSelect = $('#symptoms-select');
  const symptomList = $('#symptom-list');
  const selectedSymptomsField = $('#selected-symptoms-field');
  const diagnoseBtn = $('#diagnose-btn');
  const selectedSymptoms = [];

  symptomsSelect.on('change', () => {
    const selectedOption = symptomsSelect.find('option:selected');
    const selectedSymptom = selectedOption.val();
    if (selectedSymptoms.length >= 5) {
      alert('You have already selected the maximum number of symptoms.');
      selectedOption.prop('selected', false);
      return;
    }
    selectedSymptoms.push(selectedSymptom);

    const symptomListItem = $('<li>').text(selectedSymptom).addClass('selected');
    const closeIcon = $('<span>').addClass('close-icon text-danger').attr('aria-hidden', 'true').html('&times;');
    symptomListItem.append(closeIcon);
    symptomList.append(symptomListItem);

    // Add an event listener to the close icon to remove the selected symptom
    closeIcon.on('click', () => {
      removeSelectedSymptom(selectedSymptom, symptomListItem);
    });

    selectedSymptomsField.val(JSON.stringify(selectedSymptoms));

    if (selectedSymptoms.length === 0 || selectedSymptoms.length > 5) {
      diagnoseBtn.attr('disabled', '');
    } else {
      diagnoseBtn.removeAttr('disabled');
    }
  });

  const form = $('#diagnosis-form');
  form.on('submit', (event) => {
    const selectedSymptoms = JSON.parse(selectedSymptomsField.val());
    if (selectedSymptoms.length === 0) {
      event.preventDefault();
      alert('Please select at least one symptom.');
    } else if (selectedSymptoms.length > 5) {
      event.preventDefault();
      alert('You have selected too many symptoms.');
    }
  });

  symptomsSelect.find('option:first-child').prop('disabled', true); // Disable the "Select Symptoms" option

  function removeSelectedSymptom(symptom, listItem) {
    const symptomIndex = selectedSymptoms.indexOf(symptom);
    if (symptomIndex > -1) {
      selectedSymptoms.splice(symptomIndex, 1);
      listItem.remove();
      if (selectedSymptoms.length === 0 || selectedSymptoms.length > 5) {
        diagnoseBtn.attr('disabled', '');
      } else {
        diagnoseBtn.removeAttr('disabled');
      }
    }
    selectedSymptomsField.val(JSON.stringify(selectedSymptoms));
  }


});



