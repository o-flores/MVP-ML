const BASE_URL = "http://127.0.0.1:5000";

const predict = async (e) => {
	e.preventDefault();

	const formData = new FormData(e.target);
	const formProps = Object.fromEntries(formData.entries());

	try {
		const response = await fetch(`${BASE_URL}/predict`, {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify(formProps),
		});

		const { outcome } = await response.json();
		const message =
			outcome === 1
				? "Há grandes chances de você estar com algum nível de obesidade, considere mudar alguns hábitos"
				: "Há grandes chances de você levar uma vida saudável, continue assim";
		alert(message);
		e.target.reset();
	} catch (error) {
		console.error("Error:", error);
	}
};

const onLoad = () => {
	const form = document.getElementById("form");
	form.onsubmit = predict;
};

window.onload = onLoad();
