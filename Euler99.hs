import System.IO
import Data.List.Split
import Data.List

-- returns largest element in a list of Integers
largest :: [Integer] -> Integer
largest (a:b) = foldr max 0 b

main = do 
	
	contents <- readFile "Euler99.txt" 
	
	let strings = words contents

	let stringpairs = map (splitOn ",") strings

	let numpairs = map (map (\a -> read a :: Integer)) stringpairs

	let exponentials = map (\[a,b] ->  a^b) numpairs
	
	let maxindex = elemIndex (largest exponentials) exponentials
	
	-- one less than the correct line number due to indexing by 0
	print maxindex