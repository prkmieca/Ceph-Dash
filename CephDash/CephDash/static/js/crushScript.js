
function Disable() {

    document.getElementById("group-rack").setAttribute("hidden", "true");
    document.getElementById("group-chasis").setAttribute("hidden", "true");

    console.log("root clicked")
}

function EnableRack() {


	document.getElementById("group-chasis").setAttribute("hidden", "true");

	document.getElementById("group-rack").removeAttribute("hidden");

	console.log("rack clicked")
}


function EnableChasis() {


	document.getElementById("group-rack").setAttribute("hidden", "true");

	document.getElementById("group-chasis").removeAttribute("hidden");

	console.log("chasis clicked")
}

function DisableErasured() {


	document.getElementById("group-code-profile").setAttribute("hidden", "true");
	document.getElementById("group-r").removeAttribute("hidden");
    document.getElementById("group-pt").removeAttribute("hidden");


}

function DisableReplicated() {


	document.getElementById("group-r").setAttribute("hidden", "true");
	document.getElementById("group-pt").setAttribute("hidden", "true");
	document.getElementById("group-code-profile").removeAttribute("hidden");

}