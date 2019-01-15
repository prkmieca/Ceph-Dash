
function Disable() {

    document.getElementById("exampleFormControlSelect1").setAttribute("hidden", "true");
    document.getElementById("exampleFormControlSelect2").setAttribute("hidden", "true");
    document.getElementById("group-rack").setAttribute("hidden", "true");
    document.getElementById("group-chasis").setAttribute("hidden", "true");


}

function EnableRack() {

	document.getElementById("exampleFormControlSelect2").setAttribute("hidden", "true");
	document.getElementById("group-chasis").setAttribute("hidden", "true");

	document.getElementById("exampleFormControlSelect1").removeAttribute("hidden");
	document.getElementById("group-rack").removeAttribute("hidden");


}


function EnableChasis() {

	document.getElementById("exampleFormControlSelect1").setAttribute("hidden", "true");
	document.getElementById("group-rack").setAttribute("hidden", "true");

	document.getElementById("exampleFormControlSelec2").removeAttribute("hidden");
	document.getElementById("group-chasis").removeAttribute("hidden");


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