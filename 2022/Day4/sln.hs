import Data.List.Split (splitOn)
import Data.List (intersect)

main = do
    input <- readFile "Day4/input.txt"
    let parsed = map (splitOn ",") $ lines input
    print $ length $ filter checkAreas parsed
    print $ length $ filter checkAreas2 parsed

convertToRange :: [Char] -> [Integer]
convertToRange x = [read a :: Integer .. read b :: Integer] 
                    where [a,b] = splitOn "-" x

checkAreas :: [[Char]] -> Bool
checkAreas xs =  (a' `intersect` b') `elem` [a',b']  where [a',b'] = map convertToRange xs

checkAreas2 :: [[Char]] -> Bool
checkAreas2 xs =  (a' `intersect` b') /= []  where [a',b'] = map convertToRange xs