function adjustNumberOfPeople(operation) {
	var numberOfPeople = parseInt(document.getElementById("numberOfPeople").value);
	var nopField = document.getElementById("numberOfPeople");

	if (!isNaN(numberOfPeople)) {
		if (operation == "increase") {
			numberOfPeople++;
		} else if (numberOfPeople > 0) {
			numberOfPeople--;
		}
		nopField.value = numberOfPeople;
	};
}

function allowNumbersOnly(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
}
