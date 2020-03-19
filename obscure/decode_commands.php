<?php
$k="80e32263";
$kh="6f8af44abea0";
$kf="351039f4a7b5";

$input1 = "3Qve>.IXeOLC>[D&6f8af44abea0QKwu/Xr7GuFo50p4HuAZHBfnqhv7/+ccFfisfH4bYOSMRi0eGPgZuRd6SPsdGP//c+dVM7gnYSWvlINZmlWQGyDpzCowpzczRely/Q351039f4a7b5+'Qn/?>-
e=ZU mx";

$input2 = "3Qve>.IXeOLC>[D&6f8af44abea0QKxo+HM4thMoMKWcSng9UZNbdc4WFhO2jaU4eMhPaDTePEuB48JstWIb4aEirLpXpdgb7g8Bx/IGI/JLbVRcFack+r90YxXpmBA1wQKaU9jeRhvp7imF351039f4a7b5+'Qn/?>-
e=ZU mx";

$input3 = "3Qve>.IXeOLC>[D&6f8af44abea0QKxI+Ak49hMoNaXoypsATiJfd3clJ+KmL5OyfLiGNSBKHFWppDXbjhH/M9orZ0qPjQ14MLA5CjeLxAG9/fBJgQyWrbiZPrCFcj3xDb95CvC29r/AN2ziEh0351039f4a7b5+'Qn/?>-
e=ZU mx";

$input4 = "3Qve>.IXeOLC>[D&6f8af44abea0QKwu/Xr7GuFo56r7/X/jfHEdLv77HX4eaufRRXofHPkXukp5H/oZGfH8LuQCMrwmbybyl9RYnhQdJsKpqxrepRMoTSemlRLaXZdBZhoq75ohMhAxMvrQKEw351039f4a7b5 'Qn/?>-
e";

preg_match("/$kh(.+)$kf/",$input4,$m);


$mystr = $m[1];

$t = base64_decode($mystr);

  $c=strlen($k);
  $l=strlen($t);
  $o="";
  for($i=0;$i<$l;)
    {
     for($j=0;($j<$c&&$i<$l);$j++,$i++)
       {$o.=$t{$i}^$k{$j};}
    }

print(gzuncompress($o))

?>
