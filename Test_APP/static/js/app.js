
	window.onload = function typeAnimation() {
		Typed.new("#writing-text", {
			strings: [
				"Bem vindo !", "Projectos de arquitectura", "Proposição de serviços a seu pedido", "À sua disposição!"
			],
			// Optionally use an HTML element to grab strings from (must wrap each string in a <p>)
			stringsElement: null,
			// typing speed
			typeSpeed: 1,
			contentType: 'text',
			callback: function() {
				$("#writing-text").css({"color": "#fff", "background-color": "#C8412B"});
			},
			preStringTyped: function() {},
			onStringTyped: function() {}
		});
	};

