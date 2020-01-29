<?php
$done = false;
$events = [];
$guesses = 0;
while (!$done) {
	$guesses++;
	$days = [1,2,3,4,5];
	$locs = ['bst','kst','mst','qst','vst'];
	$fams = ['ford','ingram','powell','thornton','zimmerman'];
	$reqs = ['bounce','clown','magician','photo','superhero'];

	shuffle($days);
	shuffle($locs);
	shuffle($fams);
	shuffle($reqs);

	for ($i=1;$i<=5;$i++) {
		$events[$i]['day'] = array_pop($days);
		$events[$i]['loc'] = array_pop($locs);
		$events[$i]['fam'] = array_pop($fams);
		$events[$i]['req'] = array_pop($reqs);
	}
	
	$failed = false;
	foreach ($events as $event) {
		if ($event['fam']=='thornton' && ($event['req']=='bounce' || $event['req']=='photo') ) {
			$failed = true; break;
		}
		if ($event['fam']=='ford' && ($event['req']=='photo' || $event['req']=='superhero') ) {
			$failed = true; break;
		}
		if ($event['fam']=='ingram' && ($event['req']=='superhero') ) {
			$failed = true; break;
		}
		if ($event['fam']=='zimmerman' && (($event['req']!='bounce') || ($event['day']==5)) ) {
			$failed = true; break;
		}
		if ($event['req']=='clown' && $event['day']==5) {
			$failed = true; break;
		}
		if ($event['loc']=='kst' & $event['req']=='magician') {
			$failed = true; break;
		}

		// assignments
		if ($event['loc'] == 'kst')
			$kst_day = $event['day'];
		if ($event['req'] == 'magician') {
			$magician_day = $event['day'];
			$magician_loc = $event['loc'];
			$magician_fam = $event['fam'];
		}
		if ($event['req'] == 'superhero') {
			$superhero_day = $event['day'];
			$superhero_loc = $event['loc'];
		}
		if ($event['req'] == 'clown') {
			$clown_day = $event['day'];
			$clown_loc = $event['loc'];
		}
		if ($event['fam']=='thornton')
			$thornton_day = $event['day'];
		if ($event['req']=='photo')
			$photo_day = $event['day'];
		if ($event['req']=='bounce')
			$bounce_day = $event['day'];
		if ($event['loc']=='bst')
			$bst_day = $event['day'];
		if ($event['loc']=='vst')
			$vst_day = $event['day'];
	}
	if (!$failed) {
		if ($kst_day != ($magician_day+1)) {
			$failed = true;
		}
		if ($thornton_day != ($photo_day-2) || $thornton_day != ($bounce_day-3)) {
			$failed = true;
		}
		if ($bst_day <= $vst_day) {
			$failed = true;
		}
		if ($magician_loc != 'bst' && $magician_fam != 'thornton') {
			$failed = true;
		}

		if ($superhero_loc != 'qst' && $clown_loc != 'qst') {
			$failed = true;
		}
		if ($superhero_loc == 'qst' && $clown_day != 1) {
			$failed = true;
		}
		if ($clown_loc == 'qst' && $superhero_day != 1) {
			$failed = true;
		}
	}
	
	if ($failed) {
		continue;
	}
	
	$final_events = [];
	foreach ($events as $event) {
		$final_events[$event['day']] = $event;
	}
	asort($final_events);
	
	echo "Total guesses: {$guesses}\n";
	print_r($final_events);
	$done = true;
}
