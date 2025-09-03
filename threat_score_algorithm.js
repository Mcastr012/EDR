// calculates CISA threat score based on MITRE ATT&CK id
function calculateThreatScore(attack_id)
{
	// MITRE ATT&CK pre-sets translated to
	// CISA minimum scores from the U.S.
	// Department of Homeland Security
	// e.g. minor attack = 10

	var minimum_score = 31;
	var functional_impact = 0;
	var observed_activity = 80;
	var activity_location = 50;
	var actor_type = 50;
	var information_impact = 0;
	var recoverability = 40;
	var cross_dependency = 35;
	var potential_impact = 0;

	// changes CISA weights based on
	// MITRE ATT&CK ids indicating
	// different types of attacks

	if (attack_id == "T1003")
	{
		functional_impact = 100;
		observed_activity = 100;
		information_impact = 80;
		potential_impact = 100;
	}

	if (attack_id == "T1004")
	{
		functional_impact = 20;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1028")
	{
		functional_impact = 100;
		information_impact = 70;
		potential_impact = 50;
	}

	if (attack_id == "T1035")
	{
		functional_impact = 35;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1042")
	{
		functional_impact = 35;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1053")
	{
		functional_impact = 35;
		information_impact = 20;
		potential_impact = 75;
	}

	if (attack_id == "T1059")
	{
		functional_impact = 35;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1060")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 75;
	}

	if (attack_id == "T1064")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 75;
	}

	if (attack_id == "T1070")
	{
		functional_impact = 60;
		information_impact = 70;
		potential_impact = 75;
	}

	if (attack_id == "T1037")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1076")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1085")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1086")
	{
		functional_impact = 35;
		information_impact = 50;
		potential_impact = 75;
	}

	if (attack_id == "T1088")
	{
		functional_impact = 60;
		information_impact = 50;
		potential_impact = 75;
	}

	if (attack_id == "T1101")
	{
		functional_impact = 35;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1103")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1117")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1122")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1128")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1131")
	{
		functional_impact = 60;
		information_impact = 80;
		potential_impact = 50;
	}

	if (attack_id == "T1138")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1140")
	{
		functional_impact = 60;
		information_impact = 70;
		potential_impact = 75;
	}

	if (attack_id == "T1170")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1180")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1182")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1183")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1191")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1196")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1197")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1202")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1216")
	{
		functional_impact = 60;
		information_impact = 50;
		potential_impact = 75;
	}

	if (attack_id == "T1218")
	{
		functional_impact = 60;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1220")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "T1223")
	{
		functional_impact = 0;
		information_impact = 0;
		potential_impact = 50;
	}

	if (attack_id == "C1000")
	{
		functional_impact = 35;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "C1001")
	{
		functional_impact = 35;
		information_impact = 50;
		potential_impact = 75;
	}

	if (attack_id == "C1002")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	if (attack_id == "C1003")
	{
		functional_impact = 60;
		information_impact = 20;
		potential_impact = 75;
	}

	if (attack_id == "C1004")
	{
		functional_impact = 0;
		information_impact = 50;
		potential_impact = 50;
	}

	if (attack_id == "C1005")
	{
		functional_impact = 35;
		information_impact = 50;
		potential_impact = 75;
	}

	if (attack_id == "C1006")
	{
		functional_impact = 0;
		information_impact = 20;
		potential_impact = 50;
	}

	// calculates maximum threat score based on cisa default algorithm
	var maximum_score = (functional_impact * (6/34)) + (observed_activity * (5/34)) + (activity_location * (4/34)) + (actor_type * (4/34)) + (information_impact * (2/34)) + (recoverability * (4/34)) + (cross_dependency * (3/34)) + (potential_impact * (6/34));

	// calculates cisa score based cisa default algorithm
	var cisa_score = ((maximum_score - minimum_score) / (100 - minimum_score)) * 100;

	// returns cisa score rounded to the nearest integer
	return Math.ceil(cisa_score)
}
