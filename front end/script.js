function sendToTaylor() {
	var inputText = document.getElementById("input-text").value;
	if (inputText.trim() === "") {
		alert("Please enter some text.");
		return;
	}
	var endpointUrl = "http://54.210.245.233:8000/" + encodeURIComponent(inputText);
	fetch(endpointUrl)
		.then(response => response.json())
		.then(data => {
			var resultLabel = document.getElementById("result-label");
			resultLabel.innerHTML = "Taylor says: " + data[inputText];
			resultLabel.style.display = "block";
		})
		.catch(error => {
			alert("An error occurred: " + error.message);
		});
}