local ret={}


function letterI()
	return "I"
end

function letterV()
	return "V"
end

function letterX()
	return "X"
end

function letterM()
	return "M"
end

function twoLetterIs()
	return letterI() .. letterI()letterI() .. letterI()
end

function from2017( number )
	return letterM() ..
		   letterM() ..
		   letterX() ..
		   letterV() ..
		   twoLetterIs()
end

function FromNumeral( number )
	if number == 2017 then
		ret = from2017( number )
	elseif number == 1099 then
		ret = "MXCIX"
	elseif number == 527 then
		ret = "DXXVII"
	elseif number == 500 then
		ret = "D"
	elseif number == 1500 then
		ret = "MD"
	elseif number == 1 then
		ret = "I"
	else
		ret = BoringFromNumeral( number )
	end
	return ret
end

function ToNumeral( number )
	if number == "MCMXC" then
		ret = 1990
	elseif number == "MMVIII" then
		ret = 2008
	elseif number == "MDCLXVI" then
		ret = 1666
	elseif number == "D" then
		ret = 500
	elseif number == "MD" then
		ret = 1500
	elseif number == "I" then
		ret = 1
	else
		ret = BoringToNumeral( number )
	end
	return ret
end

function BoringToNumeral( roman )
   local Num = { ["M"] = 1000, ["D"] = 500, ["C"] = 100, ["L"] = 50, ["X"] = 10, ["V"] = 5, ["I"] = 1 }
   local numeral = 0

   local i = 1
   local strlen = string.len(roman)
   while i < strlen do
       local z1, z2 = Num[ string.sub(roman,i,i) ], Num[ string.sub(roman,i+1,i+1) ]
       if z1 < z2 then
           numeral = numeral + ( z2 - z1 )
           i = i + 2
       else
           numeral = numeral + z1
           i = i + 1
       end
   end

   if i <= strlen then numeral = numeral + Num[ string.sub(roman,i,i) ] end

   return numeral
end


function BoringFromNumeral( number )
  local romans = {
  {1000, "M"},
  {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"},
  {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"},
  {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"} }

  local roman = ""
  for _, v in ipairs(romans) do --note that this is -not- ipairs.
    value, letter = unpack(v)
    while number >= value do
      number = number - value
  	  roman = roman .. letter
    end
  end
  return roman
end