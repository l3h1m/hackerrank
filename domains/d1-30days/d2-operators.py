// Day 2: Operators

mealCost =   float(input());
tipPercent = int(input());
taxPercent = int(input());

tip = mealCost * (float(tipPercent)/100);
tax = mealCost * (float(taxPercent)/100);

totalCost = mealCost + float(tip) + float(tax) ;

s1 = "The total meal cost is ";
s2 = " dollars";
cost = round(totalCost);

print (s1+str(cost)+s2 );
