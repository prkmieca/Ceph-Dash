function enableReplicated() {


	document.getElementById("group-erasure-pool-rule").setAttribute("hidden", "true");
	document.getElementById("group-erasure-pool-code-profile").setAttribute("hidden", "true");

	document.getElementById("group-replicated-pool-rule1").removeAttribute("hidden");
	document.getElementById("poolSize").removeAttribute("hidden");

}


function enableErasured() {


	document.getElementById("group-replicated-pool-rule1").setAttribute("hidden", "true");
	document.getElementById("poolSize").setAttribute("hidden", "true");

	document.getElementById("group-erasure-pool-rule").removeAttribute("hidden");
	document.getElementById("group-erasure-pool-code-profile").removeAttribute("hidden");

}

