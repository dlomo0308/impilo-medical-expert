$(document).ready(function() {
  const symptomSelect = $('#symptoms-select');
  const symptomList = $('#symptom-list');
  const selectedSymptomsField = $('#selected-symptoms-field');
  const diagnoseBtn = $('#diagnose-btn');
  const selectedSymptoms = [];

  function updateSelectedSymptoms() {
      selectedSymptomsField.val(JSON.stringify(selectedSymptoms));
      symptomList.empty();
      for (const symptom of selectedSymptoms) {
          const symptomListItem = $('<li>').text(symptom).addClass('selected');
          const closeIcon = $('<span>').addClass('close-icon text-danger').attr('aria-hidden', 'true').html('&times');
          symptomListItem.append(closeIcon);
          symptomList.append(symptomListItem);

          // Add an event listener to the close icon to remove the selected symptom
          closeIcon.on('click', () => {
              const symptomIndex = selectedSymptoms.indexOf(symptom);
              if (symptomIndex > -1) {
                  selectedSymptoms.splice(symptomIndex, 1);
                  updateSelectedSymptoms();
                  symptomSelect.append(new Option(symptom, symptom));
                  if (selectedSymptoms.length === 0 || selectedSymptoms.length > 5) {
                      diagnoseBtn.attr('disabled', '');
                  } else {
                      diagnoseBtn.removeAttr('disabled');
                  }
              }
          });
      }

      // Remove the corresponding option from the select element for selected symptoms
      const options = symptomSelect.find('option');
      options.each((index, option) => {
          const $option = $(option);
          if (selectedSymptoms.includes($option.text())) {
              $option.prop('disabled', true).addClass('selected');
          } else {
              $option.prop('disabled', false).removeClass('selected');
          }
      });

      if (selectedSymptoms.length === 0 || selectedSymptoms.length > 5) {
          diagnoseBtn.attr('disabled', '');
      } else {
          diagnoseBtn.removeAttr('disabled');
      }
  }

  symptomSelect.on('change', (event) => {
      const selectedOption = $(event.target).find(':selected');
      const selectedSymptom = selectedOption.text();
      if (selectedSymptoms.length >= 5) {
          alert('You have already selected the maximum number of symptoms.');
          selectedOption.prop('selected', false);
          return;
      }
      selectedSymptoms.push(selectedSymptom);
      updateSelectedSymptoms();
      selectedOption.prop('disabled', true);
  });

  const form = $('#diagnosis-form');
  form.on('submit', (event) => {
      if (selectedSymptoms.length === 0) {
          event.preventDefault();
          alert('Please select at least one symptom.');
      } else if (selectedSymptoms.length > 5) {
          event.preventDefault();
          alert('You have selected too many symptoms.');
      }
  });

  symptomSelect.find('option:first-child').prop('disabled', true); // Disable the "Select Symptoms" option
});